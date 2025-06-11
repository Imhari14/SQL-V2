"""
Advanced SAP HANA SQL Parser for Migration Analysis
==================================================

This module provides sophisticated SQL parsing capabilities for SAP HANA procedures,
focusing on migration requirements analysis including:
- Complex join relationship analysis
- Filter condition consolidation across procedures
- Data lineage and dependency mapping
"""

import re
import sqlparse
import sys
import os
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional, Any
from dataclasses import dataclass, field
from collections import defaultdict, Counter
import networkx as nx

# Try to import ANTLR if available
try:
    # Add the parent directory to path to access ANTLR generated files
    parent_dir = Path(__file__).parent.parent
    generated_dir = parent_dir / "generated"
    if generated_dir.exists():
        sys.path.insert(0, str(generated_dir))

        from antlr4 import *
        from HanaLexer import HanaLexer
        from HanaParser import HanaParser
        from HanaListener import HanaListener
        ANTLR_AVAILABLE = True
        print("✅ ANTLR SAP HANA grammar available")
    else:
        ANTLR_AVAILABLE = False
        print("⚠️ ANTLR generated files not found, using sqlparse fallback")
except ImportError:
    ANTLR_AVAILABLE = False
    print("⚠️ ANTLR not available, using sqlparse fallback")

@dataclass
class TableReference:
    """Represents a table reference with all its usage details"""
    name: str
    schema: Optional[str] = None
    alias: Optional[str] = None
    columns: Set[str] = field(default_factory=set)
    usage_contexts: Set[str] = field(default_factory=set)  # SELECT, JOIN, WHERE, etc.
    
    @property
    def full_name(self) -> str:
        return f"{self.schema}.{self.name}" if self.schema else self.name

@dataclass
class FilterCondition:
    """Represents a filter condition with detailed analysis"""
    table: str
    column: str
    operator: str
    values: List[str]
    condition_text: str
    procedure_id: str
    is_parameter: bool = False
    
@dataclass
class JoinRelationship:
    """Represents a join relationship between tables"""
    left_table: str
    right_table: str
    join_type: str
    condition: str
    procedure_id: str
    left_columns: List[str] = field(default_factory=list)
    right_columns: List[str] = field(default_factory=list)

@dataclass
class Parameter:
    """Represents a procedure parameter"""
    name: str
    data_type: str
    direction: str = 'IN'

@dataclass
class ProcedureAnalysis:
    """Complete analysis of a single procedure"""
    procedure_id: str
    tables: Dict[str, TableReference]
    filters: List[FilterCondition]
    joins: List[JoinRelationship]
    parameters: List[Dict[str, Any]]
    raw_sql: str
    complexity_score: int = 0

class SAP_HANA_Listener(HanaListener if ANTLR_AVAILABLE else object):
    """Basic ANTLR listener for SAP HANA SQL parsing"""

    def __init__(self):
        self.tables = set()
        self.columns = defaultdict(set)
        self.joins = []
        self.filters = []
        self.current_table_alias = {}

    def enterTableName(self, ctx):
        """Extract table names"""
        if hasattr(ctx, 'getText'):
            table_name = ctx.getText().strip('"').upper()
            if len(table_name) >= 3 and table_name.isalpha():
                self.tables.add(table_name)

    def enterColumnName(self, ctx):
        """Extract column references"""
        if hasattr(ctx, 'getText'):
            column_ref = ctx.getText()
            if '.' in column_ref:
                table, column = column_ref.split('.', 1)
                self.columns[table.upper()].add(column.upper())

class Enhanced_SAP_HANA_Listener(HanaListener if ANTLR_AVAILABLE else object):
    """Enhanced ANTLR listener for detailed SAP HANA SQL parsing"""

    def __init__(self):
        self.tables = set()
        self.columns = defaultdict(set)
        self.joins = []
        self.filters = []
        self.parameters = []
        self.table_aliases = {}
        self.current_context = None
        self.filter_conditions = []
        self.join_conditions = []
        self.current_sql_text = ""

    def set_sql_text(self, sql_text: str):
        """Set the original SQL text for fallback parsing"""
        self.current_sql_text = sql_text

    def enterEveryRule(self, ctx):
        """Track context for better parsing"""
        rule_name = type(ctx).__name__

        # Extract table and column information from any rule that contains SQL
        if hasattr(ctx, 'getText'):
            text = ctx.getText()

            # Look for table.column patterns
            if '.' in text and len(text) < 100:  # Avoid very long texts
                self._extract_table_column_patterns(text)

            # Look for table aliases in FROM/JOIN clauses
            if any(keyword in text.upper() for keyword in ['FROM', 'JOIN']):
                self._extract_table_aliases(text)

    def _extract_table_column_patterns(self, text: str):
        """Extract table.column patterns from any text"""
        import re

        # Pattern for table.column references
        pattern = r'(\w+)\.(\w+)'
        matches = re.findall(pattern, text, re.IGNORECASE)

        for table_or_alias, column in matches:
            table_upper = table_or_alias.upper()
            column_upper = column.upper()

            # Skip obvious non-table patterns
            if (len(table_upper) >= 2 and len(column_upper) >= 2 and
                table_upper not in ['AND', 'OR', 'IN', 'ON', 'AS', 'IS', 'NOT'] and
                column_upper not in ['AND', 'OR', 'IN', 'ON', 'AS', 'IS', 'NOT']):

                # Check if it's a known SAP table or reasonable table name
                if (table_upper in ['BSEG', 'BKPF', 'VBAK', 'VBAP', 'VBRK', 'VBRP', 'LFA1', 'KNA1'] or
                    (len(table_upper) >= 3 and len(table_upper) <= 8 and table_upper.isalnum())):

                    self.tables.add(table_upper)
                    self.columns[table_upper].add(column_upper)

    def _extract_table_aliases(self, text: str):
        """Extract table aliases from FROM/JOIN clauses"""
        import re

        # Pattern for table aliases
        alias_patterns = [
            r'FROM\s+(\w+)\s+(\w+)',
            r'JOIN\s+(\w+)\s+(\w+)',
            r'INNER\s+JOIN\s+(\w+)\s+(\w+)',
            r'LEFT\s+JOIN\s+(\w+)\s+(\w+)',
            r'RIGHT\s+JOIN\s+(\w+)\s+(\w+)'
        ]

        for pattern in alias_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for table, alias in matches:
                table_upper = table.upper()
                alias_upper = alias.upper()

                # Valid alias mapping
                if (len(alias_upper) <= 3 and
                    alias_upper not in ['ON', 'WHERE', 'AND', 'OR', 'AS'] and
                    table_upper != alias_upper):
                    self.table_aliases[alias_upper] = table_upper

    def enterTable_name(self, ctx):
        """Extract table names with better accuracy"""
        if hasattr(ctx, 'getText'):
            table_text = ctx.getText().strip('"').strip("'").upper()
            # Filter out obvious non-table names
            if (len(table_text) >= 3 and
                table_text.isalnum() and
                not table_text.isdigit() and
                table_text not in ['AND', 'OR', 'IN', 'ON', 'AS']):
                self.tables.add(table_text)

    def enterColumn_name(self, ctx):
        """Extract column references with table context"""
        if hasattr(ctx, 'getText'):
            column_ref = ctx.getText().strip()
            if '.' in column_ref:
                parts = column_ref.split('.')
                if len(parts) == 2:
                    table, column = parts
                    table = table.strip('"').strip("'").upper()
                    column = column.strip('"').strip("'").upper()
                    if table and column:
                        self.columns[table].add(column)

    def enterParameter(self, ctx):
        """Extract parameters"""
        if hasattr(ctx, 'getText'):
            param_text = ctx.getText()
            if param_text.startswith(':'):
                self.parameters.append(param_text)

    def enterWhere_clause(self, ctx):
        """Extract WHERE clause conditions"""
        if hasattr(ctx, 'getText'):
            condition_text = ctx.getText()
            self.filter_conditions.append(condition_text)

    def enterJoin_clause(self, ctx):
        """Extract JOIN conditions"""
        if hasattr(ctx, 'getText'):
            join_text = ctx.getText()
            self.join_conditions.append(join_text)

    def finalize_parsing(self):
        """Finalize parsing by resolving aliases and cleaning up data"""

        # Always try to extract more data with fallback parsing
        if self.current_sql_text:
            self._fallback_regex_parsing()

        # Resolve aliases in columns
        resolved_columns = defaultdict(set)

        for table_or_alias, columns in self.columns.items():
            # Check if this is an alias
            actual_table = self.table_aliases.get(table_or_alias, table_or_alias)
            resolved_columns[actual_table].update(columns)

        self.columns = resolved_columns

        # Add aliased tables to main tables set
        for alias, table in self.table_aliases.items():
            self.tables.add(table)

    def _fallback_regex_parsing(self):
        """Enhanced fallback regex parsing for different SQL patterns"""
        import re

        sql = self.current_sql_text

        # Extract tables from FROM/JOIN clauses
        table_patterns = [
            r'FROM\s+([a-zA-Z][a-zA-Z0-9_]{2,15})\s+(?:AS\s+)?(\w+)?',
            r'JOIN\s+([a-zA-Z][a-zA-Z0-9_]{2,15})\s+(?:AS\s+)?(\w+)?',
            r'INNER\s+JOIN\s+([a-zA-Z][a-zA-Z0-9_]{2,15})\s+(?:AS\s+)?(\w+)?',
            r'INSERT\s+INTO\s+([a-zA-Z][a-zA-Z0-9_]{2,15})',
            r'TRUNCATE\s+TABLE\s+([a-zA-Z][a-zA-Z0-9_]{2,15})',
        ]

        for pattern in table_patterns:
            matches = re.finditer(pattern, sql, re.IGNORECASE)
            for match in matches:
                table = match.group(1).upper()
                alias = match.group(2) if len(match.groups()) > 1 else None

                if table and len(table) >= 3:
                    self.tables.add(table)

                    if alias and len(alias) <= 3:
                        self.table_aliases[alias.upper()] = table

        # Extract columns from SELECT statements (handle INSERT...SELECT pattern)
        self._extract_select_columns(sql)

        # Extract all table.column patterns
        column_pattern = r'(\w+)\.(\w+)'
        matches = re.findall(column_pattern, sql, re.IGNORECASE)

        for table_or_alias, column in matches:
            table_upper = table_or_alias.upper()
            column_upper = column.upper()

            # Resolve alias
            actual_table = self.table_aliases.get(table_upper, table_upper)

            if actual_table in self.tables:
                self.columns[actual_table].add(column_upper)

    def _extract_select_columns(self, sql: str):
        """Extract columns from SELECT statements, especially INSERT...SELECT"""
        import re

        # Pattern for SELECT columns in INSERT...SELECT statements
        select_pattern = r'SELECT\s+(.*?)\s+FROM\s+(\w+)'
        matches = re.finditer(select_pattern, sql, re.IGNORECASE | re.DOTALL)

        for match in matches:
            columns_text = match.group(1)
            table_name = match.group(2).upper()

            # Add the table
            self.tables.add(table_name)

            # Extract individual columns
            # Split by comma and clean up
            column_list = [col.strip() for col in columns_text.split(',')]

            for column in column_list:
                # Remove aliases (AS keyword)
                column = re.sub(r'\s+as\s+\w+', '', column, flags=re.IGNORECASE)
                # Remove functions and expressions, keep just column names
                column = column.strip()

                # Skip complex expressions, keep simple column names
                if (column and
                    not any(char in column for char in ['(', ')', '+', '-', '*', '/', '\'', '"']) and
                    column.upper() not in ['CURRENT_TIMESTAMP', 'CURRENT_DATE'] and
                    not column.isdigit()):

                    column_upper = column.upper()
                    if len(column_upper) >= 2 and column_upper.replace('_', '').isalnum():
                        self.columns[table_name].add(column_upper)

class AdvancedSQLParser:
    """Advanced SQL parser for SAP HANA migration analysis with ANTLR support"""

    def __init__(self):
        self.use_antlr = ANTLR_AVAILABLE
        self.sap_table_patterns = {
            'VBAK': 'Sales Document Header',
            'VBAP': 'Sales Document Items',
            'VBRK': 'Billing Document Header',
            'VBRP': 'Billing Document Items',
            'BKPF': 'Accounting Document Header',
            'BSEG': 'Accounting Document Line Items',
            'CDHDR': 'Change Document Header',
            'CDPOS': 'Change Document Items',
            'KNA1': 'Customer Master',
            'LFA1': 'Vendor Master',
            'MARA': 'Material Master',
            'MARD': 'Material Stock Data',
            'MAKT': 'Material Descriptions',
            'USR02': 'User Master Record',
            'USH02': 'User Master Record (Historical)'
        }

        print(f"🔧 SQL Parser initialized with {'ANTLR' if self.use_antlr else 'sqlparse'} backend")

    def _extract_filters_from_antlr(self, listener: Enhanced_SAP_HANA_Listener, procedure_id: str) -> List[FilterCondition]:
        """Extract filters from ANTLR parse results"""
        filters = []

        # Process filter conditions from ANTLR
        for condition_text in listener.filter_conditions:
            # Use regex to parse the condition since ANTLR gives us the full text
            filter_matches = re.finditer(
                r'(\w+)\.(\w+)\s*(=|!=|<>|<|>|<=|>=|IN|LIKE|BETWEEN)\s*(.+?)(?:\s+AND|\s+OR|$)',
                condition_text,
                re.IGNORECASE
            )

            for match in filter_matches:
                table = match.group(1).upper()
                column = match.group(2).upper()
                operator = match.group(3).upper()
                value_part = match.group(4).strip()

                # Extract values
                values = self._extract_filter_values(value_part, operator)
                is_parameter = ':' in value_part

                filter_cond = FilterCondition(
                    table=table,
                    column=column,
                    operator=operator,
                    values=values,
                    condition_text=f"{table}.{column} {operator} {value_part}",
                    is_parameter=is_parameter,
                    procedure_id=procedure_id
                )
                filters.append(filter_cond)

        return filters

    def _extract_joins_from_antlr(self, listener: Enhanced_SAP_HANA_Listener, procedure_id: str) -> List[JoinRelationship]:
        """Extract joins from ANTLR parse results"""
        joins = []

        # Process join conditions from ANTLR
        for join_text in listener.join_conditions:
            # Use regex to parse join conditions
            join_matches = re.finditer(
                r'(INNER|LEFT|RIGHT|FULL|CROSS)?\s*JOIN\s+(\w+)(?:\s+AS\s+(\w+))?\s+ON\s+(.+?)(?:\s+(?:INNER|LEFT|RIGHT|FULL|CROSS|WHERE|GROUP|ORDER|$))',
                join_text,
                re.IGNORECASE
            )

            for match in join_matches:
                join_type = (match.group(1) or 'INNER').upper()
                right_table = match.group(2).upper()
                right_alias = match.group(3)
                condition = match.group(4).strip()

                # Extract left table from condition
                left_table = self._extract_left_table_from_condition(condition)

                if left_table:
                    join_rel = JoinRelationship(
                        left_table=left_table,
                        right_table=right_table,
                        join_type=join_type,
                        condition=condition,
                        left_columns=self._extract_columns_from_condition(condition, left_table),
                        right_columns=self._extract_columns_from_condition(condition, right_table),
                        procedure_id=procedure_id
                    )
                    joins.append(join_rel)

        return joins

    def _extract_parameters_from_antlr(self, listener: Enhanced_SAP_HANA_Listener) -> List[Parameter]:
        """Extract parameters from ANTLR parse results"""
        parameters = []
        unique_params = list(set(listener.parameters))  # Remove duplicates

        for param_name in unique_params:
            # Create Parameter object with basic info
            param = Parameter(
                name=param_name,
                data_type='UNKNOWN',  # ANTLR listener doesn't capture type info yet
                direction='IN'
            )
            parameters.append(param)

        return parameters

    def analyze_cross_procedure_patterns(self, procedures: List[ProcedureAnalysis]) -> Dict[str, Any]:
        """Analyze patterns across multiple procedures for migration insights"""

        # Consolidate tables across procedures (one row per table)
        table_consolidation = self._consolidate_tables_across_procedures(procedures)

        # Consolidate filters across procedures
        filter_analysis = self._analyze_filter_patterns(procedures)

        # Analyze join patterns
        join_analysis = self._analyze_join_patterns(procedures)

        # Create data lineage graph
        lineage_graph = self._create_data_lineage(procedures)

        # Identify migration critical points
        critical_points = self._identify_critical_migration_points(procedures)

        return {
            'table_consolidation': table_consolidation,
            'filter_analysis': filter_analysis,
            'join_analysis': join_analysis,
            'data_lineage': lineage_graph,
            'critical_points': critical_points,
            'summary': {
                'total_procedures': len(procedures),
                'unique_tables': len(set().union(*[p.tables.keys() for p in procedures])),
                'total_joins': sum(len(p.joins) for p in procedures),
                'total_filters': sum(len(p.filters) for p in procedures)
            }
        }

    def _consolidate_tables_across_procedures(self, procedures: List[ProcedureAnalysis]) -> Dict[str, Any]:
        """Consolidate table usage across ALL procedures - one row per table"""

        table_consolidation = {}

        # Get all unique tables
        all_tables = set()
        for proc in procedures:
            all_tables.update(proc.tables.keys())

        # For each table, consolidate information from all procedures
        for table_name in all_tables:
            # Find all procedures that use this table
            using_procedures = []
            all_columns = set()
            all_usage_contexts = set()
            all_filters = []
            all_joins = []

            for proc in procedures:
                if table_name in proc.tables:
                    using_procedures.append(proc.procedure_id)
                    table_ref = proc.tables[table_name]
                    all_columns.update(table_ref.columns)
                    all_usage_contexts.update(table_ref.usage_contexts)

                # Collect filters for this table
                table_filters = [f for f in proc.filters if f.table == table_name]
                all_filters.extend(table_filters)

                # Collect joins for this table
                table_joins = [j for j in proc.joins if j.left_table == table_name or j.right_table == table_name]
                all_joins.extend(table_joins)

            # Consolidate filter conditions
            consolidated_filters = self._consolidate_filter_conditions(all_filters)

            # Consolidate join conditions
            consolidated_joins = self._consolidate_join_conditions(all_joins, table_name)

            # Create consolidated entry
            table_consolidation[table_name] = {
                'table_name': table_name,
                'used_in_procedures': using_procedures,
                'procedure_count': len(using_procedures),
                'all_columns': sorted(list(all_columns)),
                'usage_contexts': sorted(list(all_usage_contexts)),
                'consolidated_filters': consolidated_filters,
                'consolidated_joins': consolidated_joins,
                'table_purpose': self.sap_table_patterns.get(table_name, 'Business data table'),
                'migration_priority': self._assess_migration_priority(len(using_procedures), len(all_filters), len(all_joins))
            }

        return table_consolidation

    def _consolidate_filter_conditions(self, filters: List[FilterCondition]) -> Dict[str, Any]:
        """Consolidate filter conditions for a table across procedures"""

        if not filters:
            return {'has_filters': False, 'patterns': []}

        # Group by column
        column_filters = defaultdict(list)
        for f in filters:
            column_filters[f.column].append(f)

        patterns = []
        for column, column_filter_list in column_filters.items():
            # Analyze pattern for this column
            procedures_with_filter = set(f.procedure_id for f in column_filter_list)
            all_values = []
            operators = set()

            for f in column_filter_list:
                all_values.extend(f.values)
                operators.add(f.operator)

            unique_values = set(all_values)

            pattern = {
                'column': column,
                'procedures_with_filter': list(procedures_with_filter),
                'filter_frequency': len(procedures_with_filter),
                'operators': list(operators),
                'unique_values': list(unique_values),
                'example_conditions': [f.condition_text for f in column_filter_list[:3]],  # First 3 examples
                'migration_note': self._generate_filter_migration_note(len(procedures_with_filter), unique_values)
            }
            patterns.append(pattern)

        return {
            'has_filters': True,
            'total_filter_patterns': len(patterns),
            'patterns': patterns
        }

    def _consolidate_join_conditions(self, joins: List[JoinRelationship], table_name: str) -> Dict[str, Any]:
        """Consolidate join conditions for a table across procedures"""

        if not joins:
            return {'has_joins': False, 'relationships': []}

        # Group by related table
        join_relationships = defaultdict(list)
        for j in joins:
            related_table = j.right_table if j.left_table == table_name else j.left_table
            join_relationships[related_table].append(j)

        relationships = []
        for related_table, join_list in join_relationships.items():
            # Analyze relationship pattern
            procedures_with_join = set(j.procedure_id for j in join_list)
            join_types = set(j.join_type for j in join_list)
            conditions = set(j.condition for j in join_list)

            relationship = {
                'related_table': related_table,
                'procedures_with_join': list(procedures_with_join),
                'join_frequency': len(procedures_with_join),
                'join_types': list(join_types),
                'unique_conditions': list(conditions),
                'example_condition': join_list[0].condition,  # First example
                'migration_note': self._generate_join_migration_note(len(procedures_with_join), len(conditions))
            }
            relationships.append(relationship)

        return {
            'has_joins': True,
            'total_relationships': len(relationships),
            'relationships': relationships
        }

    def _generate_filter_migration_note(self, procedure_count: int, unique_values: set) -> str:
        """Generate migration note for filter patterns"""

        if procedure_count == 1:
            return "SINGLE_USE - Consider if filter is needed in migration"
        elif len(unique_values) == 1:
            return "CONSISTENT - Same filter across procedures, safe to retain"
        elif len(unique_values) > 5:
            return "VARIABLE - Multiple filter values, review for optimization"
        else:
            return "MODERATE - Few variations, consolidate if possible"

    def _generate_join_migration_note(self, procedure_count: int, condition_count: int) -> str:
        """Generate migration note for join patterns"""

        if procedure_count == 1:
            return "SINGLE_USE - Verify if join is critical for migration"
        elif condition_count == 1:
            return "CONSISTENT - Same join logic, retain as-is"
        else:
            return "VARIABLE - Multiple join patterns, standardize for migration"

    def _assess_migration_priority(self, procedure_count: int, filter_count: int, join_count: int) -> str:
        """Assess migration priority for a table"""

        score = procedure_count * 2 + filter_count + join_count

        if score >= 10:
            return "CRITICAL"
        elif score >= 5:
            return "HIGH"
        elif score >= 2:
            return "MEDIUM"
        else:
            return "LOW"

    def _analyze_filter_patterns(self, procedures: List[ProcedureAnalysis]) -> Dict[str, Any]:
        """Analyze filter patterns across procedures to identify migration requirements"""

        # First, identify all table.column combinations used across procedures
        all_table_columns = set()
        for proc in procedures:
            for table_name, table_ref in proc.tables.items():
                for column in table_ref.columns:
                    all_table_columns.add(f"{table_name}.{column}")

        # Group filters by table.column
        column_filters = defaultdict(list)
        column_usage = defaultdict(set)  # Track which procedures use each column

        for proc in procedures:
            # Track column usage (with or without filters)
            for table_name, table_ref in proc.tables.items():
                for column in table_ref.columns:
                    key = f"{table_name}.{column}"
                    column_usage[key].add(proc.procedure_id)

            # Track filters
            for filter_cond in proc.filters:
                key = f"{filter_cond.table}.{filter_cond.column}"
                column_filters[key].append({
                    'procedure': proc.procedure_id,
                    'operator': filter_cond.operator,
                    'values': filter_cond.values,
                    'condition': filter_cond.condition_text,
                    'is_parameter': filter_cond.is_parameter
                })

        # Analyze patterns
        filter_patterns = {}
        migration_recommendations = []

        for column in all_table_columns:
            filters = column_filters.get(column, [])
            procedures_using_column = column_usage.get(column, set())
            procedures_with_filters = set(f['procedure'] for f in filters)
            procedures_without_filters = procedures_using_column - procedures_with_filters

            if not filters:
                continue  # Skip columns with no filters

            # Analyze value patterns
            all_values = []
            operators = set()
            has_parameters = False

            for f in filters:
                all_values.extend(f['values'])
                operators.add(f['operator'])
                if f['is_parameter']:
                    has_parameters = True

            unique_values = set(all_values)
            value_frequency = Counter(all_values)

            pattern_analysis = {
                'column': column,
                'procedures_using_column': list(procedures_using_column),
                'procedures_with_filters': list(procedures_with_filters),
                'procedures_without_filters': list(procedures_without_filters),
                'total_procedures_using': len(procedures_using_column),
                'filtered_procedures_count': len(procedures_with_filters),
                'unfiltered_procedures_count': len(procedures_without_filters),
                'operators_used': list(operators),
                'unique_values': list(unique_values),
                'value_frequency': dict(value_frequency),
                'has_parameters': has_parameters,
                'filters': filters
            }

            # Enhanced migration recommendation logic with detailed procedure analysis
            if procedures_without_filters:
                # Some procedures use the column without filters - they need ALL values
                filtered_proc_details = []
                for proc in procedures_with_filters:
                    proc_filters = [f for f in filters if f['procedure'] == proc]
                    if proc_filters:
                        proc_values = []
                        for pf in proc_filters:
                            proc_values.extend(pf['values'])
                        filtered_proc_details.append(f"{proc} (filters: {', '.join(set(proc_values))})")

                recommendation = f"Column {column}:\n" \
                               f"  - FILTERED in procedures: {', '.join(filtered_proc_details)}\n" \
                               f"  - NOT FILTERED in procedures: {', '.join(sorted(procedures_without_filters))} (requires ALL values)\n" \
                               f"  - RECOMMENDATION: Remove filter in migration - some procedures need all column values."
                migration_recommendations.append(recommendation)
                pattern_analysis['migration_decision'] = 'REMOVE_FILTER'

            elif len(unique_values) == 1:
                # All procedures use the same filter value
                proc_details = [f"{proc} (filter: {list(unique_values)[0]})" for proc in procedures_with_filters]
                recommendation = f"Column {column}:\n" \
                               f"  - CONSISTENTLY FILTERED in procedures: {', '.join(proc_details)}\n" \
                               f"  - NOT USED in other procedures\n" \
                               f"  - RECOMMENDATION: Retain filter '{list(unique_values)[0]}' in migration."
                migration_recommendations.append(recommendation)
                pattern_analysis['migration_decision'] = 'RETAIN_FILTER'

            else:
                # Multiple filter values across procedures
                proc_details = []
                for proc in procedures_with_filters:
                    proc_filters = [f for f in filters if f['procedure'] == proc]
                    if proc_filters:
                        proc_values = []
                        for pf in proc_filters:
                            proc_values.extend(pf['values'])
                        proc_details.append(f"{proc} (filters: {', '.join(set(proc_values))})")

                recommendation = f"Column {column}:\n" \
                               f"  - DIFFERENT FILTERS in procedures: {', '.join(proc_details)}\n" \
                               f"  - NOT USED in other procedures\n" \
                               f"  - RECOMMENDATION: Use union of all values ({', '.join(sorted(unique_values))}) or consolidate filter logic."
                migration_recommendations.append(recommendation)
                pattern_analysis['migration_decision'] = 'CONSOLIDATE_FILTER'

            filter_patterns[column] = pattern_analysis

        return {
            'patterns': filter_patterns,
            'recommendations': migration_recommendations,
            'summary': {
                'total_filtered_columns': len(filter_patterns),
                'columns_needing_all_values': len([p for p in filter_patterns.values() if p['migration_decision'] == 'REMOVE_FILTER']),
                'columns_with_consistent_filters': len([p for p in filter_patterns.values() if p['migration_decision'] == 'RETAIN_FILTER'])
            }
        }

    def _analyze_join_patterns(self, procedures: List[ProcedureAnalysis]) -> Dict[str, Any]:
        """Analyze join patterns for migration complexity assessment"""

        # Collect all joins
        all_joins = []
        for proc in procedures:
            all_joins.extend(proc.joins)

        # Group joins by table pairs
        join_patterns = defaultdict(list)

        for join in all_joins:
            # Create a consistent key for table pairs
            tables = sorted([join.left_table, join.right_table])
            key = f"{tables[0]}-{tables[1]}"

            join_patterns[key].append({
                'procedure': join.procedure_id,
                'join_type': join.join_type,
                'condition': join.condition,
                'left_table': join.left_table,
                'right_table': join.right_table,
                'left_columns': join.left_columns,
                'right_columns': join.right_columns
            })

        # Analyze patterns
        pattern_analysis = {}
        migration_complexity = []

        for table_pair, joins in join_patterns.items():
            # Analyze join consistency
            join_types = set(j['join_type'] for j in joins)
            conditions = set(j['condition'] for j in joins)
            proc_count = len(set(j['procedure'] for j in joins))

            analysis = {
                'table_pair': table_pair,
                'used_in_procedures': proc_count,
                'join_types': list(join_types),
                'unique_conditions': len(conditions),
                'conditions': list(conditions),
                'joins': joins
            }

            # Complexity assessment
            if len(join_types) > 1:
                migration_complexity.append(f"Table pair {table_pair} uses different join types: {join_types}")

            if len(conditions) > 1:
                migration_complexity.append(f"Table pair {table_pair} has {len(conditions)} different join conditions")

            pattern_analysis[table_pair] = analysis

        return {
            'patterns': pattern_analysis,
            'complexity_issues': migration_complexity,
            'summary': {
                'total_join_patterns': len(join_patterns),
                'avg_procedures_per_join': sum(p['used_in_procedures'] for p in pattern_analysis.values()) / len(pattern_analysis) if pattern_analysis else 0
            }
        }

    def _create_data_lineage(self, procedures: List[ProcedureAnalysis]) -> Dict[str, Any]:
        """Create data lineage graph for migration planning"""

        # Create directed graph
        G = nx.DiGraph()

        # Add nodes (tables)
        all_tables = set()
        for proc in procedures:
            all_tables.update(proc.tables.keys())

        for table in all_tables:
            G.add_node(table,
                      table_type=self.sap_table_patterns.get(table, 'Business Table'),
                      procedures=[]
                      )

        # Add edges (joins)
        for proc in procedures:
            # Add procedure to table nodes
            for table in proc.tables.keys():
                G.nodes[table]['procedures'].append(proc.procedure_id)

            # Add join relationships
            for join in proc.joins:
                if join.left_table in G.nodes and join.right_table in G.nodes:
                    if G.has_edge(join.left_table, join.right_table):
                        # Update existing edge
                        G.edges[join.left_table, join.right_table]['procedures'].append(proc.procedure_id)
                        G.edges[join.left_table, join.right_table]['join_types'].add(join.join_type)
                    else:
                        # Create new edge
                        G.add_edge(join.left_table, join.right_table,
                                 procedures=[proc.procedure_id],
                                 join_types={join.join_type},
                                 conditions=[join.condition])

        # Analyze graph properties
        centrality = nx.degree_centrality(G)
        components = list(nx.weakly_connected_components(G))

        return {
            'nodes': list(G.nodes(data=True)),
            'edges': list(G.edges(data=True)),
            'centrality': centrality,
            'components': [list(comp) for comp in components],
            'summary': {
                'total_tables': len(G.nodes),
                'total_relationships': len(G.edges),
                'connected_components': len(components),
                'most_connected_tables': sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:5]
            }
        }

    def _identify_critical_migration_points(self, procedures: List[ProcedureAnalysis]) -> List[Dict[str, Any]]:
        """Identify critical points for migration planning"""

        critical_points = []

        # High complexity procedures
        high_complexity = [p for p in procedures if p.complexity_score > 50]
        if high_complexity:
            critical_points.append({
                'type': 'High Complexity Procedures',
                'description': f'{len(high_complexity)} procedures have high complexity scores',
                'procedures': [p.procedure_id for p in high_complexity],
                'recommendation': 'Prioritize testing and validation for these procedures'
            })

        # Tables used across many procedures
        table_usage = defaultdict(int)
        for proc in procedures:
            for table in proc.tables.keys():
                table_usage[table] += 1

        highly_used_tables = [(table, count) for table, count in table_usage.items() if count > len(procedures) * 0.5]
        if highly_used_tables:
            critical_points.append({
                'type': 'Highly Used Tables',
                'description': f'Tables used in >50% of procedures',
                'tables': highly_used_tables,
                'recommendation': 'Ensure these tables are migrated first and thoroughly tested'
            })

        return critical_points
    
    def parse_procedure(self, sql_text: str, procedure_id: str = None) -> ProcedureAnalysis:
        """Parse a single SAP HANA procedure using enhanced parsing for LLM"""

        # Extract procedure ID if not provided
        if not procedure_id:
            procedure_id = self._extract_procedure_id(sql_text)

        # Use enhanced sqlparse for better LLM data quality
        # ANTLR has issues with PROCEDURE syntax, so prioritize enhanced sqlparse
        try:
            return self._parse_with_sqlparse(sql_text, procedure_id)
        except Exception as e:
            print(f"⚠️ Enhanced parsing failed for {procedure_id}, using basic fallback: {e}")
            # Fallback to basic parsing if enhanced fails
            return self._parse_with_basic_fallback(sql_text, procedure_id)

    def _parse_with_basic_fallback(self, sql_text: str, procedure_id: str) -> ProcedureAnalysis:
        """Basic fallback parsing"""

        # Clean and normalize SQL
        cleaned_sql = self._clean_sql(sql_text)

        # Extract components with basic methods
        tables = self._extract_tables(cleaned_sql)
        filters = self._extract_filters(cleaned_sql, procedure_id)
        joins = self._extract_joins(cleaned_sql, procedure_id)
        parameters = self._extract_parameters(cleaned_sql)

        # Calculate complexity
        complexity = self._calculate_complexity(tables, filters, joins)

        return ProcedureAnalysis(
            procedure_id=procedure_id,
            tables=tables,
            filters=filters,
            joins=joins,
            parameters=parameters,
            raw_sql=sql_text,
            complexity_score=complexity
        )

    def _parse_with_antlr(self, sql_text: str, procedure_id: str) -> ProcedureAnalysis:
        """Parse using ANTLR SAP HANA grammar with enhanced listener"""

        try:
            # Create ANTLR input stream
            input_stream = InputStream(sql_text)
            lexer = HanaLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = HanaParser(stream)

            # Parse the SQL - use correct grammar rule name
            tree = parser.compilation_unit()  # Fixed: use compilation_unit (with underscore)

            # Create enhanced listener for better extraction
            listener = Enhanced_SAP_HANA_Listener()
            listener.set_sql_text(sql_text)  # Provide original SQL for fallback

            walker = ParseTreeWalker()
            walker.walk(listener, tree)

            # Finalize parsing (resolve aliases, fallback if needed)
            listener.finalize_parsing()

            # Convert ANTLR results to our format with enhanced data
            tables = {}
            for table_name in listener.tables:
                columns = listener.columns.get(table_name, set())
                tables[table_name] = TableReference(
                    name=table_name,
                    columns=columns,
                    usage_contexts={'ANTLR_PARSED', 'SELECT', 'JOIN'}  # Enhanced contexts
                )

            # Extract filters and joins from ANTLR parse tree
            filters = self._extract_filters_from_antlr(listener, procedure_id)
            joins = self._extract_joins_from_antlr(listener, procedure_id)
            parameters = self._extract_parameters_from_antlr(listener)

            # If ANTLR didn't extract enough, supplement with enhanced regex
            if not filters or not joins or len(tables) == 0:
                print(f"⚠️ ANTLR extraction incomplete for {procedure_id}, supplementing with enhanced parsing")

                # Use enhanced sqlparse method as supplement
                enhanced_result = self._parse_with_sqlparse(sql_text, procedure_id)

                # Merge results (prefer ANTLR where available)
                if len(tables) == 0:
                    tables = enhanced_result.tables
                if not filters:
                    filters = enhanced_result.filters
                if not joins:
                    joins = enhanced_result.joins
                if not parameters:
                    parameters = enhanced_result.parameters

            # Calculate complexity
            complexity = self._calculate_complexity(tables, filters, joins)

            print(f"✅ Enhanced ANTLR parsed {procedure_id}: {len(tables)} tables, {len(filters)} filters, {len(joins)} joins")

            # Debug output for BSEG
            if 'BSEG' in tables:
                bseg_columns = tables['BSEG'].columns
                print(f"   BSEG columns found: {sorted(list(bseg_columns))}")

            return ProcedureAnalysis(
                procedure_id=procedure_id,
                tables=tables,
                filters=filters,
                joins=joins,
                parameters=parameters,
                raw_sql=sql_text,
                complexity_score=complexity
            )

        except Exception as e:
            print(f"⚠️ ANTLR parsing error for {procedure_id}: {e}")
            raise e  # Re-raise to trigger fallback

    def _parse_with_sqlparse(self, sql_text: str, procedure_id: str) -> ProcedureAnalysis:
        """Parse using enhanced sqlparse with proper filter value extraction"""

        # Use enhanced parsing for better LLM data
        tables = self._extract_tables_enhanced(sql_text)
        filters = self._extract_filters_enhanced_for_llm(sql_text, procedure_id)
        joins = self._extract_joins(sql_text, procedure_id)
        parameters = self._extract_parameters(sql_text)

        # Convert to TableReference format
        table_refs = {}
        for table_name in tables:
            columns = self._extract_columns_for_table(sql_text, table_name)
            table_refs[table_name] = TableReference(
                name=table_name,
                columns=columns,
                usage_contexts={'SELECT', 'JOIN', 'FILTER'}
            )

        # Calculate complexity
        complexity = self._calculate_complexity(table_refs, filters, joins)

        return ProcedureAnalysis(
            procedure_id=procedure_id,
            tables=table_refs,
            filters=filters,
            joins=joins,
            parameters=parameters,
            raw_sql=sql_text,
            complexity_score=complexity
        )

    def _extract_tables_enhanced(self, sql_text: str) -> Set[str]:
        """Extract table names with enhanced accuracy - handle both uppercase and lowercase"""
        tables = set()

        # Pattern for FROM and JOIN clauses - handle case insensitive
        table_patterns = [
            r'FROM\s+([a-zA-Z][a-zA-Z0-9_]{2,7})(?:\s+(?:AS\s+)?(\w+))?',
            r'JOIN\s+([a-zA-Z][a-zA-Z0-9_]{2,7})(?:\s+(?:AS\s+)?(\w+))?',
            r'INNER\s+JOIN\s+([a-zA-Z][a-zA-Z0-9_]{2,7})(?:\s+(?:AS\s+)?(\w+))?',
            r'LEFT\s+JOIN\s+([a-zA-Z][a-zA-Z0-9_]{2,7})(?:\s+(?:AS\s+)?(\w+))?',
            r'RIGHT\s+JOIN\s+([a-zA-Z][a-zA-Z0-9_]{2,7})(?:\s+(?:AS\s+)?(\w+))?',
            r'UPDATE\s+([a-zA-Z][a-zA-Z0-9_]{2,7})',
            r'INSERT\s+INTO\s+([a-zA-Z][a-zA-Z0-9_]{2,7})'
        ]

        # Words to exclude (common SQL keywords)
        excluded_words = {
            'AND', 'OR', 'NOT', 'IN', 'ON', 'AS', 'IS', 'NULL', 'TRUE', 'FALSE',
            'DATE', 'TIME', 'YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'SECOND',
            'PAYMENT', 'AMOUNT', 'TOTAL', 'COUNT', 'SUM', 'AVG', 'MAX', 'MIN',
            'CASE', 'WHEN', 'THEN', 'ELSE', 'END', 'LIKE', 'BETWEEN', 'EXISTS',
            'SELECT', 'FROM', 'WHERE', 'GROUP', 'ORDER', 'HAVING', 'UNION',
            'CREATE', 'ALTER', 'DROP', 'INSERT', 'UPDATE', 'DELETE', 'CURRENT',
            'CURRENT_DATE', 'CURRENT_TIME', 'CURRENT_TIMESTAMP'
        }

        for pattern in table_patterns:
            matches = re.finditer(pattern, sql_text, re.IGNORECASE)
            for match in matches:
                table_name = match.group(1).upper()

                # Enhanced filtering for SAP tables
                if (len(table_name) >= 3 and
                    len(table_name) <= 8 and  # SAP tables are typically 3-8 chars
                    table_name.isalnum() and
                    not table_name.isdigit() and
                    table_name not in excluded_words and
                    # Must start with letters (SAP convention)
                    table_name[0].isalpha() and
                    # Known SAP tables or reasonable patterns
                    (table_name in self.sap_table_patterns or
                     table_name in ['BKPF', 'BSEG', 'LFA1', 'KNA1', 'MARA', 'MAKT', 'MARD'] or
                     re.match(r'^[A-Z]{3,5}[0-9]*[A-Z]*$', table_name))):
                    tables.add(table_name)

        return tables

    def _extract_filters_enhanced_for_llm(self, sql_text: str, procedure_id: str) -> List[FilterCondition]:
        """Extract filters with proper value preservation for LLM including aliased tables"""
        filters = []

        # Build alias mapping for all tables
        alias_to_table = self._build_alias_mapping(sql_text)

        # Multiple patterns to catch different filter formats
        patterns = [
            # Pattern for IN clauses with parentheses
            r'(\w+)\.(\w+)\s+(IN)\s*\([^)]+\)',
            # Pattern for other operators including IS NULL/IS NOT NULL
            r'(\w+)\.(\w+)\s+(IS\s+NOT\s+NULL|IS\s+NULL)',
            r'(\w+)\.(\w+)\s*(=|!=|<>|<|>|<=|>=|LIKE|BETWEEN)\s*([^A-Z\n]+?)(?=\s+AND\s+|\s+OR\s+|;|\)|$)',
        ]

        for pattern in patterns:
            matches = re.finditer(pattern, sql_text, re.IGNORECASE)

            for match in matches:
                table_or_alias = match.group(1).upper()
                column = match.group(2).upper()
                operator = match.group(3).upper()

                # Resolve alias to actual table name
                actual_table = alias_to_table.get(table_or_alias, table_or_alias)

                if operator == 'IN':
                    # For IN clauses, get the full match including parentheses
                    value_part = match.group(0).split(operator, 1)[1].strip()
                    values = self._extract_values_for_llm(value_part, operator)
                elif 'NULL' in operator:
                    # For IS NULL/IS NOT NULL
                    value_part = operator
                    values = [operator]
                else:
                    value_part = match.group(4).strip() if len(match.groups()) >= 4 else ""
                    values = self._extract_values_for_llm(value_part, operator)

                filter_cond = FilterCondition(
                    table=actual_table,
                    column=column,
                    operator=operator,
                    values=values,
                    condition_text=f"{table_or_alias}.{column} {operator} {value_part}",
                    is_parameter=':' in value_part,
                    procedure_id=procedure_id
                )
                filters.append(filter_cond)

        return filters

    def _build_alias_mapping(self, sql_text: str) -> Dict[str, str]:
        """Build mapping from alias to actual table name - handle case insensitive"""
        alias_to_table = {}

        # Pattern for table aliases in FROM and JOIN clauses - case insensitive
        alias_patterns = [
            r'FROM\s+([a-zA-Z][a-zA-Z0-9_]{2,7})\s+(?:AS\s+)?(\w+)',
            r'JOIN\s+([a-zA-Z][a-zA-Z0-9_]{2,7})\s+(?:AS\s+)?(\w+)',
            r'INNER\s+JOIN\s+([a-zA-Z][a-zA-Z0-9_]{2,7})\s+(?:AS\s+)?(\w+)',
            r'LEFT\s+JOIN\s+([a-zA-Z][a-zA-Z0-9_]{2,7})\s+(?:AS\s+)?(\w+)',
            r'RIGHT\s+JOIN\s+([a-zA-Z][a-zA-Z0-9_]{2,7})\s+(?:AS\s+)?(\w+)'
        ]

        for pattern in alias_patterns:
            matches = re.finditer(pattern, sql_text, re.IGNORECASE)
            for match in matches:
                table_name = match.group(1).upper()
                alias = match.group(2).upper()

                # Only map if alias is different from table name and not a SQL keyword
                if (alias != table_name and
                    len(alias) <= 3 and  # Aliases are typically short
                    alias not in {'ON', 'WHERE', 'AND', 'OR', 'AS', 'INNER', 'LEFT', 'RIGHT', 'JOIN', 'SET'}):
                    alias_to_table[alias] = table_name

        return alias_to_table

    def _extract_values_for_llm(self, value_part: str, operator: str) -> List[str]:
        """Extract filter values properly for LLM - handles 'OR', 'TA', 'ZOR' correctly"""
        values = []

        if operator == 'IN':
            # Find all quoted strings in the value part
            quoted_pattern = r"'([^']*)'"
            quoted_matches = re.findall(quoted_pattern, value_part)
            values.extend(quoted_matches)

            # If no quoted strings found, try parentheses content
            if not values:
                paren_pattern = r'\((.*?)\)'
                paren_match = re.search(paren_pattern, value_part)
                if paren_match:
                    content = paren_match.group(1)
                    # Split by comma and clean
                    raw_values = [v.strip().strip("'\"") for v in content.split(',')]
                    values.extend([v for v in raw_values if v])

        elif operator == 'BETWEEN':
            # Extract BETWEEN values
            between_pattern = r'(.+?)\s+AND\s+(.+)'
            match = re.search(between_pattern, value_part, re.IGNORECASE)
            if match:
                val1 = match.group(1).strip().strip("'\"")
                val2 = match.group(2).strip().strip("'\"")
                values = [val1, val2]

        else:
            # Single value
            clean_value = value_part.strip().strip("'\"")
            if clean_value:
                values = [clean_value]

        return values

    def _extract_columns_for_table(self, sql_text: str, table_name: str) -> Set[str]:
        """Extract columns used for a specific table including aliases - ENHANCED VERSION"""
        columns = set()

        # Method 1: Build alias mapping and find table.column patterns
        alias_to_table = self._build_alias_mapping(sql_text)

        # Find all table.column patterns in the SQL
        column_pattern = r'(\w+)\.(\w+)'
        matches = re.findall(column_pattern, sql_text, re.IGNORECASE)

        # Find columns for this specific table
        for table_or_alias, column in matches:
            table_or_alias_upper = table_or_alias.upper()
            column_upper = column.upper()

            # Check if this is the table we want (direct match)
            if table_or_alias_upper == table_name:
                columns.add(column_upper)
            # Check if this is an alias for the table we want
            elif table_or_alias_upper in alias_to_table and alias_to_table[table_or_alias_upper] == table_name:
                columns.add(column_upper)

        # Method 2: Extract columns from SELECT statements (for INSERT...SELECT patterns)
        select_columns = self._extract_select_columns_for_table(sql_text, table_name)
        columns.update(select_columns)

        return columns

    def _extract_select_columns_for_table(self, sql_text: str, table_name: str) -> Set[str]:
        """Extract columns from SELECT statements for a specific table"""
        columns = set()

        # Pattern for SELECT columns in INSERT...SELECT or simple SELECT statements
        select_pattern = r'SELECT\s+(.*?)\s+FROM\s+' + re.escape(table_name)
        matches = re.finditer(select_pattern, sql_text, re.IGNORECASE | re.DOTALL)

        for match in matches:
            columns_text = match.group(1)

            # Extract individual columns
            column_list = [col.strip() for col in columns_text.split(',')]

            for column in column_list:
                # Remove aliases (AS keyword)
                column = re.sub(r'\s+as\s+\w+', '', column, flags=re.IGNORECASE)
                column = column.strip()

                # Skip complex expressions, keep simple column names
                if (column and
                    not any(char in column for char in ['(', ')', '+', '-', '*', '/', '\'', '"']) and
                    column.upper() not in ['CURRENT_TIMESTAMP', 'CURRENT_DATE'] and
                    not column.isdigit()):

                    column_upper = column.upper()
                    if len(column_upper) >= 2 and column_upper.replace('_', '').isalnum():
                        columns.add(column_upper)

        return columns

    def _find_table_aliases(self, sql_text: str, table_name: str) -> Set[str]:
        """Find aliases for a given table"""
        aliases = set()

        # Pattern for table aliases: FROM/JOIN table_name AS alias or FROM/JOIN table_name alias
        alias_patterns = [
            rf'{table_name}\s+AS\s+(\w+)',
            rf'{table_name}\s+(\w+)(?=\s+(?:ON|WHERE|INNER|LEFT|RIGHT|GROUP|ORDER|$))',
            rf'FROM\s+{table_name}\s+(\w+)',
            rf'JOIN\s+{table_name}\s+(\w+)'
        ]

        for pattern in alias_patterns:
            matches = re.finditer(pattern, sql_text, re.IGNORECASE)
            for match in matches:
                alias = match.group(1).upper()
                # Exclude SQL keywords
                if alias not in {'ON', 'WHERE', 'AND', 'OR', 'AS', 'INNER', 'LEFT', 'RIGHT', 'JOIN'}:
                    aliases.add(alias)

        return aliases
    
    def _extract_procedure_id(self, sql_text: str) -> str:
        """Extract procedure ID from SQL text"""
        # Pattern for SAP HANA procedure names
        patterns = [
            r'PROCEDURE\s+"[^"]*"\.?"([^"]+)"',
            r'PROCEDURE\s+([A-Z_][A-Z0-9_]*)',
            r'::([A-Z_][A-Z0-9_]*)"'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, sql_text, re.IGNORECASE)
            if match:
                return match.group(1)
        
        return "UNKNOWN_PROCEDURE"
    
    def _clean_sql(self, sql_text: str) -> str:
        """Clean and normalize SQL text - preserve filter values for analysis"""
        # Remove comments
        sql_text = re.sub(r'/\*.*?\*/', '', sql_text, flags=re.DOTALL)
        sql_text = re.sub(r'--.*?\n', '\n', sql_text)

        # Keep string literals for filter analysis - they contain the actual values
        # Don't replace with 'STRING' as we need actual values like 'OR', 'TA', 'ZOR'

        # Normalize whitespace
        sql_text = re.sub(r'\s+', ' ', sql_text)

        return sql_text
    
    def _extract_tables(self, sql_text: str) -> Dict[str, TableReference]:
        """Extract all table references with detailed analysis"""
        tables = {}
        
        # Pattern for table references in different contexts
        patterns = [
            # FROM clause
            (r'\bFROM\s+(?:"[^"]+"\.)?"?([A-Z][A-Z0-9_]+)"?(?:\s+(?:AS\s+)?([A-Z][A-Z0-9_]+))?', 'FROM'),
            # JOIN clause
            (r'\b(?:INNER|LEFT|RIGHT|FULL|CROSS)?\s*JOIN\s+(?:"[^"]+"\.)?"?([A-Z][A-Z0-9_]+)"?(?:\s+(?:AS\s+)?([A-Z][A-Z0-9_]+))?', 'JOIN'),
            # INSERT INTO
            (r'\bINSERT\s+INTO\s+(?:"[^"]+"\.)?"?([A-Z][A-Z0-9_]+)"?', 'INSERT'),
            # UPDATE
            (r'\bUPDATE\s+(?:"[^"]+"\.)?"?([A-Z][A-Z0-9_]+)"?', 'UPDATE'),
        ]
        
        for pattern, context in patterns:
            matches = re.findall(pattern, sql_text, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    table_name = match[0]
                    alias = match[1] if len(match) > 1 and match[1] else None
                else:
                    table_name = match
                    alias = None
                
                if table_name and len(table_name) >= 3:
                    if table_name not in tables:
                        tables[table_name] = TableReference(
                            name=table_name,
                            alias=alias
                        )
                    tables[table_name].usage_contexts.add(context)
        
        # Extract columns for each table
        for table_name, table_ref in tables.items():
            table_ref.columns = self._extract_columns_for_table(sql_text, table_name, table_ref.alias)
        
        return tables
    

    
    def _extract_filters(self, sql_text: str, procedure_id: str) -> List[FilterCondition]:
        """Extract filter conditions with detailed analysis"""
        filters = []
        
        # Find WHERE clauses
        where_pattern = r'\bWHERE\b(.*?)(?:\bGROUP\s+BY\b|\bORDER\s+BY\b|\bHAVING\b|\bUNION\b|\bINTERSECT\b|\bEXCEPT\b|\;|$)'
        where_matches = re.findall(where_pattern, sql_text, re.IGNORECASE | re.DOTALL)
        
        for where_clause in where_matches:
            # Extract individual conditions
            conditions = self._parse_where_conditions(where_clause, procedure_id)
            filters.extend(conditions)
        
        # Find HAVING clauses
        having_pattern = r'\bHAVING\b(.*?)(?:\bORDER\s+BY\b|\bUNION\b|\bINTERSECT\b|\bEXCEPT\b|\;|$)'
        having_matches = re.findall(having_pattern, sql_text, re.IGNORECASE | re.DOTALL)
        
        for having_clause in having_matches:
            conditions = self._parse_where_conditions(having_clause, procedure_id)
            filters.extend(conditions)
        
        return filters
    
    def _parse_where_conditions(self, where_clause: str, procedure_id: str) -> List[FilterCondition]:
        """Parse individual WHERE conditions"""
        conditions = []
        
        # Split by AND/OR but preserve the conditions
        condition_parts = re.split(r'\b(?:AND|OR)\b', where_clause, flags=re.IGNORECASE)
        
        for part in condition_parts:
            part = part.strip()
            if not part:
                continue
            
            # Pattern for table.column operator value
            condition_pattern = r'([A-Z][A-Z0-9_]*\.[A-Z][A-Z0-9_]*)\s*([<>=!]+|IN|LIKE|BETWEEN)\s*(.+?)(?:\s+AND\s+|\s+OR\s+|$)'
            match = re.search(condition_pattern, part, re.IGNORECASE)
            
            if match:
                table_column = match.group(1)
                operator = match.group(2)
                value_part = match.group(3).strip()
                
                # Split table.column
                if '.' in table_column:
                    table, column = table_column.split('.', 1)
                    
                    # Extract values
                    values = self._extract_filter_values(value_part, operator)
                    
                    # Check if it's a parameter
                    is_parameter = ':' in value_part or value_part.startswith('?')
                    
                    condition = FilterCondition(
                        table=table.upper(),
                        column=column.upper(),
                        operator=operator.upper(),
                        values=values,
                        condition_text=part.strip(),
                        procedure_id=procedure_id,
                        is_parameter=is_parameter
                    )
                    conditions.append(condition)
        
        return conditions
    
    def _extract_filter_values(self, value_part: str, operator: str) -> List[str]:
        """Extract filter values from condition - preserve actual values like 'OR', 'TA', 'ZOR'"""
        values = []

        if operator.upper() == 'IN':
            # Extract values from IN clause - handle both ('OR', 'TA', 'ZOR') and incomplete patterns
            # Look for parentheses content
            in_pattern = r'\((.*?)\)'
            match = re.search(in_pattern, value_part)
            if match:
                values_str = match.group(1)
                # Split by comma and extract quoted values
                raw_values = [v.strip() for v in values_str.split(',')]
                for v in raw_values:
                    # Remove quotes but keep the actual value
                    clean_value = v.strip("'\"").strip()
                    if clean_value:  # Only add non-empty values
                        values.append(clean_value)
            else:
                # Handle incomplete IN clause - try to extract from the full value_part
                # Look for quoted strings in the value_part
                quoted_values = re.findall(r"'([^']*)'", value_part)
                values.extend(quoted_values)

        elif operator.upper() == 'BETWEEN':
            # Extract BETWEEN values
            between_pattern = r'(.+?)\s+AND\s+(.+)'
            match = re.search(between_pattern, value_part, re.IGNORECASE)
            if match:
                val1 = match.group(1).strip().strip("'\"").strip()
                val2 = match.group(2).strip().strip("'\"").strip()
                values = [val1, val2]
        else:
            # Single value - preserve actual value
            clean_value = value_part.strip().strip("'\"").strip()
            if clean_value:
                values = [clean_value]

        return values
    
    def _extract_joins(self, sql_text: str, procedure_id: str) -> List[JoinRelationship]:
        """Extract join relationships with detailed analysis"""
        joins = []
        
        # Pattern for JOIN clauses
        join_pattern = r'\b((?:INNER|LEFT|RIGHT|FULL|CROSS)?\s*JOIN)\s+(?:"[^"]+"\.)?"?([A-Z][A-Z0-9_]+)"?(?:\s+(?:AS\s+)?([A-Z][A-Z0-9_]+))?\s+ON\s+(.*?)(?=\s+(?:INNER|LEFT|RIGHT|FULL|CROSS)?\s*JOIN|\bWHERE\b|\bGROUP\s+BY\b|\bORDER\s+BY\b|\bHAVING\b|\;|$)'
        
        matches = re.findall(join_pattern, sql_text, re.IGNORECASE | re.DOTALL)
        
        for match in matches:
            join_type = match[0].strip()
            right_table = match[1]
            right_alias = match[2] if match[2] else None
            condition = match[3].strip()
            
            # Parse join condition to extract left table
            left_table = self._extract_left_table_from_join(condition)
            
            # Extract columns involved in join
            left_columns, right_columns = self._extract_join_columns(condition)
            
            join_rel = JoinRelationship(
                left_table=left_table,
                right_table=right_table,
                join_type=join_type,
                condition=condition,
                procedure_id=procedure_id,
                left_columns=left_columns,
                right_columns=right_columns
            )
            joins.append(join_rel)
        
        return joins
    
    def _extract_left_table_from_join(self, condition: str) -> str:
        """Extract left table from join condition"""
        # Look for table.column pattern on the left side of =
        pattern = r'([A-Z][A-Z0-9_]*)\.[A-Z][A-Z0-9_]*\s*='
        match = re.search(pattern, condition, re.IGNORECASE)
        return match.group(1).upper() if match else "UNKNOWN"
    
    def _extract_join_columns(self, condition: str) -> Tuple[List[str], List[str]]:
        """Extract columns involved in join condition"""
        left_columns = []
        right_columns = []
        
        # Pattern for table.column = table.column
        pattern = r'([A-Z][A-Z0-9_]*\.[A-Z][A-Z0-9_]*)\s*=\s*([A-Z][A-Z0-9_]*\.[A-Z][A-Z0-9_]*)'
        matches = re.findall(pattern, condition, re.IGNORECASE)
        
        for match in matches:
            left_col = match[0].split('.')[1] if '.' in match[0] else match[0]
            right_col = match[1].split('.')[1] if '.' in match[1] else match[1]
            left_columns.append(left_col.upper())
            right_columns.append(right_col.upper())
        
        return left_columns, right_columns
    
    def _extract_parameters(self, sql_text: str) -> List[Parameter]:
        """Extract procedure parameters"""
        parameters = []

        # Pattern for procedure parameters
        param_pattern = r'\bIN\s+([A-Z_][A-Z0-9_]*)\s+([A-Z]+(?:\([^)]+\))?)'
        matches = re.findall(param_pattern, sql_text, re.IGNORECASE)

        for match in matches:
            param = Parameter(
                name=match[0],
                data_type=match[1],
                direction='IN'
            )
            parameters.append(param)

        return parameters
    
    def _calculate_complexity(self, tables: Dict[str, TableReference], 
                            filters: List[FilterCondition], 
                            joins: List[JoinRelationship]) -> int:
        """Calculate procedure complexity score"""
        score = 0
        score += len(tables) * 2  # Tables
        score += len(filters) * 3  # Filters
        score += len(joins) * 5   # Joins
        
        # Bonus for complex joins
        for join in joins:
            if 'AND' in join.condition:
                score += 2
        
        return score
