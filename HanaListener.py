# Generated from C:/Users/harip/Desktop/SQL-vs/antlr-saphana/Hana.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .HanaParser import HanaParser
else:
    from HanaParser import HanaParser

# This class defines a complete listener for a parse tree produced by HanaParser.
class HanaListener(ParseTreeListener):

    # Enter a parse tree produced by HanaParser#swallow_to_semi.
    def enterSwallow_to_semi(self, ctx:HanaParser.Swallow_to_semiContext):
        pass

    # Exit a parse tree produced by HanaParser#swallow_to_semi.
    def exitSwallow_to_semi(self, ctx:HanaParser.Swallow_to_semiContext):
        pass


    # Enter a parse tree produced by HanaParser#compilation_unit.
    def enterCompilation_unit(self, ctx:HanaParser.Compilation_unitContext):
        pass

    # Exit a parse tree produced by HanaParser#compilation_unit.
    def exitCompilation_unit(self, ctx:HanaParser.Compilation_unitContext):
        pass


    # Enter a parse tree produced by HanaParser#sql_script.
    def enterSql_script(self, ctx:HanaParser.Sql_scriptContext):
        pass

    # Exit a parse tree produced by HanaParser#sql_script.
    def exitSql_script(self, ctx:HanaParser.Sql_scriptContext):
        pass


    # Enter a parse tree produced by HanaParser#unit_statement.
    def enterUnit_statement(self, ctx:HanaParser.Unit_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#unit_statement.
    def exitUnit_statement(self, ctx:HanaParser.Unit_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#set_schema.
    def enterSet_schema(self, ctx:HanaParser.Set_schemaContext):
        pass

    # Exit a parse tree produced by HanaParser#set_schema.
    def exitSet_schema(self, ctx:HanaParser.Set_schemaContext):
        pass


    # Enter a parse tree produced by HanaParser#drop_procedure.
    def enterDrop_procedure(self, ctx:HanaParser.Drop_procedureContext):
        pass

    # Exit a parse tree produced by HanaParser#drop_procedure.
    def exitDrop_procedure(self, ctx:HanaParser.Drop_procedureContext):
        pass


    # Enter a parse tree produced by HanaParser#create_procedure_body.
    def enterCreate_procedure_body(self, ctx:HanaParser.Create_procedure_bodyContext):
        pass

    # Exit a parse tree produced by HanaParser#create_procedure_body.
    def exitCreate_procedure_body(self, ctx:HanaParser.Create_procedure_bodyContext):
        pass


    # Enter a parse tree produced by HanaParser#param_name.
    def enterParam_name(self, ctx:HanaParser.Param_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#param_name.
    def exitParam_name(self, ctx:HanaParser.Param_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#param_type.
    def enterParam_type(self, ctx:HanaParser.Param_typeContext):
        pass

    # Exit a parse tree produced by HanaParser#param_type.
    def exitParam_type(self, ctx:HanaParser.Param_typeContext):
        pass


    # Enter a parse tree produced by HanaParser#sql_type.
    def enterSql_type(self, ctx:HanaParser.Sql_typeContext):
        pass

    # Exit a parse tree produced by HanaParser#sql_type.
    def exitSql_type(self, ctx:HanaParser.Sql_typeContext):
        pass


    # Enter a parse tree produced by HanaParser#table_type.
    def enterTable_type(self, ctx:HanaParser.Table_typeContext):
        pass

    # Exit a parse tree produced by HanaParser#table_type.
    def exitTable_type(self, ctx:HanaParser.Table_typeContext):
        pass


    # Enter a parse tree produced by HanaParser#table_type_definition.
    def enterTable_type_definition(self, ctx:HanaParser.Table_type_definitionContext):
        pass

    # Exit a parse tree produced by HanaParser#table_type_definition.
    def exitTable_type_definition(self, ctx:HanaParser.Table_type_definitionContext):
        pass


    # Enter a parse tree produced by HanaParser#column_list_definition.
    def enterColumn_list_definition(self, ctx:HanaParser.Column_list_definitionContext):
        pass

    # Exit a parse tree produced by HanaParser#column_list_definition.
    def exitColumn_list_definition(self, ctx:HanaParser.Column_list_definitionContext):
        pass


    # Enter a parse tree produced by HanaParser#column_elem.
    def enterColumn_elem(self, ctx:HanaParser.Column_elemContext):
        pass

    # Exit a parse tree produced by HanaParser#column_elem.
    def exitColumn_elem(self, ctx:HanaParser.Column_elemContext):
        pass


    # Enter a parse tree produced by HanaParser#column_name.
    def enterColumn_name(self, ctx:HanaParser.Column_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#column_name.
    def exitColumn_name(self, ctx:HanaParser.Column_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#data_type.
    def enterData_type(self, ctx:HanaParser.Data_typeContext):
        pass

    # Exit a parse tree produced by HanaParser#data_type.
    def exitData_type(self, ctx:HanaParser.Data_typeContext):
        pass


    # Enter a parse tree produced by HanaParser#parameter.
    def enterParameter(self, ctx:HanaParser.ParameterContext):
        pass

    # Exit a parse tree produced by HanaParser#parameter.
    def exitParameter(self, ctx:HanaParser.ParameterContext):
        pass


    # Enter a parse tree produced by HanaParser#parameter_clause.
    def enterParameter_clause(self, ctx:HanaParser.Parameter_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#parameter_clause.
    def exitParameter_clause(self, ctx:HanaParser.Parameter_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#lang.
    def enterLang(self, ctx:HanaParser.LangContext):
        pass

    # Exit a parse tree produced by HanaParser#lang.
    def exitLang(self, ctx:HanaParser.LangContext):
        pass


    # Enter a parse tree produced by HanaParser#security_mode.
    def enterSecurity_mode(self, ctx:HanaParser.Security_modeContext):
        pass

    # Exit a parse tree produced by HanaParser#security_mode.
    def exitSecurity_mode(self, ctx:HanaParser.Security_modeContext):
        pass


    # Enter a parse tree produced by HanaParser#default_schema_name.
    def enterDefault_schema_name(self, ctx:HanaParser.Default_schema_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#default_schema_name.
    def exitDefault_schema_name(self, ctx:HanaParser.Default_schema_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#view_name.
    def enterView_name(self, ctx:HanaParser.View_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#view_name.
    def exitView_name(self, ctx:HanaParser.View_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_decl_list.
    def enterProc_decl_list(self, ctx:HanaParser.Proc_decl_listContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_decl_list.
    def exitProc_decl_list(self, ctx:HanaParser.Proc_decl_listContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_decl.
    def enterProc_decl(self, ctx:HanaParser.Proc_declContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_decl.
    def exitProc_decl(self, ctx:HanaParser.Proc_declContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_decl_op.
    def enterProc_decl_op(self, ctx:HanaParser.Proc_decl_opContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_decl_op.
    def exitProc_decl_op(self, ctx:HanaParser.Proc_decl_opContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_variable.
    def enterProc_variable(self, ctx:HanaParser.Proc_variableContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_variable.
    def exitProc_variable(self, ctx:HanaParser.Proc_variableContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_table_variable.
    def enterProc_table_variable(self, ctx:HanaParser.Proc_table_variableContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_table_variable.
    def exitProc_table_variable(self, ctx:HanaParser.Proc_table_variableContext):
        pass


    # Enter a parse tree produced by HanaParser#variable_name_list.
    def enterVariable_name_list(self, ctx:HanaParser.Variable_name_listContext):
        pass

    # Exit a parse tree produced by HanaParser#variable_name_list.
    def exitVariable_name_list(self, ctx:HanaParser.Variable_name_listContext):
        pass


    # Enter a parse tree produced by HanaParser#array_datatype.
    def enterArray_datatype(self, ctx:HanaParser.Array_datatypeContext):
        pass

    # Exit a parse tree produced by HanaParser#array_datatype.
    def exitArray_datatype(self, ctx:HanaParser.Array_datatypeContext):
        pass


    # Enter a parse tree produced by HanaParser#array_constructor.
    def enterArray_constructor(self, ctx:HanaParser.Array_constructorContext):
        pass

    # Exit a parse tree produced by HanaParser#array_constructor.
    def exitArray_constructor(self, ctx:HanaParser.Array_constructorContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_default.
    def enterProc_default(self, ctx:HanaParser.Proc_defaultContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_default.
    def exitProc_default(self, ctx:HanaParser.Proc_defaultContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_cursor.
    def enterProc_cursor(self, ctx:HanaParser.Proc_cursorContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_cursor.
    def exitProc_cursor(self, ctx:HanaParser.Proc_cursorContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_cursor_param_list.
    def enterProc_cursor_param_list(self, ctx:HanaParser.Proc_cursor_param_listContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_cursor_param_list.
    def exitProc_cursor_param_list(self, ctx:HanaParser.Proc_cursor_param_listContext):
        pass


    # Enter a parse tree produced by HanaParser#variable_name.
    def enterVariable_name(self, ctx:HanaParser.Variable_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#variable_name.
    def exitVariable_name(self, ctx:HanaParser.Variable_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#cursor_name.
    def enterCursor_name(self, ctx:HanaParser.Cursor_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#cursor_name.
    def exitCursor_name(self, ctx:HanaParser.Cursor_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_cursor_param.
    def enterProc_cursor_param(self, ctx:HanaParser.Proc_cursor_paramContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_cursor_param.
    def exitProc_cursor_param(self, ctx:HanaParser.Proc_cursor_paramContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_condition.
    def enterProc_condition(self, ctx:HanaParser.Proc_conditionContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_condition.
    def exitProc_condition(self, ctx:HanaParser.Proc_conditionContext):
        pass


    # Enter a parse tree produced by HanaParser#sql_error_code.
    def enterSql_error_code(self, ctx:HanaParser.Sql_error_codeContext):
        pass

    # Exit a parse tree produced by HanaParser#sql_error_code.
    def exitSql_error_code(self, ctx:HanaParser.Sql_error_codeContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_handler_list.
    def enterProc_handler_list(self, ctx:HanaParser.Proc_handler_listContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_handler_list.
    def exitProc_handler_list(self, ctx:HanaParser.Proc_handler_listContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_handler.
    def enterProc_handler(self, ctx:HanaParser.Proc_handlerContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_handler.
    def exitProc_handler(self, ctx:HanaParser.Proc_handlerContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_condition_value_list.
    def enterProc_condition_value_list(self, ctx:HanaParser.Proc_condition_value_listContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_condition_value_list.
    def exitProc_condition_value_list(self, ctx:HanaParser.Proc_condition_value_listContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_condition_value.
    def enterProc_condition_value(self, ctx:HanaParser.Proc_condition_valueContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_condition_value.
    def exitProc_condition_value(self, ctx:HanaParser.Proc_condition_valueContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_stmt_list.
    def enterProc_stmt_list(self, ctx:HanaParser.Proc_stmt_listContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_stmt_list.
    def exitProc_stmt_list(self, ctx:HanaParser.Proc_stmt_listContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_stmt.
    def enterProc_stmt(self, ctx:HanaParser.Proc_stmtContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_stmt.
    def exitProc_stmt(self, ctx:HanaParser.Proc_stmtContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_sql.
    def enterProc_sql(self, ctx:HanaParser.Proc_sqlContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_sql.
    def exitProc_sql(self, ctx:HanaParser.Proc_sqlContext):
        pass


    # Enter a parse tree produced by HanaParser#update_stmt.
    def enterUpdate_stmt(self, ctx:HanaParser.Update_stmtContext):
        pass

    # Exit a parse tree produced by HanaParser#update_stmt.
    def exitUpdate_stmt(self, ctx:HanaParser.Update_stmtContext):
        pass


    # Enter a parse tree produced by HanaParser#insert_stmt.
    def enterInsert_stmt(self, ctx:HanaParser.Insert_stmtContext):
        pass

    # Exit a parse tree produced by HanaParser#insert_stmt.
    def exitInsert_stmt(self, ctx:HanaParser.Insert_stmtContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_signal.
    def enterProc_signal(self, ctx:HanaParser.Proc_signalContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_signal.
    def exitProc_signal(self, ctx:HanaParser.Proc_signalContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_resignal.
    def enterProc_resignal(self, ctx:HanaParser.Proc_resignalContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_resignal.
    def exitProc_resignal(self, ctx:HanaParser.Proc_resignalContext):
        pass


    # Enter a parse tree produced by HanaParser#signal_value.
    def enterSignal_value(self, ctx:HanaParser.Signal_valueContext):
        pass

    # Exit a parse tree produced by HanaParser#signal_value.
    def exitSignal_value(self, ctx:HanaParser.Signal_valueContext):
        pass


    # Enter a parse tree produced by HanaParser#signal_name.
    def enterSignal_name(self, ctx:HanaParser.Signal_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#signal_name.
    def exitSignal_name(self, ctx:HanaParser.Signal_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#set_signal_info.
    def enterSet_signal_info(self, ctx:HanaParser.Set_signal_infoContext):
        pass

    # Exit a parse tree produced by HanaParser#set_signal_info.
    def exitSet_signal_info(self, ctx:HanaParser.Set_signal_infoContext):
        pass


    # Enter a parse tree produced by HanaParser#message_string.
    def enterMessage_string(self, ctx:HanaParser.Message_stringContext):
        pass

    # Exit a parse tree produced by HanaParser#message_string.
    def exitMessage_string(self, ctx:HanaParser.Message_stringContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_if.
    def enterProc_if(self, ctx:HanaParser.Proc_ifContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_if.
    def exitProc_if(self, ctx:HanaParser.Proc_ifContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_elsif_list.
    def enterProc_elsif_list(self, ctx:HanaParser.Proc_elsif_listContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_elsif_list.
    def exitProc_elsif_list(self, ctx:HanaParser.Proc_elsif_listContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_else.
    def enterProc_else(self, ctx:HanaParser.Proc_elseContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_else.
    def exitProc_else(self, ctx:HanaParser.Proc_elseContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_block.
    def enterProc_block(self, ctx:HanaParser.Proc_blockContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_block.
    def exitProc_block(self, ctx:HanaParser.Proc_blockContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_block_option.
    def enterProc_block_option(self, ctx:HanaParser.Proc_block_optionContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_block_option.
    def exitProc_block_option(self, ctx:HanaParser.Proc_block_optionContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_assign.
    def enterProc_assign(self, ctx:HanaParser.Proc_assignContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_assign.
    def exitProc_assign(self, ctx:HanaParser.Proc_assignContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_single_assign.
    def enterProc_single_assign(self, ctx:HanaParser.Proc_single_assignContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_single_assign.
    def exitProc_single_assign(self, ctx:HanaParser.Proc_single_assignContext):
        pass


    # Enter a parse tree produced by HanaParser#unnest_function.
    def enterUnnest_function(self, ctx:HanaParser.Unnest_functionContext):
        pass

    # Exit a parse tree produced by HanaParser#unnest_function.
    def exitUnnest_function(self, ctx:HanaParser.Unnest_functionContext):
        pass


    # Enter a parse tree produced by HanaParser#table_name.
    def enterTable_name(self, ctx:HanaParser.Table_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#table_name.
    def exitTable_name(self, ctx:HanaParser.Table_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#as_col_names.
    def enterAs_col_names(self, ctx:HanaParser.As_col_namesContext):
        pass

    # Exit a parse tree produced by HanaParser#as_col_names.
    def exitAs_col_names(self, ctx:HanaParser.As_col_namesContext):
        pass


    # Enter a parse tree produced by HanaParser#column_name_list.
    def enterColumn_name_list(self, ctx:HanaParser.Column_name_listContext):
        pass

    # Exit a parse tree produced by HanaParser#column_name_list.
    def exitColumn_name_list(self, ctx:HanaParser.Column_name_listContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_call.
    def enterProc_call(self, ctx:HanaParser.Proc_callContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_call.
    def exitProc_call(self, ctx:HanaParser.Proc_callContext):
        pass


    # Enter a parse tree produced by HanaParser#param_list.
    def enterParam_list(self, ctx:HanaParser.Param_listContext):
        pass

    # Exit a parse tree produced by HanaParser#param_list.
    def exitParam_list(self, ctx:HanaParser.Param_listContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_param.
    def enterProc_param(self, ctx:HanaParser.Proc_paramContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_param.
    def exitProc_param(self, ctx:HanaParser.Proc_paramContext):
        pass


    # Enter a parse tree produced by HanaParser#named_param.
    def enterNamed_param(self, ctx:HanaParser.Named_paramContext):
        pass

    # Exit a parse tree produced by HanaParser#named_param.
    def exitNamed_param(self, ctx:HanaParser.Named_paramContext):
        pass


    # Enter a parse tree produced by HanaParser#procedure_body.
    def enterProcedure_body(self, ctx:HanaParser.Procedure_bodyContext):
        pass

    # Exit a parse tree produced by HanaParser#procedure_body.
    def exitProcedure_body(self, ctx:HanaParser.Procedure_bodyContext):
        pass


    # Enter a parse tree produced by HanaParser#procedure_body_.
    def enterProcedure_body_(self, ctx:HanaParser.Procedure_body_Context):
        pass

    # Exit a parse tree produced by HanaParser#procedure_body_.
    def exitProcedure_body_(self, ctx:HanaParser.Procedure_body_Context):
        pass


    # Enter a parse tree produced by HanaParser#parameter_name.
    def enterParameter_name(self, ctx:HanaParser.Parameter_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#parameter_name.
    def exitParameter_name(self, ctx:HanaParser.Parameter_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#for_each_row.
    def enterFor_each_row(self, ctx:HanaParser.For_each_rowContext):
        pass

    # Exit a parse tree produced by HanaParser#for_each_row.
    def exitFor_each_row(self, ctx:HanaParser.For_each_rowContext):
        pass


    # Enter a parse tree produced by HanaParser#alter_attribute_definition.
    def enterAlter_attribute_definition(self, ctx:HanaParser.Alter_attribute_definitionContext):
        pass

    # Exit a parse tree produced by HanaParser#alter_attribute_definition.
    def exitAlter_attribute_definition(self, ctx:HanaParser.Alter_attribute_definitionContext):
        pass


    # Enter a parse tree produced by HanaParser#attribute_definition.
    def enterAttribute_definition(self, ctx:HanaParser.Attribute_definitionContext):
        pass

    # Exit a parse tree produced by HanaParser#attribute_definition.
    def exitAttribute_definition(self, ctx:HanaParser.Attribute_definitionContext):
        pass


    # Enter a parse tree produced by HanaParser#alter_collection_clauses.
    def enterAlter_collection_clauses(self, ctx:HanaParser.Alter_collection_clausesContext):
        pass

    # Exit a parse tree produced by HanaParser#alter_collection_clauses.
    def exitAlter_collection_clauses(self, ctx:HanaParser.Alter_collection_clausesContext):
        pass


    # Enter a parse tree produced by HanaParser#dependent_handling_clause.
    def enterDependent_handling_clause(self, ctx:HanaParser.Dependent_handling_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#dependent_handling_clause.
    def exitDependent_handling_clause(self, ctx:HanaParser.Dependent_handling_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#dependent_exceptions_part.
    def enterDependent_exceptions_part(self, ctx:HanaParser.Dependent_exceptions_partContext):
        pass

    # Exit a parse tree produced by HanaParser#dependent_exceptions_part.
    def exitDependent_exceptions_part(self, ctx:HanaParser.Dependent_exceptions_partContext):
        pass


    # Enter a parse tree produced by HanaParser#type_definition.
    def enterType_definition(self, ctx:HanaParser.Type_definitionContext):
        pass

    # Exit a parse tree produced by HanaParser#type_definition.
    def exitType_definition(self, ctx:HanaParser.Type_definitionContext):
        pass


    # Enter a parse tree produced by HanaParser#object_type_def.
    def enterObject_type_def(self, ctx:HanaParser.Object_type_defContext):
        pass

    # Exit a parse tree produced by HanaParser#object_type_def.
    def exitObject_type_def(self, ctx:HanaParser.Object_type_defContext):
        pass


    # Enter a parse tree produced by HanaParser#object_as_part.
    def enterObject_as_part(self, ctx:HanaParser.Object_as_partContext):
        pass

    # Exit a parse tree produced by HanaParser#object_as_part.
    def exitObject_as_part(self, ctx:HanaParser.Object_as_partContext):
        pass


    # Enter a parse tree produced by HanaParser#object_under_part.
    def enterObject_under_part(self, ctx:HanaParser.Object_under_partContext):
        pass

    # Exit a parse tree produced by HanaParser#object_under_part.
    def exitObject_under_part(self, ctx:HanaParser.Object_under_partContext):
        pass


    # Enter a parse tree produced by HanaParser#nested_table_type_def.
    def enterNested_table_type_def(self, ctx:HanaParser.Nested_table_type_defContext):
        pass

    # Exit a parse tree produced by HanaParser#nested_table_type_def.
    def exitNested_table_type_def(self, ctx:HanaParser.Nested_table_type_defContext):
        pass


    # Enter a parse tree produced by HanaParser#sqlj_object_type.
    def enterSqlj_object_type(self, ctx:HanaParser.Sqlj_object_typeContext):
        pass

    # Exit a parse tree produced by HanaParser#sqlj_object_type.
    def exitSqlj_object_type(self, ctx:HanaParser.Sqlj_object_typeContext):
        pass


    # Enter a parse tree produced by HanaParser#type_body.
    def enterType_body(self, ctx:HanaParser.Type_bodyContext):
        pass

    # Exit a parse tree produced by HanaParser#type_body.
    def exitType_body(self, ctx:HanaParser.Type_bodyContext):
        pass


    # Enter a parse tree produced by HanaParser#type_body_elements.
    def enterType_body_elements(self, ctx:HanaParser.Type_body_elementsContext):
        pass

    # Exit a parse tree produced by HanaParser#type_body_elements.
    def exitType_body_elements(self, ctx:HanaParser.Type_body_elementsContext):
        pass


    # Enter a parse tree produced by HanaParser#map_order_func_declaration.
    def enterMap_order_func_declaration(self, ctx:HanaParser.Map_order_func_declarationContext):
        pass

    # Exit a parse tree produced by HanaParser#map_order_func_declaration.
    def exitMap_order_func_declaration(self, ctx:HanaParser.Map_order_func_declarationContext):
        pass


    # Enter a parse tree produced by HanaParser#subprog_decl_in_type.
    def enterSubprog_decl_in_type(self, ctx:HanaParser.Subprog_decl_in_typeContext):
        pass

    # Exit a parse tree produced by HanaParser#subprog_decl_in_type.
    def exitSubprog_decl_in_type(self, ctx:HanaParser.Subprog_decl_in_typeContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_decl_in_type.
    def enterProc_decl_in_type(self, ctx:HanaParser.Proc_decl_in_typeContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_decl_in_type.
    def exitProc_decl_in_type(self, ctx:HanaParser.Proc_decl_in_typeContext):
        pass


    # Enter a parse tree produced by HanaParser#func_decl_in_type.
    def enterFunc_decl_in_type(self, ctx:HanaParser.Func_decl_in_typeContext):
        pass

    # Exit a parse tree produced by HanaParser#func_decl_in_type.
    def exitFunc_decl_in_type(self, ctx:HanaParser.Func_decl_in_typeContext):
        pass


    # Enter a parse tree produced by HanaParser#constructor_declaration.
    def enterConstructor_declaration(self, ctx:HanaParser.Constructor_declarationContext):
        pass

    # Exit a parse tree produced by HanaParser#constructor_declaration.
    def exitConstructor_declaration(self, ctx:HanaParser.Constructor_declarationContext):
        pass


    # Enter a parse tree produced by HanaParser#modifier_clause.
    def enterModifier_clause(self, ctx:HanaParser.Modifier_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#modifier_clause.
    def exitModifier_clause(self, ctx:HanaParser.Modifier_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#object_member_spec.
    def enterObject_member_spec(self, ctx:HanaParser.Object_member_specContext):
        pass

    # Exit a parse tree produced by HanaParser#object_member_spec.
    def exitObject_member_spec(self, ctx:HanaParser.Object_member_specContext):
        pass


    # Enter a parse tree produced by HanaParser#sqlj_object_type_attr.
    def enterSqlj_object_type_attr(self, ctx:HanaParser.Sqlj_object_type_attrContext):
        pass

    # Exit a parse tree produced by HanaParser#sqlj_object_type_attr.
    def exitSqlj_object_type_attr(self, ctx:HanaParser.Sqlj_object_type_attrContext):
        pass


    # Enter a parse tree produced by HanaParser#element_spec.
    def enterElement_spec(self, ctx:HanaParser.Element_specContext):
        pass

    # Exit a parse tree produced by HanaParser#element_spec.
    def exitElement_spec(self, ctx:HanaParser.Element_specContext):
        pass


    # Enter a parse tree produced by HanaParser#element_spec_options.
    def enterElement_spec_options(self, ctx:HanaParser.Element_spec_optionsContext):
        pass

    # Exit a parse tree produced by HanaParser#element_spec_options.
    def exitElement_spec_options(self, ctx:HanaParser.Element_spec_optionsContext):
        pass


    # Enter a parse tree produced by HanaParser#subprogram_spec.
    def enterSubprogram_spec(self, ctx:HanaParser.Subprogram_specContext):
        pass

    # Exit a parse tree produced by HanaParser#subprogram_spec.
    def exitSubprogram_spec(self, ctx:HanaParser.Subprogram_specContext):
        pass


    # Enter a parse tree produced by HanaParser#type_procedure_spec.
    def enterType_procedure_spec(self, ctx:HanaParser.Type_procedure_specContext):
        pass

    # Exit a parse tree produced by HanaParser#type_procedure_spec.
    def exitType_procedure_spec(self, ctx:HanaParser.Type_procedure_specContext):
        pass


    # Enter a parse tree produced by HanaParser#type_function_spec.
    def enterType_function_spec(self, ctx:HanaParser.Type_function_specContext):
        pass

    # Exit a parse tree produced by HanaParser#type_function_spec.
    def exitType_function_spec(self, ctx:HanaParser.Type_function_specContext):
        pass


    # Enter a parse tree produced by HanaParser#constructor_spec.
    def enterConstructor_spec(self, ctx:HanaParser.Constructor_specContext):
        pass

    # Exit a parse tree produced by HanaParser#constructor_spec.
    def exitConstructor_spec(self, ctx:HanaParser.Constructor_specContext):
        pass


    # Enter a parse tree produced by HanaParser#map_order_function_spec.
    def enterMap_order_function_spec(self, ctx:HanaParser.Map_order_function_specContext):
        pass

    # Exit a parse tree produced by HanaParser#map_order_function_spec.
    def exitMap_order_function_spec(self, ctx:HanaParser.Map_order_function_specContext):
        pass


    # Enter a parse tree produced by HanaParser#pragma_clause.
    def enterPragma_clause(self, ctx:HanaParser.Pragma_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#pragma_clause.
    def exitPragma_clause(self, ctx:HanaParser.Pragma_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#pragma_elements.
    def enterPragma_elements(self, ctx:HanaParser.Pragma_elementsContext):
        pass

    # Exit a parse tree produced by HanaParser#pragma_elements.
    def exitPragma_elements(self, ctx:HanaParser.Pragma_elementsContext):
        pass


    # Enter a parse tree produced by HanaParser#type_elements_parameter.
    def enterType_elements_parameter(self, ctx:HanaParser.Type_elements_parameterContext):
        pass

    # Exit a parse tree produced by HanaParser#type_elements_parameter.
    def exitType_elements_parameter(self, ctx:HanaParser.Type_elements_parameterContext):
        pass


    # Enter a parse tree produced by HanaParser#create_sequence.
    def enterCreate_sequence(self, ctx:HanaParser.Create_sequenceContext):
        pass

    # Exit a parse tree produced by HanaParser#create_sequence.
    def exitCreate_sequence(self, ctx:HanaParser.Create_sequenceContext):
        pass


    # Enter a parse tree produced by HanaParser#sequence_spec.
    def enterSequence_spec(self, ctx:HanaParser.Sequence_specContext):
        pass

    # Exit a parse tree produced by HanaParser#sequence_spec.
    def exitSequence_spec(self, ctx:HanaParser.Sequence_specContext):
        pass


    # Enter a parse tree produced by HanaParser#sequence_start_clause.
    def enterSequence_start_clause(self, ctx:HanaParser.Sequence_start_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#sequence_start_clause.
    def exitSequence_start_clause(self, ctx:HanaParser.Sequence_start_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#invoker_rights_clause.
    def enterInvoker_rights_clause(self, ctx:HanaParser.Invoker_rights_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#invoker_rights_clause.
    def exitInvoker_rights_clause(self, ctx:HanaParser.Invoker_rights_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#compiler_parameters_clause.
    def enterCompiler_parameters_clause(self, ctx:HanaParser.Compiler_parameters_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#compiler_parameters_clause.
    def exitCompiler_parameters_clause(self, ctx:HanaParser.Compiler_parameters_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#call_spec.
    def enterCall_spec(self, ctx:HanaParser.Call_specContext):
        pass

    # Exit a parse tree produced by HanaParser#call_spec.
    def exitCall_spec(self, ctx:HanaParser.Call_specContext):
        pass


    # Enter a parse tree produced by HanaParser#java_spec.
    def enterJava_spec(self, ctx:HanaParser.Java_specContext):
        pass

    # Exit a parse tree produced by HanaParser#java_spec.
    def exitJava_spec(self, ctx:HanaParser.Java_specContext):
        pass


    # Enter a parse tree produced by HanaParser#c_spec.
    def enterC_spec(self, ctx:HanaParser.C_specContext):
        pass

    # Exit a parse tree produced by HanaParser#c_spec.
    def exitC_spec(self, ctx:HanaParser.C_specContext):
        pass


    # Enter a parse tree produced by HanaParser#c_agent_in_clause.
    def enterC_agent_in_clause(self, ctx:HanaParser.C_agent_in_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#c_agent_in_clause.
    def exitC_agent_in_clause(self, ctx:HanaParser.C_agent_in_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#c_parameters_clause.
    def enterC_parameters_clause(self, ctx:HanaParser.C_parameters_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#c_parameters_clause.
    def exitC_parameters_clause(self, ctx:HanaParser.C_parameters_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#default_value_part.
    def enterDefault_value_part(self, ctx:HanaParser.Default_value_partContext):
        pass

    # Exit a parse tree produced by HanaParser#default_value_part.
    def exitDefault_value_part(self, ctx:HanaParser.Default_value_partContext):
        pass


    # Enter a parse tree produced by HanaParser#declare_spec.
    def enterDeclare_spec(self, ctx:HanaParser.Declare_specContext):
        pass

    # Exit a parse tree produced by HanaParser#declare_spec.
    def exitDeclare_spec(self, ctx:HanaParser.Declare_specContext):
        pass


    # Enter a parse tree produced by HanaParser#variable_declaration.
    def enterVariable_declaration(self, ctx:HanaParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by HanaParser#variable_declaration.
    def exitVariable_declaration(self, ctx:HanaParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by HanaParser#subtype_declaration.
    def enterSubtype_declaration(self, ctx:HanaParser.Subtype_declarationContext):
        pass

    # Exit a parse tree produced by HanaParser#subtype_declaration.
    def exitSubtype_declaration(self, ctx:HanaParser.Subtype_declarationContext):
        pass


    # Enter a parse tree produced by HanaParser#cursor_declaration.
    def enterCursor_declaration(self, ctx:HanaParser.Cursor_declarationContext):
        pass

    # Exit a parse tree produced by HanaParser#cursor_declaration.
    def exitCursor_declaration(self, ctx:HanaParser.Cursor_declarationContext):
        pass


    # Enter a parse tree produced by HanaParser#parameter_spec.
    def enterParameter_spec(self, ctx:HanaParser.Parameter_specContext):
        pass

    # Exit a parse tree produced by HanaParser#parameter_spec.
    def exitParameter_spec(self, ctx:HanaParser.Parameter_specContext):
        pass


    # Enter a parse tree produced by HanaParser#exception_declaration.
    def enterException_declaration(self, ctx:HanaParser.Exception_declarationContext):
        pass

    # Exit a parse tree produced by HanaParser#exception_declaration.
    def exitException_declaration(self, ctx:HanaParser.Exception_declarationContext):
        pass


    # Enter a parse tree produced by HanaParser#pragma_declaration.
    def enterPragma_declaration(self, ctx:HanaParser.Pragma_declarationContext):
        pass

    # Exit a parse tree produced by HanaParser#pragma_declaration.
    def exitPragma_declaration(self, ctx:HanaParser.Pragma_declarationContext):
        pass


    # Enter a parse tree produced by HanaParser#record_declaration.
    def enterRecord_declaration(self, ctx:HanaParser.Record_declarationContext):
        pass

    # Exit a parse tree produced by HanaParser#record_declaration.
    def exitRecord_declaration(self, ctx:HanaParser.Record_declarationContext):
        pass


    # Enter a parse tree produced by HanaParser#record_type_dec.
    def enterRecord_type_dec(self, ctx:HanaParser.Record_type_decContext):
        pass

    # Exit a parse tree produced by HanaParser#record_type_dec.
    def exitRecord_type_dec(self, ctx:HanaParser.Record_type_decContext):
        pass


    # Enter a parse tree produced by HanaParser#field_spec.
    def enterField_spec(self, ctx:HanaParser.Field_specContext):
        pass

    # Exit a parse tree produced by HanaParser#field_spec.
    def exitField_spec(self, ctx:HanaParser.Field_specContext):
        pass


    # Enter a parse tree produced by HanaParser#record_var_dec.
    def enterRecord_var_dec(self, ctx:HanaParser.Record_var_decContext):
        pass

    # Exit a parse tree produced by HanaParser#record_var_dec.
    def exitRecord_var_dec(self, ctx:HanaParser.Record_var_decContext):
        pass


    # Enter a parse tree produced by HanaParser#table_declaration.
    def enterTable_declaration(self, ctx:HanaParser.Table_declarationContext):
        pass

    # Exit a parse tree produced by HanaParser#table_declaration.
    def exitTable_declaration(self, ctx:HanaParser.Table_declarationContext):
        pass


    # Enter a parse tree produced by HanaParser#table_type_dec.
    def enterTable_type_dec(self, ctx:HanaParser.Table_type_decContext):
        pass

    # Exit a parse tree produced by HanaParser#table_type_dec.
    def exitTable_type_dec(self, ctx:HanaParser.Table_type_decContext):
        pass


    # Enter a parse tree produced by HanaParser#table_indexed_by_part.
    def enterTable_indexed_by_part(self, ctx:HanaParser.Table_indexed_by_partContext):
        pass

    # Exit a parse tree produced by HanaParser#table_indexed_by_part.
    def exitTable_indexed_by_part(self, ctx:HanaParser.Table_indexed_by_partContext):
        pass


    # Enter a parse tree produced by HanaParser#varray_type_def.
    def enterVarray_type_def(self, ctx:HanaParser.Varray_type_defContext):
        pass

    # Exit a parse tree produced by HanaParser#varray_type_def.
    def exitVarray_type_def(self, ctx:HanaParser.Varray_type_defContext):
        pass


    # Enter a parse tree produced by HanaParser#table_var_dec.
    def enterTable_var_dec(self, ctx:HanaParser.Table_var_decContext):
        pass

    # Exit a parse tree produced by HanaParser#table_var_dec.
    def exitTable_var_dec(self, ctx:HanaParser.Table_var_decContext):
        pass


    # Enter a parse tree produced by HanaParser#seq_of_statements.
    def enterSeq_of_statements(self, ctx:HanaParser.Seq_of_statementsContext):
        pass

    # Exit a parse tree produced by HanaParser#seq_of_statements.
    def exitSeq_of_statements(self, ctx:HanaParser.Seq_of_statementsContext):
        pass


    # Enter a parse tree produced by HanaParser#label_declaration.
    def enterLabel_declaration(self, ctx:HanaParser.Label_declarationContext):
        pass

    # Exit a parse tree produced by HanaParser#label_declaration.
    def exitLabel_declaration(self, ctx:HanaParser.Label_declarationContext):
        pass


    # Enter a parse tree produced by HanaParser#statement.
    def enterStatement(self, ctx:HanaParser.StatementContext):
        pass

    # Exit a parse tree produced by HanaParser#statement.
    def exitStatement(self, ctx:HanaParser.StatementContext):
        pass


    # Enter a parse tree produced by HanaParser#assignment_statement.
    def enterAssignment_statement(self, ctx:HanaParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#assignment_statement.
    def exitAssignment_statement(self, ctx:HanaParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#continue_statement.
    def enterContinue_statement(self, ctx:HanaParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#continue_statement.
    def exitContinue_statement(self, ctx:HanaParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#exit_statement.
    def enterExit_statement(self, ctx:HanaParser.Exit_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#exit_statement.
    def exitExit_statement(self, ctx:HanaParser.Exit_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#goto_statement.
    def enterGoto_statement(self, ctx:HanaParser.Goto_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#goto_statement.
    def exitGoto_statement(self, ctx:HanaParser.Goto_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#if_statement.
    def enterIf_statement(self, ctx:HanaParser.If_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#if_statement.
    def exitIf_statement(self, ctx:HanaParser.If_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#elsif_part.
    def enterElsif_part(self, ctx:HanaParser.Elsif_partContext):
        pass

    # Exit a parse tree produced by HanaParser#elsif_part.
    def exitElsif_part(self, ctx:HanaParser.Elsif_partContext):
        pass


    # Enter a parse tree produced by HanaParser#else_part.
    def enterElse_part(self, ctx:HanaParser.Else_partContext):
        pass

    # Exit a parse tree produced by HanaParser#else_part.
    def exitElse_part(self, ctx:HanaParser.Else_partContext):
        pass


    # Enter a parse tree produced by HanaParser#loop_statement.
    def enterLoop_statement(self, ctx:HanaParser.Loop_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#loop_statement.
    def exitLoop_statement(self, ctx:HanaParser.Loop_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#cursor_loop_param.
    def enterCursor_loop_param(self, ctx:HanaParser.Cursor_loop_paramContext):
        pass

    # Exit a parse tree produced by HanaParser#cursor_loop_param.
    def exitCursor_loop_param(self, ctx:HanaParser.Cursor_loop_paramContext):
        pass


    # Enter a parse tree produced by HanaParser#forall_statement.
    def enterForall_statement(self, ctx:HanaParser.Forall_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#forall_statement.
    def exitForall_statement(self, ctx:HanaParser.Forall_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#bounds_clause.
    def enterBounds_clause(self, ctx:HanaParser.Bounds_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#bounds_clause.
    def exitBounds_clause(self, ctx:HanaParser.Bounds_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#between_bound.
    def enterBetween_bound(self, ctx:HanaParser.Between_boundContext):
        pass

    # Exit a parse tree produced by HanaParser#between_bound.
    def exitBetween_bound(self, ctx:HanaParser.Between_boundContext):
        pass


    # Enter a parse tree produced by HanaParser#lower_bound.
    def enterLower_bound(self, ctx:HanaParser.Lower_boundContext):
        pass

    # Exit a parse tree produced by HanaParser#lower_bound.
    def exitLower_bound(self, ctx:HanaParser.Lower_boundContext):
        pass


    # Enter a parse tree produced by HanaParser#upper_bound.
    def enterUpper_bound(self, ctx:HanaParser.Upper_boundContext):
        pass

    # Exit a parse tree produced by HanaParser#upper_bound.
    def exitUpper_bound(self, ctx:HanaParser.Upper_boundContext):
        pass


    # Enter a parse tree produced by HanaParser#null_statement.
    def enterNull_statement(self, ctx:HanaParser.Null_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#null_statement.
    def exitNull_statement(self, ctx:HanaParser.Null_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#raise_statement.
    def enterRaise_statement(self, ctx:HanaParser.Raise_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#raise_statement.
    def exitRaise_statement(self, ctx:HanaParser.Raise_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#return_statement.
    def enterReturn_statement(self, ctx:HanaParser.Return_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#return_statement.
    def exitReturn_statement(self, ctx:HanaParser.Return_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#function_call.
    def enterFunction_call(self, ctx:HanaParser.Function_callContext):
        pass

    # Exit a parse tree produced by HanaParser#function_call.
    def exitFunction_call(self, ctx:HanaParser.Function_callContext):
        pass


    # Enter a parse tree produced by HanaParser#body.
    def enterBody(self, ctx:HanaParser.BodyContext):
        pass

    # Exit a parse tree produced by HanaParser#body.
    def exitBody(self, ctx:HanaParser.BodyContext):
        pass


    # Enter a parse tree produced by HanaParser#exception_clause.
    def enterException_clause(self, ctx:HanaParser.Exception_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#exception_clause.
    def exitException_clause(self, ctx:HanaParser.Exception_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#exception_handler.
    def enterException_handler(self, ctx:HanaParser.Exception_handlerContext):
        pass

    # Exit a parse tree produced by HanaParser#exception_handler.
    def exitException_handler(self, ctx:HanaParser.Exception_handlerContext):
        pass


    # Enter a parse tree produced by HanaParser#trigger_block.
    def enterTrigger_block(self, ctx:HanaParser.Trigger_blockContext):
        pass

    # Exit a parse tree produced by HanaParser#trigger_block.
    def exitTrigger_block(self, ctx:HanaParser.Trigger_blockContext):
        pass


    # Enter a parse tree produced by HanaParser#block.
    def enterBlock(self, ctx:HanaParser.BlockContext):
        pass

    # Exit a parse tree produced by HanaParser#block.
    def exitBlock(self, ctx:HanaParser.BlockContext):
        pass


    # Enter a parse tree produced by HanaParser#sql_statement.
    def enterSql_statement(self, ctx:HanaParser.Sql_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#sql_statement.
    def exitSql_statement(self, ctx:HanaParser.Sql_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#execute_immediate.
    def enterExecute_immediate(self, ctx:HanaParser.Execute_immediateContext):
        pass

    # Exit a parse tree produced by HanaParser#execute_immediate.
    def exitExecute_immediate(self, ctx:HanaParser.Execute_immediateContext):
        pass


    # Enter a parse tree produced by HanaParser#dynamic_returning_clause.
    def enterDynamic_returning_clause(self, ctx:HanaParser.Dynamic_returning_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#dynamic_returning_clause.
    def exitDynamic_returning_clause(self, ctx:HanaParser.Dynamic_returning_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#data_manipulation_language_statements.
    def enterData_manipulation_language_statements(self, ctx:HanaParser.Data_manipulation_language_statementsContext):
        pass

    # Exit a parse tree produced by HanaParser#data_manipulation_language_statements.
    def exitData_manipulation_language_statements(self, ctx:HanaParser.Data_manipulation_language_statementsContext):
        pass


    # Enter a parse tree produced by HanaParser#cursor_manipulation_statements.
    def enterCursor_manipulation_statements(self, ctx:HanaParser.Cursor_manipulation_statementsContext):
        pass

    # Exit a parse tree produced by HanaParser#cursor_manipulation_statements.
    def exitCursor_manipulation_statements(self, ctx:HanaParser.Cursor_manipulation_statementsContext):
        pass


    # Enter a parse tree produced by HanaParser#close_statement.
    def enterClose_statement(self, ctx:HanaParser.Close_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#close_statement.
    def exitClose_statement(self, ctx:HanaParser.Close_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#open_statement.
    def enterOpen_statement(self, ctx:HanaParser.Open_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#open_statement.
    def exitOpen_statement(self, ctx:HanaParser.Open_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#fetch_statement.
    def enterFetch_statement(self, ctx:HanaParser.Fetch_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#fetch_statement.
    def exitFetch_statement(self, ctx:HanaParser.Fetch_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#open_for_statement.
    def enterOpen_for_statement(self, ctx:HanaParser.Open_for_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#open_for_statement.
    def exitOpen_for_statement(self, ctx:HanaParser.Open_for_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#transaction_control_statements.
    def enterTransaction_control_statements(self, ctx:HanaParser.Transaction_control_statementsContext):
        pass

    # Exit a parse tree produced by HanaParser#transaction_control_statements.
    def exitTransaction_control_statements(self, ctx:HanaParser.Transaction_control_statementsContext):
        pass


    # Enter a parse tree produced by HanaParser#set_transaction_command.
    def enterSet_transaction_command(self, ctx:HanaParser.Set_transaction_commandContext):
        pass

    # Exit a parse tree produced by HanaParser#set_transaction_command.
    def exitSet_transaction_command(self, ctx:HanaParser.Set_transaction_commandContext):
        pass


    # Enter a parse tree produced by HanaParser#set_constraint_command.
    def enterSet_constraint_command(self, ctx:HanaParser.Set_constraint_commandContext):
        pass

    # Exit a parse tree produced by HanaParser#set_constraint_command.
    def exitSet_constraint_command(self, ctx:HanaParser.Set_constraint_commandContext):
        pass


    # Enter a parse tree produced by HanaParser#commit_statement.
    def enterCommit_statement(self, ctx:HanaParser.Commit_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#commit_statement.
    def exitCommit_statement(self, ctx:HanaParser.Commit_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#write_clause.
    def enterWrite_clause(self, ctx:HanaParser.Write_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#write_clause.
    def exitWrite_clause(self, ctx:HanaParser.Write_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#rollback_statement.
    def enterRollback_statement(self, ctx:HanaParser.Rollback_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#rollback_statement.
    def exitRollback_statement(self, ctx:HanaParser.Rollback_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#savepoint_statement.
    def enterSavepoint_statement(self, ctx:HanaParser.Savepoint_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#savepoint_statement.
    def exitSavepoint_statement(self, ctx:HanaParser.Savepoint_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#explain_statement.
    def enterExplain_statement(self, ctx:HanaParser.Explain_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#explain_statement.
    def exitExplain_statement(self, ctx:HanaParser.Explain_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#select_statement.
    def enterSelect_statement(self, ctx:HanaParser.Select_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#select_statement.
    def exitSelect_statement(self, ctx:HanaParser.Select_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#subquery_factoring_clause.
    def enterSubquery_factoring_clause(self, ctx:HanaParser.Subquery_factoring_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#subquery_factoring_clause.
    def exitSubquery_factoring_clause(self, ctx:HanaParser.Subquery_factoring_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#factoring_element.
    def enterFactoring_element(self, ctx:HanaParser.Factoring_elementContext):
        pass

    # Exit a parse tree produced by HanaParser#factoring_element.
    def exitFactoring_element(self, ctx:HanaParser.Factoring_elementContext):
        pass


    # Enter a parse tree produced by HanaParser#search_clause.
    def enterSearch_clause(self, ctx:HanaParser.Search_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#search_clause.
    def exitSearch_clause(self, ctx:HanaParser.Search_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#cycle_clause.
    def enterCycle_clause(self, ctx:HanaParser.Cycle_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#cycle_clause.
    def exitCycle_clause(self, ctx:HanaParser.Cycle_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#subquery.
    def enterSubquery(self, ctx:HanaParser.SubqueryContext):
        pass

    # Exit a parse tree produced by HanaParser#subquery.
    def exitSubquery(self, ctx:HanaParser.SubqueryContext):
        pass


    # Enter a parse tree produced by HanaParser#subquery_operation_part.
    def enterSubquery_operation_part(self, ctx:HanaParser.Subquery_operation_partContext):
        pass

    # Exit a parse tree produced by HanaParser#subquery_operation_part.
    def exitSubquery_operation_part(self, ctx:HanaParser.Subquery_operation_partContext):
        pass


    # Enter a parse tree produced by HanaParser#subquery_basic_elements.
    def enterSubquery_basic_elements(self, ctx:HanaParser.Subquery_basic_elementsContext):
        pass

    # Exit a parse tree produced by HanaParser#subquery_basic_elements.
    def exitSubquery_basic_elements(self, ctx:HanaParser.Subquery_basic_elementsContext):
        pass


    # Enter a parse tree produced by HanaParser#query_block.
    def enterQuery_block(self, ctx:HanaParser.Query_blockContext):
        pass

    # Exit a parse tree produced by HanaParser#query_block.
    def exitQuery_block(self, ctx:HanaParser.Query_blockContext):
        pass


    # Enter a parse tree produced by HanaParser#selected_element.
    def enterSelected_element(self, ctx:HanaParser.Selected_elementContext):
        pass

    # Exit a parse tree produced by HanaParser#selected_element.
    def exitSelected_element(self, ctx:HanaParser.Selected_elementContext):
        pass


    # Enter a parse tree produced by HanaParser#from_clause.
    def enterFrom_clause(self, ctx:HanaParser.From_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#from_clause.
    def exitFrom_clause(self, ctx:HanaParser.From_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#select_list_elements.
    def enterSelect_list_elements(self, ctx:HanaParser.Select_list_elementsContext):
        pass

    # Exit a parse tree produced by HanaParser#select_list_elements.
    def exitSelect_list_elements(self, ctx:HanaParser.Select_list_elementsContext):
        pass


    # Enter a parse tree produced by HanaParser#table_ref_list.
    def enterTable_ref_list(self, ctx:HanaParser.Table_ref_listContext):
        pass

    # Exit a parse tree produced by HanaParser#table_ref_list.
    def exitTable_ref_list(self, ctx:HanaParser.Table_ref_listContext):
        pass


    # Enter a parse tree produced by HanaParser#table_ref.
    def enterTable_ref(self, ctx:HanaParser.Table_refContext):
        pass

    # Exit a parse tree produced by HanaParser#table_ref.
    def exitTable_ref(self, ctx:HanaParser.Table_refContext):
        pass


    # Enter a parse tree produced by HanaParser#table_ref_aux.
    def enterTable_ref_aux(self, ctx:HanaParser.Table_ref_auxContext):
        pass

    # Exit a parse tree produced by HanaParser#table_ref_aux.
    def exitTable_ref_aux(self, ctx:HanaParser.Table_ref_auxContext):
        pass


    # Enter a parse tree produced by HanaParser#join_clause.
    def enterJoin_clause(self, ctx:HanaParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#join_clause.
    def exitJoin_clause(self, ctx:HanaParser.Join_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#join_on_part.
    def enterJoin_on_part(self, ctx:HanaParser.Join_on_partContext):
        pass

    # Exit a parse tree produced by HanaParser#join_on_part.
    def exitJoin_on_part(self, ctx:HanaParser.Join_on_partContext):
        pass


    # Enter a parse tree produced by HanaParser#join_using_part.
    def enterJoin_using_part(self, ctx:HanaParser.Join_using_partContext):
        pass

    # Exit a parse tree produced by HanaParser#join_using_part.
    def exitJoin_using_part(self, ctx:HanaParser.Join_using_partContext):
        pass


    # Enter a parse tree produced by HanaParser#outer_join_type.
    def enterOuter_join_type(self, ctx:HanaParser.Outer_join_typeContext):
        pass

    # Exit a parse tree produced by HanaParser#outer_join_type.
    def exitOuter_join_type(self, ctx:HanaParser.Outer_join_typeContext):
        pass


    # Enter a parse tree produced by HanaParser#query_partition_clause.
    def enterQuery_partition_clause(self, ctx:HanaParser.Query_partition_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#query_partition_clause.
    def exitQuery_partition_clause(self, ctx:HanaParser.Query_partition_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#flashback_query_clause.
    def enterFlashback_query_clause(self, ctx:HanaParser.Flashback_query_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#flashback_query_clause.
    def exitFlashback_query_clause(self, ctx:HanaParser.Flashback_query_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#pivot_clause.
    def enterPivot_clause(self, ctx:HanaParser.Pivot_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#pivot_clause.
    def exitPivot_clause(self, ctx:HanaParser.Pivot_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#pivot_element.
    def enterPivot_element(self, ctx:HanaParser.Pivot_elementContext):
        pass

    # Exit a parse tree produced by HanaParser#pivot_element.
    def exitPivot_element(self, ctx:HanaParser.Pivot_elementContext):
        pass


    # Enter a parse tree produced by HanaParser#pivot_for_clause.
    def enterPivot_for_clause(self, ctx:HanaParser.Pivot_for_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#pivot_for_clause.
    def exitPivot_for_clause(self, ctx:HanaParser.Pivot_for_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#pivot_in_clause.
    def enterPivot_in_clause(self, ctx:HanaParser.Pivot_in_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#pivot_in_clause.
    def exitPivot_in_clause(self, ctx:HanaParser.Pivot_in_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#pivot_in_clause_element.
    def enterPivot_in_clause_element(self, ctx:HanaParser.Pivot_in_clause_elementContext):
        pass

    # Exit a parse tree produced by HanaParser#pivot_in_clause_element.
    def exitPivot_in_clause_element(self, ctx:HanaParser.Pivot_in_clause_elementContext):
        pass


    # Enter a parse tree produced by HanaParser#pivot_in_clause_elements.
    def enterPivot_in_clause_elements(self, ctx:HanaParser.Pivot_in_clause_elementsContext):
        pass

    # Exit a parse tree produced by HanaParser#pivot_in_clause_elements.
    def exitPivot_in_clause_elements(self, ctx:HanaParser.Pivot_in_clause_elementsContext):
        pass


    # Enter a parse tree produced by HanaParser#unpivot_clause.
    def enterUnpivot_clause(self, ctx:HanaParser.Unpivot_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#unpivot_clause.
    def exitUnpivot_clause(self, ctx:HanaParser.Unpivot_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#unpivot_in_clause.
    def enterUnpivot_in_clause(self, ctx:HanaParser.Unpivot_in_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#unpivot_in_clause.
    def exitUnpivot_in_clause(self, ctx:HanaParser.Unpivot_in_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#unpivot_in_elements.
    def enterUnpivot_in_elements(self, ctx:HanaParser.Unpivot_in_elementsContext):
        pass

    # Exit a parse tree produced by HanaParser#unpivot_in_elements.
    def exitUnpivot_in_elements(self, ctx:HanaParser.Unpivot_in_elementsContext):
        pass


    # Enter a parse tree produced by HanaParser#hierarchical_query_clause.
    def enterHierarchical_query_clause(self, ctx:HanaParser.Hierarchical_query_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#hierarchical_query_clause.
    def exitHierarchical_query_clause(self, ctx:HanaParser.Hierarchical_query_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#start_part.
    def enterStart_part(self, ctx:HanaParser.Start_partContext):
        pass

    # Exit a parse tree produced by HanaParser#start_part.
    def exitStart_part(self, ctx:HanaParser.Start_partContext):
        pass


    # Enter a parse tree produced by HanaParser#group_by_clause.
    def enterGroup_by_clause(self, ctx:HanaParser.Group_by_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#group_by_clause.
    def exitGroup_by_clause(self, ctx:HanaParser.Group_by_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#group_by_elements.
    def enterGroup_by_elements(self, ctx:HanaParser.Group_by_elementsContext):
        pass

    # Exit a parse tree produced by HanaParser#group_by_elements.
    def exitGroup_by_elements(self, ctx:HanaParser.Group_by_elementsContext):
        pass


    # Enter a parse tree produced by HanaParser#rollup_cube_clause.
    def enterRollup_cube_clause(self, ctx:HanaParser.Rollup_cube_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#rollup_cube_clause.
    def exitRollup_cube_clause(self, ctx:HanaParser.Rollup_cube_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#grouping_sets_clause.
    def enterGrouping_sets_clause(self, ctx:HanaParser.Grouping_sets_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#grouping_sets_clause.
    def exitGrouping_sets_clause(self, ctx:HanaParser.Grouping_sets_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#grouping_sets_elements.
    def enterGrouping_sets_elements(self, ctx:HanaParser.Grouping_sets_elementsContext):
        pass

    # Exit a parse tree produced by HanaParser#grouping_sets_elements.
    def exitGrouping_sets_elements(self, ctx:HanaParser.Grouping_sets_elementsContext):
        pass


    # Enter a parse tree produced by HanaParser#having_clause.
    def enterHaving_clause(self, ctx:HanaParser.Having_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#having_clause.
    def exitHaving_clause(self, ctx:HanaParser.Having_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#model_clause.
    def enterModel_clause(self, ctx:HanaParser.Model_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#model_clause.
    def exitModel_clause(self, ctx:HanaParser.Model_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#cell_reference_options.
    def enterCell_reference_options(self, ctx:HanaParser.Cell_reference_optionsContext):
        pass

    # Exit a parse tree produced by HanaParser#cell_reference_options.
    def exitCell_reference_options(self, ctx:HanaParser.Cell_reference_optionsContext):
        pass


    # Enter a parse tree produced by HanaParser#return_rows_clause.
    def enterReturn_rows_clause(self, ctx:HanaParser.Return_rows_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#return_rows_clause.
    def exitReturn_rows_clause(self, ctx:HanaParser.Return_rows_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#reference_model.
    def enterReference_model(self, ctx:HanaParser.Reference_modelContext):
        pass

    # Exit a parse tree produced by HanaParser#reference_model.
    def exitReference_model(self, ctx:HanaParser.Reference_modelContext):
        pass


    # Enter a parse tree produced by HanaParser#main_model.
    def enterMain_model(self, ctx:HanaParser.Main_modelContext):
        pass

    # Exit a parse tree produced by HanaParser#main_model.
    def exitMain_model(self, ctx:HanaParser.Main_modelContext):
        pass


    # Enter a parse tree produced by HanaParser#model_column_clauses.
    def enterModel_column_clauses(self, ctx:HanaParser.Model_column_clausesContext):
        pass

    # Exit a parse tree produced by HanaParser#model_column_clauses.
    def exitModel_column_clauses(self, ctx:HanaParser.Model_column_clausesContext):
        pass


    # Enter a parse tree produced by HanaParser#model_column_partition_part.
    def enterModel_column_partition_part(self, ctx:HanaParser.Model_column_partition_partContext):
        pass

    # Exit a parse tree produced by HanaParser#model_column_partition_part.
    def exitModel_column_partition_part(self, ctx:HanaParser.Model_column_partition_partContext):
        pass


    # Enter a parse tree produced by HanaParser#model_column_list.
    def enterModel_column_list(self, ctx:HanaParser.Model_column_listContext):
        pass

    # Exit a parse tree produced by HanaParser#model_column_list.
    def exitModel_column_list(self, ctx:HanaParser.Model_column_listContext):
        pass


    # Enter a parse tree produced by HanaParser#model_column.
    def enterModel_column(self, ctx:HanaParser.Model_columnContext):
        pass

    # Exit a parse tree produced by HanaParser#model_column.
    def exitModel_column(self, ctx:HanaParser.Model_columnContext):
        pass


    # Enter a parse tree produced by HanaParser#model_rules_clause.
    def enterModel_rules_clause(self, ctx:HanaParser.Model_rules_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#model_rules_clause.
    def exitModel_rules_clause(self, ctx:HanaParser.Model_rules_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#model_rules_part.
    def enterModel_rules_part(self, ctx:HanaParser.Model_rules_partContext):
        pass

    # Exit a parse tree produced by HanaParser#model_rules_part.
    def exitModel_rules_part(self, ctx:HanaParser.Model_rules_partContext):
        pass


    # Enter a parse tree produced by HanaParser#model_rules_element.
    def enterModel_rules_element(self, ctx:HanaParser.Model_rules_elementContext):
        pass

    # Exit a parse tree produced by HanaParser#model_rules_element.
    def exitModel_rules_element(self, ctx:HanaParser.Model_rules_elementContext):
        pass


    # Enter a parse tree produced by HanaParser#cell_assignment.
    def enterCell_assignment(self, ctx:HanaParser.Cell_assignmentContext):
        pass

    # Exit a parse tree produced by HanaParser#cell_assignment.
    def exitCell_assignment(self, ctx:HanaParser.Cell_assignmentContext):
        pass


    # Enter a parse tree produced by HanaParser#model_iterate_clause.
    def enterModel_iterate_clause(self, ctx:HanaParser.Model_iterate_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#model_iterate_clause.
    def exitModel_iterate_clause(self, ctx:HanaParser.Model_iterate_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#until_part.
    def enterUntil_part(self, ctx:HanaParser.Until_partContext):
        pass

    # Exit a parse tree produced by HanaParser#until_part.
    def exitUntil_part(self, ctx:HanaParser.Until_partContext):
        pass


    # Enter a parse tree produced by HanaParser#order_by_clause.
    def enterOrder_by_clause(self, ctx:HanaParser.Order_by_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#order_by_clause.
    def exitOrder_by_clause(self, ctx:HanaParser.Order_by_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#order_by_elements.
    def enterOrder_by_elements(self, ctx:HanaParser.Order_by_elementsContext):
        pass

    # Exit a parse tree produced by HanaParser#order_by_elements.
    def exitOrder_by_elements(self, ctx:HanaParser.Order_by_elementsContext):
        pass


    # Enter a parse tree produced by HanaParser#for_update_clause.
    def enterFor_update_clause(self, ctx:HanaParser.For_update_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#for_update_clause.
    def exitFor_update_clause(self, ctx:HanaParser.For_update_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#for_update_of_part.
    def enterFor_update_of_part(self, ctx:HanaParser.For_update_of_partContext):
        pass

    # Exit a parse tree produced by HanaParser#for_update_of_part.
    def exitFor_update_of_part(self, ctx:HanaParser.For_update_of_partContext):
        pass


    # Enter a parse tree produced by HanaParser#for_update_options.
    def enterFor_update_options(self, ctx:HanaParser.For_update_optionsContext):
        pass

    # Exit a parse tree produced by HanaParser#for_update_options.
    def exitFor_update_options(self, ctx:HanaParser.For_update_optionsContext):
        pass


    # Enter a parse tree produced by HanaParser#update_statement.
    def enterUpdate_statement(self, ctx:HanaParser.Update_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#update_statement.
    def exitUpdate_statement(self, ctx:HanaParser.Update_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#update_set_clause.
    def enterUpdate_set_clause(self, ctx:HanaParser.Update_set_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#update_set_clause.
    def exitUpdate_set_clause(self, ctx:HanaParser.Update_set_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#column_based_update_set_clause.
    def enterColumn_based_update_set_clause(self, ctx:HanaParser.Column_based_update_set_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#column_based_update_set_clause.
    def exitColumn_based_update_set_clause(self, ctx:HanaParser.Column_based_update_set_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#delete_statement.
    def enterDelete_statement(self, ctx:HanaParser.Delete_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#delete_statement.
    def exitDelete_statement(self, ctx:HanaParser.Delete_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#insert_statement.
    def enterInsert_statement(self, ctx:HanaParser.Insert_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#insert_statement.
    def exitInsert_statement(self, ctx:HanaParser.Insert_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#declare_statement.
    def enterDeclare_statement(self, ctx:HanaParser.Declare_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#declare_statement.
    def exitDeclare_statement(self, ctx:HanaParser.Declare_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#exception_statement.
    def enterException_statement(self, ctx:HanaParser.Exception_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#exception_statement.
    def exitException_statement(self, ctx:HanaParser.Exception_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_condition_value_.
    def enterProc_condition_value_(self, ctx:HanaParser.Proc_condition_value_Context):
        pass

    # Exit a parse tree produced by HanaParser#proc_condition_value_.
    def exitProc_condition_value_(self, ctx:HanaParser.Proc_condition_value_Context):
        pass


    # Enter a parse tree produced by HanaParser#single_table_insert.
    def enterSingle_table_insert(self, ctx:HanaParser.Single_table_insertContext):
        pass

    # Exit a parse tree produced by HanaParser#single_table_insert.
    def exitSingle_table_insert(self, ctx:HanaParser.Single_table_insertContext):
        pass


    # Enter a parse tree produced by HanaParser#multi_table_insert.
    def enterMulti_table_insert(self, ctx:HanaParser.Multi_table_insertContext):
        pass

    # Exit a parse tree produced by HanaParser#multi_table_insert.
    def exitMulti_table_insert(self, ctx:HanaParser.Multi_table_insertContext):
        pass


    # Enter a parse tree produced by HanaParser#multi_table_element.
    def enterMulti_table_element(self, ctx:HanaParser.Multi_table_elementContext):
        pass

    # Exit a parse tree produced by HanaParser#multi_table_element.
    def exitMulti_table_element(self, ctx:HanaParser.Multi_table_elementContext):
        pass


    # Enter a parse tree produced by HanaParser#conditional_insert_clause.
    def enterConditional_insert_clause(self, ctx:HanaParser.Conditional_insert_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#conditional_insert_clause.
    def exitConditional_insert_clause(self, ctx:HanaParser.Conditional_insert_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#conditional_insert_when_part.
    def enterConditional_insert_when_part(self, ctx:HanaParser.Conditional_insert_when_partContext):
        pass

    # Exit a parse tree produced by HanaParser#conditional_insert_when_part.
    def exitConditional_insert_when_part(self, ctx:HanaParser.Conditional_insert_when_partContext):
        pass


    # Enter a parse tree produced by HanaParser#conditional_insert_else_part.
    def enterConditional_insert_else_part(self, ctx:HanaParser.Conditional_insert_else_partContext):
        pass

    # Exit a parse tree produced by HanaParser#conditional_insert_else_part.
    def exitConditional_insert_else_part(self, ctx:HanaParser.Conditional_insert_else_partContext):
        pass


    # Enter a parse tree produced by HanaParser#insert_into_clause.
    def enterInsert_into_clause(self, ctx:HanaParser.Insert_into_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#insert_into_clause.
    def exitInsert_into_clause(self, ctx:HanaParser.Insert_into_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#values_clause.
    def enterValues_clause(self, ctx:HanaParser.Values_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#values_clause.
    def exitValues_clause(self, ctx:HanaParser.Values_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#merge_statement.
    def enterMerge_statement(self, ctx:HanaParser.Merge_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#merge_statement.
    def exitMerge_statement(self, ctx:HanaParser.Merge_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#merge_update_clause.
    def enterMerge_update_clause(self, ctx:HanaParser.Merge_update_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#merge_update_clause.
    def exitMerge_update_clause(self, ctx:HanaParser.Merge_update_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#merge_element.
    def enterMerge_element(self, ctx:HanaParser.Merge_elementContext):
        pass

    # Exit a parse tree produced by HanaParser#merge_element.
    def exitMerge_element(self, ctx:HanaParser.Merge_elementContext):
        pass


    # Enter a parse tree produced by HanaParser#merge_update_delete_part.
    def enterMerge_update_delete_part(self, ctx:HanaParser.Merge_update_delete_partContext):
        pass

    # Exit a parse tree produced by HanaParser#merge_update_delete_part.
    def exitMerge_update_delete_part(self, ctx:HanaParser.Merge_update_delete_partContext):
        pass


    # Enter a parse tree produced by HanaParser#merge_insert_clause.
    def enterMerge_insert_clause(self, ctx:HanaParser.Merge_insert_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#merge_insert_clause.
    def exitMerge_insert_clause(self, ctx:HanaParser.Merge_insert_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#selected_tableview.
    def enterSelected_tableview(self, ctx:HanaParser.Selected_tableviewContext):
        pass

    # Exit a parse tree produced by HanaParser#selected_tableview.
    def exitSelected_tableview(self, ctx:HanaParser.Selected_tableviewContext):
        pass


    # Enter a parse tree produced by HanaParser#lock_table_statement.
    def enterLock_table_statement(self, ctx:HanaParser.Lock_table_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#lock_table_statement.
    def exitLock_table_statement(self, ctx:HanaParser.Lock_table_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#wait_nowait_part.
    def enterWait_nowait_part(self, ctx:HanaParser.Wait_nowait_partContext):
        pass

    # Exit a parse tree produced by HanaParser#wait_nowait_part.
    def exitWait_nowait_part(self, ctx:HanaParser.Wait_nowait_partContext):
        pass


    # Enter a parse tree produced by HanaParser#lock_table_element.
    def enterLock_table_element(self, ctx:HanaParser.Lock_table_elementContext):
        pass

    # Exit a parse tree produced by HanaParser#lock_table_element.
    def exitLock_table_element(self, ctx:HanaParser.Lock_table_elementContext):
        pass


    # Enter a parse tree produced by HanaParser#lock_mode.
    def enterLock_mode(self, ctx:HanaParser.Lock_modeContext):
        pass

    # Exit a parse tree produced by HanaParser#lock_mode.
    def exitLock_mode(self, ctx:HanaParser.Lock_modeContext):
        pass


    # Enter a parse tree produced by HanaParser#general_table_ref.
    def enterGeneral_table_ref(self, ctx:HanaParser.General_table_refContext):
        pass

    # Exit a parse tree produced by HanaParser#general_table_ref.
    def exitGeneral_table_ref(self, ctx:HanaParser.General_table_refContext):
        pass


    # Enter a parse tree produced by HanaParser#static_returning_clause.
    def enterStatic_returning_clause(self, ctx:HanaParser.Static_returning_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#static_returning_clause.
    def exitStatic_returning_clause(self, ctx:HanaParser.Static_returning_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#error_logging_clause.
    def enterError_logging_clause(self, ctx:HanaParser.Error_logging_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#error_logging_clause.
    def exitError_logging_clause(self, ctx:HanaParser.Error_logging_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#error_logging_into_part.
    def enterError_logging_into_part(self, ctx:HanaParser.Error_logging_into_partContext):
        pass

    # Exit a parse tree produced by HanaParser#error_logging_into_part.
    def exitError_logging_into_part(self, ctx:HanaParser.Error_logging_into_partContext):
        pass


    # Enter a parse tree produced by HanaParser#error_logging_reject_part.
    def enterError_logging_reject_part(self, ctx:HanaParser.Error_logging_reject_partContext):
        pass

    # Exit a parse tree produced by HanaParser#error_logging_reject_part.
    def exitError_logging_reject_part(self, ctx:HanaParser.Error_logging_reject_partContext):
        pass


    # Enter a parse tree produced by HanaParser#dml_table_expression_clause.
    def enterDml_table_expression_clause(self, ctx:HanaParser.Dml_table_expression_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#dml_table_expression_clause.
    def exitDml_table_expression_clause(self, ctx:HanaParser.Dml_table_expression_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#table_collection_expression.
    def enterTable_collection_expression(self, ctx:HanaParser.Table_collection_expressionContext):
        pass

    # Exit a parse tree produced by HanaParser#table_collection_expression.
    def exitTable_collection_expression(self, ctx:HanaParser.Table_collection_expressionContext):
        pass


    # Enter a parse tree produced by HanaParser#subquery_restriction_clause.
    def enterSubquery_restriction_clause(self, ctx:HanaParser.Subquery_restriction_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#subquery_restriction_clause.
    def exitSubquery_restriction_clause(self, ctx:HanaParser.Subquery_restriction_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#sample_clause.
    def enterSample_clause(self, ctx:HanaParser.Sample_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#sample_clause.
    def exitSample_clause(self, ctx:HanaParser.Sample_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#seed_part.
    def enterSeed_part(self, ctx:HanaParser.Seed_partContext):
        pass

    # Exit a parse tree produced by HanaParser#seed_part.
    def exitSeed_part(self, ctx:HanaParser.Seed_partContext):
        pass


    # Enter a parse tree produced by HanaParser#cursor_expression.
    def enterCursor_expression(self, ctx:HanaParser.Cursor_expressionContext):
        pass

    # Exit a parse tree produced by HanaParser#cursor_expression.
    def exitCursor_expression(self, ctx:HanaParser.Cursor_expressionContext):
        pass


    # Enter a parse tree produced by HanaParser#expression_list.
    def enterExpression_list(self, ctx:HanaParser.Expression_listContext):
        pass

    # Exit a parse tree produced by HanaParser#expression_list.
    def exitExpression_list(self, ctx:HanaParser.Expression_listContext):
        pass


    # Enter a parse tree produced by HanaParser#condition.
    def enterCondition(self, ctx:HanaParser.ConditionContext):
        pass

    # Exit a parse tree produced by HanaParser#condition.
    def exitCondition(self, ctx:HanaParser.ConditionContext):
        pass


    # Enter a parse tree produced by HanaParser#condition_wrapper.
    def enterCondition_wrapper(self, ctx:HanaParser.Condition_wrapperContext):
        pass

    # Exit a parse tree produced by HanaParser#condition_wrapper.
    def exitCondition_wrapper(self, ctx:HanaParser.Condition_wrapperContext):
        pass


    # Enter a parse tree produced by HanaParser#condition_.
    def enterCondition_(self, ctx:HanaParser.Condition_Context):
        pass

    # Exit a parse tree produced by HanaParser#condition_.
    def exitCondition_(self, ctx:HanaParser.Condition_Context):
        pass


    # Enter a parse tree produced by HanaParser#predicate.
    def enterPredicate(self, ctx:HanaParser.PredicateContext):
        pass

    # Exit a parse tree produced by HanaParser#predicate.
    def exitPredicate(self, ctx:HanaParser.PredicateContext):
        pass


    # Enter a parse tree produced by HanaParser#comparison_predicate.
    def enterComparison_predicate(self, ctx:HanaParser.Comparison_predicateContext):
        pass

    # Exit a parse tree produced by HanaParser#comparison_predicate.
    def exitComparison_predicate(self, ctx:HanaParser.Comparison_predicateContext):
        pass


    # Enter a parse tree produced by HanaParser#relational_operator.
    def enterRelational_operator(self, ctx:HanaParser.Relational_operatorContext):
        pass

    # Exit a parse tree produced by HanaParser#relational_operator.
    def exitRelational_operator(self, ctx:HanaParser.Relational_operatorContext):
        pass


    # Enter a parse tree produced by HanaParser#range_predicate.
    def enterRange_predicate(self, ctx:HanaParser.Range_predicateContext):
        pass

    # Exit a parse tree produced by HanaParser#range_predicate.
    def exitRange_predicate(self, ctx:HanaParser.Range_predicateContext):
        pass


    # Enter a parse tree produced by HanaParser#in_predicate.
    def enterIn_predicate(self, ctx:HanaParser.In_predicateContext):
        pass

    # Exit a parse tree produced by HanaParser#in_predicate.
    def exitIn_predicate(self, ctx:HanaParser.In_predicateContext):
        pass


    # Enter a parse tree produced by HanaParser#exist_predicate.
    def enterExist_predicate(self, ctx:HanaParser.Exist_predicateContext):
        pass

    # Exit a parse tree produced by HanaParser#exist_predicate.
    def exitExist_predicate(self, ctx:HanaParser.Exist_predicateContext):
        pass


    # Enter a parse tree produced by HanaParser#like_predicate.
    def enterLike_predicate(self, ctx:HanaParser.Like_predicateContext):
        pass

    # Exit a parse tree produced by HanaParser#like_predicate.
    def exitLike_predicate(self, ctx:HanaParser.Like_predicateContext):
        pass


    # Enter a parse tree produced by HanaParser#null_predicate.
    def enterNull_predicate(self, ctx:HanaParser.Null_predicateContext):
        pass

    # Exit a parse tree produced by HanaParser#null_predicate.
    def exitNull_predicate(self, ctx:HanaParser.Null_predicateContext):
        pass


    # Enter a parse tree produced by HanaParser#expression__list.
    def enterExpression__list(self, ctx:HanaParser.Expression__listContext):
        pass

    # Exit a parse tree produced by HanaParser#expression__list.
    def exitExpression__list(self, ctx:HanaParser.Expression__listContext):
        pass


    # Enter a parse tree produced by HanaParser#expression_.
    def enterExpression_(self, ctx:HanaParser.Expression_Context):
        pass

    # Exit a parse tree produced by HanaParser#expression_.
    def exitExpression_(self, ctx:HanaParser.Expression_Context):
        pass


    # Enter a parse tree produced by HanaParser#correlation_name.
    def enterCorrelation_name(self, ctx:HanaParser.Correlation_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#correlation_name.
    def exitCorrelation_name(self, ctx:HanaParser.Correlation_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#operator.
    def enterOperator(self, ctx:HanaParser.OperatorContext):
        pass

    # Exit a parse tree produced by HanaParser#operator.
    def exitOperator(self, ctx:HanaParser.OperatorContext):
        pass


    # Enter a parse tree produced by HanaParser#case_expression_.
    def enterCase_expression_(self, ctx:HanaParser.Case_expression_Context):
        pass

    # Exit a parse tree produced by HanaParser#case_expression_.
    def exitCase_expression_(self, ctx:HanaParser.Case_expression_Context):
        pass


    # Enter a parse tree produced by HanaParser#simple_case_expression_.
    def enterSimple_case_expression_(self, ctx:HanaParser.Simple_case_expression_Context):
        pass

    # Exit a parse tree produced by HanaParser#simple_case_expression_.
    def exitSimple_case_expression_(self, ctx:HanaParser.Simple_case_expression_Context):
        pass


    # Enter a parse tree produced by HanaParser#search_case_expression_.
    def enterSearch_case_expression_(self, ctx:HanaParser.Search_case_expression_Context):
        pass

    # Exit a parse tree produced by HanaParser#search_case_expression_.
    def exitSearch_case_expression_(self, ctx:HanaParser.Search_case_expression_Context):
        pass


    # Enter a parse tree produced by HanaParser#function_expression_.
    def enterFunction_expression_(self, ctx:HanaParser.Function_expression_Context):
        pass

    # Exit a parse tree produced by HanaParser#function_expression_.
    def exitFunction_expression_(self, ctx:HanaParser.Function_expression_Context):
        pass


    # Enter a parse tree produced by HanaParser#aggregate_expression_.
    def enterAggregate_expression_(self, ctx:HanaParser.Aggregate_expression_Context):
        pass

    # Exit a parse tree produced by HanaParser#aggregate_expression_.
    def exitAggregate_expression_(self, ctx:HanaParser.Aggregate_expression_Context):
        pass


    # Enter a parse tree produced by HanaParser#agg_name.
    def enterAgg_name(self, ctx:HanaParser.Agg_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#agg_name.
    def exitAgg_name(self, ctx:HanaParser.Agg_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#delimiter.
    def enterDelimiter(self, ctx:HanaParser.DelimiterContext):
        pass

    # Exit a parse tree produced by HanaParser#delimiter.
    def exitDelimiter(self, ctx:HanaParser.DelimiterContext):
        pass


    # Enter a parse tree produced by HanaParser#aggregate_order_by_clause.
    def enterAggregate_order_by_clause(self, ctx:HanaParser.Aggregate_order_by_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#aggregate_order_by_clause.
    def exitAggregate_order_by_clause(self, ctx:HanaParser.Aggregate_order_by_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#expression.
    def enterExpression(self, ctx:HanaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by HanaParser#expression.
    def exitExpression(self, ctx:HanaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by HanaParser#expression_wrapper.
    def enterExpression_wrapper(self, ctx:HanaParser.Expression_wrapperContext):
        pass

    # Exit a parse tree produced by HanaParser#expression_wrapper.
    def exitExpression_wrapper(self, ctx:HanaParser.Expression_wrapperContext):
        pass


    # Enter a parse tree produced by HanaParser#logical_and_expression.
    def enterLogical_and_expression(self, ctx:HanaParser.Logical_and_expressionContext):
        pass

    # Exit a parse tree produced by HanaParser#logical_and_expression.
    def exitLogical_and_expression(self, ctx:HanaParser.Logical_and_expressionContext):
        pass


    # Enter a parse tree produced by HanaParser#negated_expression.
    def enterNegated_expression(self, ctx:HanaParser.Negated_expressionContext):
        pass

    # Exit a parse tree produced by HanaParser#negated_expression.
    def exitNegated_expression(self, ctx:HanaParser.Negated_expressionContext):
        pass


    # Enter a parse tree produced by HanaParser#equality_expression.
    def enterEquality_expression(self, ctx:HanaParser.Equality_expressionContext):
        pass

    # Exit a parse tree produced by HanaParser#equality_expression.
    def exitEquality_expression(self, ctx:HanaParser.Equality_expressionContext):
        pass


    # Enter a parse tree produced by HanaParser#multiset_expression.
    def enterMultiset_expression(self, ctx:HanaParser.Multiset_expressionContext):
        pass

    # Exit a parse tree produced by HanaParser#multiset_expression.
    def exitMultiset_expression(self, ctx:HanaParser.Multiset_expressionContext):
        pass


    # Enter a parse tree produced by HanaParser#multiset_type.
    def enterMultiset_type(self, ctx:HanaParser.Multiset_typeContext):
        pass

    # Exit a parse tree produced by HanaParser#multiset_type.
    def exitMultiset_type(self, ctx:HanaParser.Multiset_typeContext):
        pass


    # Enter a parse tree produced by HanaParser#relational_expression.
    def enterRelational_expression(self, ctx:HanaParser.Relational_expressionContext):
        pass

    # Exit a parse tree produced by HanaParser#relational_expression.
    def exitRelational_expression(self, ctx:HanaParser.Relational_expressionContext):
        pass


    # Enter a parse tree produced by HanaParser#relational_expression_operator.
    def enterRelational_expression_operator(self, ctx:HanaParser.Relational_expression_operatorContext):
        pass

    # Exit a parse tree produced by HanaParser#relational_expression_operator.
    def exitRelational_expression_operator(self, ctx:HanaParser.Relational_expression_operatorContext):
        pass


    # Enter a parse tree produced by HanaParser#compound_expression.
    def enterCompound_expression(self, ctx:HanaParser.Compound_expressionContext):
        pass

    # Exit a parse tree produced by HanaParser#compound_expression.
    def exitCompound_expression(self, ctx:HanaParser.Compound_expressionContext):
        pass


    # Enter a parse tree produced by HanaParser#like_type.
    def enterLike_type(self, ctx:HanaParser.Like_typeContext):
        pass

    # Exit a parse tree produced by HanaParser#like_type.
    def exitLike_type(self, ctx:HanaParser.Like_typeContext):
        pass


    # Enter a parse tree produced by HanaParser#like_escape_part.
    def enterLike_escape_part(self, ctx:HanaParser.Like_escape_partContext):
        pass

    # Exit a parse tree produced by HanaParser#like_escape_part.
    def exitLike_escape_part(self, ctx:HanaParser.Like_escape_partContext):
        pass


    # Enter a parse tree produced by HanaParser#in_elements.
    def enterIn_elements(self, ctx:HanaParser.In_elementsContext):
        pass

    # Exit a parse tree produced by HanaParser#in_elements.
    def exitIn_elements(self, ctx:HanaParser.In_elementsContext):
        pass


    # Enter a parse tree produced by HanaParser#between_elements.
    def enterBetween_elements(self, ctx:HanaParser.Between_elementsContext):
        pass

    # Exit a parse tree produced by HanaParser#between_elements.
    def exitBetween_elements(self, ctx:HanaParser.Between_elementsContext):
        pass


    # Enter a parse tree produced by HanaParser#concatenation.
    def enterConcatenation(self, ctx:HanaParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by HanaParser#concatenation.
    def exitConcatenation(self, ctx:HanaParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by HanaParser#concatenation_wrapper.
    def enterConcatenation_wrapper(self, ctx:HanaParser.Concatenation_wrapperContext):
        pass

    # Exit a parse tree produced by HanaParser#concatenation_wrapper.
    def exitConcatenation_wrapper(self, ctx:HanaParser.Concatenation_wrapperContext):
        pass


    # Enter a parse tree produced by HanaParser#additive_expression.
    def enterAdditive_expression(self, ctx:HanaParser.Additive_expressionContext):
        pass

    # Exit a parse tree produced by HanaParser#additive_expression.
    def exitAdditive_expression(self, ctx:HanaParser.Additive_expressionContext):
        pass


    # Enter a parse tree produced by HanaParser#multiply_expression.
    def enterMultiply_expression(self, ctx:HanaParser.Multiply_expressionContext):
        pass

    # Exit a parse tree produced by HanaParser#multiply_expression.
    def exitMultiply_expression(self, ctx:HanaParser.Multiply_expressionContext):
        pass


    # Enter a parse tree produced by HanaParser#datetime_expression.
    def enterDatetime_expression(self, ctx:HanaParser.Datetime_expressionContext):
        pass

    # Exit a parse tree produced by HanaParser#datetime_expression.
    def exitDatetime_expression(self, ctx:HanaParser.Datetime_expressionContext):
        pass


    # Enter a parse tree produced by HanaParser#interval_expression.
    def enterInterval_expression(self, ctx:HanaParser.Interval_expressionContext):
        pass

    # Exit a parse tree produced by HanaParser#interval_expression.
    def exitInterval_expression(self, ctx:HanaParser.Interval_expressionContext):
        pass


    # Enter a parse tree produced by HanaParser#model_expression.
    def enterModel_expression(self, ctx:HanaParser.Model_expressionContext):
        pass

    # Exit a parse tree produced by HanaParser#model_expression.
    def exitModel_expression(self, ctx:HanaParser.Model_expressionContext):
        pass


    # Enter a parse tree produced by HanaParser#model_expression_element.
    def enterModel_expression_element(self, ctx:HanaParser.Model_expression_elementContext):
        pass

    # Exit a parse tree produced by HanaParser#model_expression_element.
    def exitModel_expression_element(self, ctx:HanaParser.Model_expression_elementContext):
        pass


    # Enter a parse tree produced by HanaParser#single_column_for_loop.
    def enterSingle_column_for_loop(self, ctx:HanaParser.Single_column_for_loopContext):
        pass

    # Exit a parse tree produced by HanaParser#single_column_for_loop.
    def exitSingle_column_for_loop(self, ctx:HanaParser.Single_column_for_loopContext):
        pass


    # Enter a parse tree produced by HanaParser#for_like_part.
    def enterFor_like_part(self, ctx:HanaParser.For_like_partContext):
        pass

    # Exit a parse tree produced by HanaParser#for_like_part.
    def exitFor_like_part(self, ctx:HanaParser.For_like_partContext):
        pass


    # Enter a parse tree produced by HanaParser#for_increment_decrement_type.
    def enterFor_increment_decrement_type(self, ctx:HanaParser.For_increment_decrement_typeContext):
        pass

    # Exit a parse tree produced by HanaParser#for_increment_decrement_type.
    def exitFor_increment_decrement_type(self, ctx:HanaParser.For_increment_decrement_typeContext):
        pass


    # Enter a parse tree produced by HanaParser#multi_column_for_loop.
    def enterMulti_column_for_loop(self, ctx:HanaParser.Multi_column_for_loopContext):
        pass

    # Exit a parse tree produced by HanaParser#multi_column_for_loop.
    def exitMulti_column_for_loop(self, ctx:HanaParser.Multi_column_for_loopContext):
        pass


    # Enter a parse tree produced by HanaParser#unary_expression.
    def enterUnary_expression(self, ctx:HanaParser.Unary_expressionContext):
        pass

    # Exit a parse tree produced by HanaParser#unary_expression.
    def exitUnary_expression(self, ctx:HanaParser.Unary_expressionContext):
        pass


    # Enter a parse tree produced by HanaParser#case_statement.
    def enterCase_statement(self, ctx:HanaParser.Case_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#case_statement.
    def exitCase_statement(self, ctx:HanaParser.Case_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#simple_case_statement.
    def enterSimple_case_statement(self, ctx:HanaParser.Simple_case_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#simple_case_statement.
    def exitSimple_case_statement(self, ctx:HanaParser.Simple_case_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#simple_case_when_part.
    def enterSimple_case_when_part(self, ctx:HanaParser.Simple_case_when_partContext):
        pass

    # Exit a parse tree produced by HanaParser#simple_case_when_part.
    def exitSimple_case_when_part(self, ctx:HanaParser.Simple_case_when_partContext):
        pass


    # Enter a parse tree produced by HanaParser#searched_case_statement.
    def enterSearched_case_statement(self, ctx:HanaParser.Searched_case_statementContext):
        pass

    # Exit a parse tree produced by HanaParser#searched_case_statement.
    def exitSearched_case_statement(self, ctx:HanaParser.Searched_case_statementContext):
        pass


    # Enter a parse tree produced by HanaParser#searched_case_when_part.
    def enterSearched_case_when_part(self, ctx:HanaParser.Searched_case_when_partContext):
        pass

    # Exit a parse tree produced by HanaParser#searched_case_when_part.
    def exitSearched_case_when_part(self, ctx:HanaParser.Searched_case_when_partContext):
        pass


    # Enter a parse tree produced by HanaParser#case_else_part.
    def enterCase_else_part(self, ctx:HanaParser.Case_else_partContext):
        pass

    # Exit a parse tree produced by HanaParser#case_else_part.
    def exitCase_else_part(self, ctx:HanaParser.Case_else_partContext):
        pass


    # Enter a parse tree produced by HanaParser#atom.
    def enterAtom(self, ctx:HanaParser.AtomContext):
        pass

    # Exit a parse tree produced by HanaParser#atom.
    def exitAtom(self, ctx:HanaParser.AtomContext):
        pass


    # Enter a parse tree produced by HanaParser#expression_or_vector.
    def enterExpression_or_vector(self, ctx:HanaParser.Expression_or_vectorContext):
        pass

    # Exit a parse tree produced by HanaParser#expression_or_vector.
    def exitExpression_or_vector(self, ctx:HanaParser.Expression_or_vectorContext):
        pass


    # Enter a parse tree produced by HanaParser#vector_expr.
    def enterVector_expr(self, ctx:HanaParser.Vector_exprContext):
        pass

    # Exit a parse tree produced by HanaParser#vector_expr.
    def exitVector_expr(self, ctx:HanaParser.Vector_exprContext):
        pass


    # Enter a parse tree produced by HanaParser#quantified_expression.
    def enterQuantified_expression(self, ctx:HanaParser.Quantified_expressionContext):
        pass

    # Exit a parse tree produced by HanaParser#quantified_expression.
    def exitQuantified_expression(self, ctx:HanaParser.Quantified_expressionContext):
        pass


    # Enter a parse tree produced by HanaParser#standard_function.
    def enterStandard_function(self, ctx:HanaParser.Standard_functionContext):
        pass

    # Exit a parse tree produced by HanaParser#standard_function.
    def exitStandard_function(self, ctx:HanaParser.Standard_functionContext):
        pass


    # Enter a parse tree produced by HanaParser#over_clause_keyword.
    def enterOver_clause_keyword(self, ctx:HanaParser.Over_clause_keywordContext):
        pass

    # Exit a parse tree produced by HanaParser#over_clause_keyword.
    def exitOver_clause_keyword(self, ctx:HanaParser.Over_clause_keywordContext):
        pass


    # Enter a parse tree produced by HanaParser#within_or_over_clause_keyword.
    def enterWithin_or_over_clause_keyword(self, ctx:HanaParser.Within_or_over_clause_keywordContext):
        pass

    # Exit a parse tree produced by HanaParser#within_or_over_clause_keyword.
    def exitWithin_or_over_clause_keyword(self, ctx:HanaParser.Within_or_over_clause_keywordContext):
        pass


    # Enter a parse tree produced by HanaParser#standard_prediction_function_keyword.
    def enterStandard_prediction_function_keyword(self, ctx:HanaParser.Standard_prediction_function_keywordContext):
        pass

    # Exit a parse tree produced by HanaParser#standard_prediction_function_keyword.
    def exitStandard_prediction_function_keyword(self, ctx:HanaParser.Standard_prediction_function_keywordContext):
        pass


    # Enter a parse tree produced by HanaParser#over_clause.
    def enterOver_clause(self, ctx:HanaParser.Over_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#over_clause.
    def exitOver_clause(self, ctx:HanaParser.Over_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#windowing_clause.
    def enterWindowing_clause(self, ctx:HanaParser.Windowing_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#windowing_clause.
    def exitWindowing_clause(self, ctx:HanaParser.Windowing_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#windowing_type.
    def enterWindowing_type(self, ctx:HanaParser.Windowing_typeContext):
        pass

    # Exit a parse tree produced by HanaParser#windowing_type.
    def exitWindowing_type(self, ctx:HanaParser.Windowing_typeContext):
        pass


    # Enter a parse tree produced by HanaParser#windowing_elements.
    def enterWindowing_elements(self, ctx:HanaParser.Windowing_elementsContext):
        pass

    # Exit a parse tree produced by HanaParser#windowing_elements.
    def exitWindowing_elements(self, ctx:HanaParser.Windowing_elementsContext):
        pass


    # Enter a parse tree produced by HanaParser#using_clause.
    def enterUsing_clause(self, ctx:HanaParser.Using_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#using_clause.
    def exitUsing_clause(self, ctx:HanaParser.Using_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#using_element.
    def enterUsing_element(self, ctx:HanaParser.Using_elementContext):
        pass

    # Exit a parse tree produced by HanaParser#using_element.
    def exitUsing_element(self, ctx:HanaParser.Using_elementContext):
        pass


    # Enter a parse tree produced by HanaParser#collect_order_by_part.
    def enterCollect_order_by_part(self, ctx:HanaParser.Collect_order_by_partContext):
        pass

    # Exit a parse tree produced by HanaParser#collect_order_by_part.
    def exitCollect_order_by_part(self, ctx:HanaParser.Collect_order_by_partContext):
        pass


    # Enter a parse tree produced by HanaParser#within_or_over_part.
    def enterWithin_or_over_part(self, ctx:HanaParser.Within_or_over_partContext):
        pass

    # Exit a parse tree produced by HanaParser#within_or_over_part.
    def exitWithin_or_over_part(self, ctx:HanaParser.Within_or_over_partContext):
        pass


    # Enter a parse tree produced by HanaParser#cost_matrix_clause.
    def enterCost_matrix_clause(self, ctx:HanaParser.Cost_matrix_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#cost_matrix_clause.
    def exitCost_matrix_clause(self, ctx:HanaParser.Cost_matrix_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#xml_passing_clause.
    def enterXml_passing_clause(self, ctx:HanaParser.Xml_passing_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#xml_passing_clause.
    def exitXml_passing_clause(self, ctx:HanaParser.Xml_passing_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#xml_attributes_clause.
    def enterXml_attributes_clause(self, ctx:HanaParser.Xml_attributes_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#xml_attributes_clause.
    def exitXml_attributes_clause(self, ctx:HanaParser.Xml_attributes_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#xml_namespaces_clause.
    def enterXml_namespaces_clause(self, ctx:HanaParser.Xml_namespaces_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#xml_namespaces_clause.
    def exitXml_namespaces_clause(self, ctx:HanaParser.Xml_namespaces_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#xml_table_column.
    def enterXml_table_column(self, ctx:HanaParser.Xml_table_columnContext):
        pass

    # Exit a parse tree produced by HanaParser#xml_table_column.
    def exitXml_table_column(self, ctx:HanaParser.Xml_table_columnContext):
        pass


    # Enter a parse tree produced by HanaParser#xml_general_default_part.
    def enterXml_general_default_part(self, ctx:HanaParser.Xml_general_default_partContext):
        pass

    # Exit a parse tree produced by HanaParser#xml_general_default_part.
    def exitXml_general_default_part(self, ctx:HanaParser.Xml_general_default_partContext):
        pass


    # Enter a parse tree produced by HanaParser#xml_multiuse_expression_element.
    def enterXml_multiuse_expression_element(self, ctx:HanaParser.Xml_multiuse_expression_elementContext):
        pass

    # Exit a parse tree produced by HanaParser#xml_multiuse_expression_element.
    def exitXml_multiuse_expression_element(self, ctx:HanaParser.Xml_multiuse_expression_elementContext):
        pass


    # Enter a parse tree produced by HanaParser#xmlroot_param_version_part.
    def enterXmlroot_param_version_part(self, ctx:HanaParser.Xmlroot_param_version_partContext):
        pass

    # Exit a parse tree produced by HanaParser#xmlroot_param_version_part.
    def exitXmlroot_param_version_part(self, ctx:HanaParser.Xmlroot_param_version_partContext):
        pass


    # Enter a parse tree produced by HanaParser#xmlroot_param_standalone_part.
    def enterXmlroot_param_standalone_part(self, ctx:HanaParser.Xmlroot_param_standalone_partContext):
        pass

    # Exit a parse tree produced by HanaParser#xmlroot_param_standalone_part.
    def exitXmlroot_param_standalone_part(self, ctx:HanaParser.Xmlroot_param_standalone_partContext):
        pass


    # Enter a parse tree produced by HanaParser#xmlserialize_param_enconding_part.
    def enterXmlserialize_param_enconding_part(self, ctx:HanaParser.Xmlserialize_param_enconding_partContext):
        pass

    # Exit a parse tree produced by HanaParser#xmlserialize_param_enconding_part.
    def exitXmlserialize_param_enconding_part(self, ctx:HanaParser.Xmlserialize_param_enconding_partContext):
        pass


    # Enter a parse tree produced by HanaParser#xmlserialize_param_version_part.
    def enterXmlserialize_param_version_part(self, ctx:HanaParser.Xmlserialize_param_version_partContext):
        pass

    # Exit a parse tree produced by HanaParser#xmlserialize_param_version_part.
    def exitXmlserialize_param_version_part(self, ctx:HanaParser.Xmlserialize_param_version_partContext):
        pass


    # Enter a parse tree produced by HanaParser#xmlserialize_param_ident_part.
    def enterXmlserialize_param_ident_part(self, ctx:HanaParser.Xmlserialize_param_ident_partContext):
        pass

    # Exit a parse tree produced by HanaParser#xmlserialize_param_ident_part.
    def exitXmlserialize_param_ident_part(self, ctx:HanaParser.Xmlserialize_param_ident_partContext):
        pass


    # Enter a parse tree produced by HanaParser#sql_plus_command.
    def enterSql_plus_command(self, ctx:HanaParser.Sql_plus_commandContext):
        pass

    # Exit a parse tree produced by HanaParser#sql_plus_command.
    def exitSql_plus_command(self, ctx:HanaParser.Sql_plus_commandContext):
        pass


    # Enter a parse tree produced by HanaParser#whenever_command.
    def enterWhenever_command(self, ctx:HanaParser.Whenever_commandContext):
        pass

    # Exit a parse tree produced by HanaParser#whenever_command.
    def exitWhenever_command(self, ctx:HanaParser.Whenever_commandContext):
        pass


    # Enter a parse tree produced by HanaParser#set_command.
    def enterSet_command(self, ctx:HanaParser.Set_commandContext):
        pass

    # Exit a parse tree produced by HanaParser#set_command.
    def exitSet_command(self, ctx:HanaParser.Set_commandContext):
        pass


    # Enter a parse tree produced by HanaParser#exit_command.
    def enterExit_command(self, ctx:HanaParser.Exit_commandContext):
        pass

    # Exit a parse tree produced by HanaParser#exit_command.
    def exitExit_command(self, ctx:HanaParser.Exit_commandContext):
        pass


    # Enter a parse tree produced by HanaParser#prompt_command.
    def enterPrompt_command(self, ctx:HanaParser.Prompt_commandContext):
        pass

    # Exit a parse tree produced by HanaParser#prompt_command.
    def exitPrompt_command(self, ctx:HanaParser.Prompt_commandContext):
        pass


    # Enter a parse tree produced by HanaParser#partition_extension_clause.
    def enterPartition_extension_clause(self, ctx:HanaParser.Partition_extension_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#partition_extension_clause.
    def exitPartition_extension_clause(self, ctx:HanaParser.Partition_extension_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#column_alias.
    def enterColumn_alias(self, ctx:HanaParser.Column_aliasContext):
        pass

    # Exit a parse tree produced by HanaParser#column_alias.
    def exitColumn_alias(self, ctx:HanaParser.Column_aliasContext):
        pass


    # Enter a parse tree produced by HanaParser#table_alias.
    def enterTable_alias(self, ctx:HanaParser.Table_aliasContext):
        pass

    # Exit a parse tree produced by HanaParser#table_alias.
    def exitTable_alias(self, ctx:HanaParser.Table_aliasContext):
        pass


    # Enter a parse tree produced by HanaParser#alias_quoted_string.
    def enterAlias_quoted_string(self, ctx:HanaParser.Alias_quoted_stringContext):
        pass

    # Exit a parse tree produced by HanaParser#alias_quoted_string.
    def exitAlias_quoted_string(self, ctx:HanaParser.Alias_quoted_stringContext):
        pass


    # Enter a parse tree produced by HanaParser#where_clause.
    def enterWhere_clause(self, ctx:HanaParser.Where_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#where_clause.
    def exitWhere_clause(self, ctx:HanaParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#current_of_clause.
    def enterCurrent_of_clause(self, ctx:HanaParser.Current_of_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#current_of_clause.
    def exitCurrent_of_clause(self, ctx:HanaParser.Current_of_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#into_clause.
    def enterInto_clause(self, ctx:HanaParser.Into_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#into_clause.
    def exitInto_clause(self, ctx:HanaParser.Into_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#xml_column_name.
    def enterXml_column_name(self, ctx:HanaParser.Xml_column_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#xml_column_name.
    def exitXml_column_name(self, ctx:HanaParser.Xml_column_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#cost_class_name.
    def enterCost_class_name(self, ctx:HanaParser.Cost_class_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#cost_class_name.
    def exitCost_class_name(self, ctx:HanaParser.Cost_class_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#attribute_name.
    def enterAttribute_name(self, ctx:HanaParser.Attribute_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#attribute_name.
    def exitAttribute_name(self, ctx:HanaParser.Attribute_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#savepoint_name.
    def enterSavepoint_name(self, ctx:HanaParser.Savepoint_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#savepoint_name.
    def exitSavepoint_name(self, ctx:HanaParser.Savepoint_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#rollback_segment_name.
    def enterRollback_segment_name(self, ctx:HanaParser.Rollback_segment_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#rollback_segment_name.
    def exitRollback_segment_name(self, ctx:HanaParser.Rollback_segment_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#table_var_name.
    def enterTable_var_name(self, ctx:HanaParser.Table_var_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#table_var_name.
    def exitTable_var_name(self, ctx:HanaParser.Table_var_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#schema_name.
    def enterSchema_name(self, ctx:HanaParser.Schema_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#schema_name.
    def exitSchema_name(self, ctx:HanaParser.Schema_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#routine_name.
    def enterRoutine_name(self, ctx:HanaParser.Routine_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#routine_name.
    def exitRoutine_name(self, ctx:HanaParser.Routine_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#package_name.
    def enterPackage_name(self, ctx:HanaParser.Package_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#package_name.
    def exitPackage_name(self, ctx:HanaParser.Package_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#implementation_type_name.
    def enterImplementation_type_name(self, ctx:HanaParser.Implementation_type_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#implementation_type_name.
    def exitImplementation_type_name(self, ctx:HanaParser.Implementation_type_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#reference_model_name.
    def enterReference_model_name(self, ctx:HanaParser.Reference_model_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#reference_model_name.
    def exitReference_model_name(self, ctx:HanaParser.Reference_model_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#main_model_name.
    def enterMain_model_name(self, ctx:HanaParser.Main_model_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#main_model_name.
    def exitMain_model_name(self, ctx:HanaParser.Main_model_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#aggregate_function_name.
    def enterAggregate_function_name(self, ctx:HanaParser.Aggregate_function_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#aggregate_function_name.
    def exitAggregate_function_name(self, ctx:HanaParser.Aggregate_function_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#query_name.
    def enterQuery_name(self, ctx:HanaParser.Query_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#query_name.
    def exitQuery_name(self, ctx:HanaParser.Query_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#constraint_name.
    def enterConstraint_name(self, ctx:HanaParser.Constraint_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#constraint_name.
    def exitConstraint_name(self, ctx:HanaParser.Constraint_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#label_name.
    def enterLabel_name(self, ctx:HanaParser.Label_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#label_name.
    def exitLabel_name(self, ctx:HanaParser.Label_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#type_name.
    def enterType_name(self, ctx:HanaParser.Type_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#type_name.
    def exitType_name(self, ctx:HanaParser.Type_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#sequence_name.
    def enterSequence_name(self, ctx:HanaParser.Sequence_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#sequence_name.
    def exitSequence_name(self, ctx:HanaParser.Sequence_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#exception_name.
    def enterException_name(self, ctx:HanaParser.Exception_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#exception_name.
    def exitException_name(self, ctx:HanaParser.Exception_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#function_name.
    def enterFunction_name(self, ctx:HanaParser.Function_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#function_name.
    def exitFunction_name(self, ctx:HanaParser.Function_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#proc_name.
    def enterProc_name(self, ctx:HanaParser.Proc_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#proc_name.
    def exitProc_name(self, ctx:HanaParser.Proc_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#trigger_name.
    def enterTrigger_name(self, ctx:HanaParser.Trigger_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#trigger_name.
    def exitTrigger_name(self, ctx:HanaParser.Trigger_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#variable_name_old.
    def enterVariable_name_old(self, ctx:HanaParser.Variable_name_oldContext):
        pass

    # Exit a parse tree produced by HanaParser#variable_name_old.
    def exitVariable_name_old(self, ctx:HanaParser.Variable_name_oldContext):
        pass


    # Enter a parse tree produced by HanaParser#index_name.
    def enterIndex_name(self, ctx:HanaParser.Index_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#index_name.
    def exitIndex_name(self, ctx:HanaParser.Index_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#cursor_name_old.
    def enterCursor_name_old(self, ctx:HanaParser.Cursor_name_oldContext):
        pass

    # Exit a parse tree produced by HanaParser#cursor_name_old.
    def exitCursor_name_old(self, ctx:HanaParser.Cursor_name_oldContext):
        pass


    # Enter a parse tree produced by HanaParser#record_name.
    def enterRecord_name(self, ctx:HanaParser.Record_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#record_name.
    def exitRecord_name(self, ctx:HanaParser.Record_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#collection_name.
    def enterCollection_name(self, ctx:HanaParser.Collection_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#collection_name.
    def exitCollection_name(self, ctx:HanaParser.Collection_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#link_name.
    def enterLink_name(self, ctx:HanaParser.Link_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#link_name.
    def exitLink_name(self, ctx:HanaParser.Link_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#column_name_old.
    def enterColumn_name_old(self, ctx:HanaParser.Column_name_oldContext):
        pass

    # Exit a parse tree produced by HanaParser#column_name_old.
    def exitColumn_name_old(self, ctx:HanaParser.Column_name_oldContext):
        pass


    # Enter a parse tree produced by HanaParser#tableview_name.
    def enterTableview_name(self, ctx:HanaParser.Tableview_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#tableview_name.
    def exitTableview_name(self, ctx:HanaParser.Tableview_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#char_set_name.
    def enterChar_set_name(self, ctx:HanaParser.Char_set_nameContext):
        pass

    # Exit a parse tree produced by HanaParser#char_set_name.
    def exitChar_set_name(self, ctx:HanaParser.Char_set_nameContext):
        pass


    # Enter a parse tree produced by HanaParser#keep_clause.
    def enterKeep_clause(self, ctx:HanaParser.Keep_clauseContext):
        pass

    # Exit a parse tree produced by HanaParser#keep_clause.
    def exitKeep_clause(self, ctx:HanaParser.Keep_clauseContext):
        pass


    # Enter a parse tree produced by HanaParser#function_argument.
    def enterFunction_argument(self, ctx:HanaParser.Function_argumentContext):
        pass

    # Exit a parse tree produced by HanaParser#function_argument.
    def exitFunction_argument(self, ctx:HanaParser.Function_argumentContext):
        pass


    # Enter a parse tree produced by HanaParser#function_argument_analytic.
    def enterFunction_argument_analytic(self, ctx:HanaParser.Function_argument_analyticContext):
        pass

    # Exit a parse tree produced by HanaParser#function_argument_analytic.
    def exitFunction_argument_analytic(self, ctx:HanaParser.Function_argument_analyticContext):
        pass


    # Enter a parse tree produced by HanaParser#function_argument_modeling.
    def enterFunction_argument_modeling(self, ctx:HanaParser.Function_argument_modelingContext):
        pass

    # Exit a parse tree produced by HanaParser#function_argument_modeling.
    def exitFunction_argument_modeling(self, ctx:HanaParser.Function_argument_modelingContext):
        pass


    # Enter a parse tree produced by HanaParser#respect_or_ignore_nulls.
    def enterRespect_or_ignore_nulls(self, ctx:HanaParser.Respect_or_ignore_nullsContext):
        pass

    # Exit a parse tree produced by HanaParser#respect_or_ignore_nulls.
    def exitRespect_or_ignore_nulls(self, ctx:HanaParser.Respect_or_ignore_nullsContext):
        pass


    # Enter a parse tree produced by HanaParser#argument.
    def enterArgument(self, ctx:HanaParser.ArgumentContext):
        pass

    # Exit a parse tree produced by HanaParser#argument.
    def exitArgument(self, ctx:HanaParser.ArgumentContext):
        pass


    # Enter a parse tree produced by HanaParser#type_spec.
    def enterType_spec(self, ctx:HanaParser.Type_specContext):
        pass

    # Exit a parse tree produced by HanaParser#type_spec.
    def exitType_spec(self, ctx:HanaParser.Type_specContext):
        pass


    # Enter a parse tree produced by HanaParser#datatype.
    def enterDatatype(self, ctx:HanaParser.DatatypeContext):
        pass

    # Exit a parse tree produced by HanaParser#datatype.
    def exitDatatype(self, ctx:HanaParser.DatatypeContext):
        pass


    # Enter a parse tree produced by HanaParser#precision_part.
    def enterPrecision_part(self, ctx:HanaParser.Precision_partContext):
        pass

    # Exit a parse tree produced by HanaParser#precision_part.
    def exitPrecision_part(self, ctx:HanaParser.Precision_partContext):
        pass


    # Enter a parse tree produced by HanaParser#native_datatype_element.
    def enterNative_datatype_element(self, ctx:HanaParser.Native_datatype_elementContext):
        pass

    # Exit a parse tree produced by HanaParser#native_datatype_element.
    def exitNative_datatype_element(self, ctx:HanaParser.Native_datatype_elementContext):
        pass


    # Enter a parse tree produced by HanaParser#bind_variable.
    def enterBind_variable(self, ctx:HanaParser.Bind_variableContext):
        pass

    # Exit a parse tree produced by HanaParser#bind_variable.
    def exitBind_variable(self, ctx:HanaParser.Bind_variableContext):
        pass


    # Enter a parse tree produced by HanaParser#bind_sql_error_code.
    def enterBind_sql_error_code(self, ctx:HanaParser.Bind_sql_error_codeContext):
        pass

    # Exit a parse tree produced by HanaParser#bind_sql_error_code.
    def exitBind_sql_error_code(self, ctx:HanaParser.Bind_sql_error_codeContext):
        pass


    # Enter a parse tree produced by HanaParser#const_sql_error_code.
    def enterConst_sql_error_code(self, ctx:HanaParser.Const_sql_error_codeContext):
        pass

    # Exit a parse tree produced by HanaParser#const_sql_error_code.
    def exitConst_sql_error_code(self, ctx:HanaParser.Const_sql_error_codeContext):
        pass


    # Enter a parse tree produced by HanaParser#bind_sql_error_message.
    def enterBind_sql_error_message(self, ctx:HanaParser.Bind_sql_error_messageContext):
        pass

    # Exit a parse tree produced by HanaParser#bind_sql_error_message.
    def exitBind_sql_error_message(self, ctx:HanaParser.Bind_sql_error_messageContext):
        pass


    # Enter a parse tree produced by HanaParser#const_sql_error_message.
    def enterConst_sql_error_message(self, ctx:HanaParser.Const_sql_error_messageContext):
        pass

    # Exit a parse tree produced by HanaParser#const_sql_error_message.
    def exitConst_sql_error_message(self, ctx:HanaParser.Const_sql_error_messageContext):
        pass


    # Enter a parse tree produced by HanaParser#general_element.
    def enterGeneral_element(self, ctx:HanaParser.General_elementContext):
        pass

    # Exit a parse tree produced by HanaParser#general_element.
    def exitGeneral_element(self, ctx:HanaParser.General_elementContext):
        pass


    # Enter a parse tree produced by HanaParser#general_element_part.
    def enterGeneral_element_part(self, ctx:HanaParser.General_element_partContext):
        pass

    # Exit a parse tree produced by HanaParser#general_element_part.
    def exitGeneral_element_part(self, ctx:HanaParser.General_element_partContext):
        pass


    # Enter a parse tree produced by HanaParser#table_element.
    def enterTable_element(self, ctx:HanaParser.Table_elementContext):
        pass

    # Exit a parse tree produced by HanaParser#table_element.
    def exitTable_element(self, ctx:HanaParser.Table_elementContext):
        pass


    # Enter a parse tree produced by HanaParser#constant.
    def enterConstant(self, ctx:HanaParser.ConstantContext):
        pass

    # Exit a parse tree produced by HanaParser#constant.
    def exitConstant(self, ctx:HanaParser.ConstantContext):
        pass


    # Enter a parse tree produced by HanaParser#numeric.
    def enterNumeric(self, ctx:HanaParser.NumericContext):
        pass

    # Exit a parse tree produced by HanaParser#numeric.
    def exitNumeric(self, ctx:HanaParser.NumericContext):
        pass


    # Enter a parse tree produced by HanaParser#numeric_negative.
    def enterNumeric_negative(self, ctx:HanaParser.Numeric_negativeContext):
        pass

    # Exit a parse tree produced by HanaParser#numeric_negative.
    def exitNumeric_negative(self, ctx:HanaParser.Numeric_negativeContext):
        pass


    # Enter a parse tree produced by HanaParser#quoted_string.
    def enterQuoted_string(self, ctx:HanaParser.Quoted_stringContext):
        pass

    # Exit a parse tree produced by HanaParser#quoted_string.
    def exitQuoted_string(self, ctx:HanaParser.Quoted_stringContext):
        pass


    # Enter a parse tree produced by HanaParser#id.
    def enterId(self, ctx:HanaParser.IdContext):
        pass

    # Exit a parse tree produced by HanaParser#id.
    def exitId(self, ctx:HanaParser.IdContext):
        pass


    # Enter a parse tree produced by HanaParser#id_expression.
    def enterId_expression(self, ctx:HanaParser.Id_expressionContext):
        pass

    # Exit a parse tree produced by HanaParser#id_expression.
    def exitId_expression(self, ctx:HanaParser.Id_expressionContext):
        pass


    # Enter a parse tree produced by HanaParser#not_equal_op.
    def enterNot_equal_op(self, ctx:HanaParser.Not_equal_opContext):
        pass

    # Exit a parse tree produced by HanaParser#not_equal_op.
    def exitNot_equal_op(self, ctx:HanaParser.Not_equal_opContext):
        pass


    # Enter a parse tree produced by HanaParser#greater_than_or_equals_op.
    def enterGreater_than_or_equals_op(self, ctx:HanaParser.Greater_than_or_equals_opContext):
        pass

    # Exit a parse tree produced by HanaParser#greater_than_or_equals_op.
    def exitGreater_than_or_equals_op(self, ctx:HanaParser.Greater_than_or_equals_opContext):
        pass


    # Enter a parse tree produced by HanaParser#less_than_or_equals_op.
    def enterLess_than_or_equals_op(self, ctx:HanaParser.Less_than_or_equals_opContext):
        pass

    # Exit a parse tree produced by HanaParser#less_than_or_equals_op.
    def exitLess_than_or_equals_op(self, ctx:HanaParser.Less_than_or_equals_opContext):
        pass


    # Enter a parse tree produced by HanaParser#concatenation_op.
    def enterConcatenation_op(self, ctx:HanaParser.Concatenation_opContext):
        pass

    # Exit a parse tree produced by HanaParser#concatenation_op.
    def exitConcatenation_op(self, ctx:HanaParser.Concatenation_opContext):
        pass


    # Enter a parse tree produced by HanaParser#outer_join_sign.
    def enterOuter_join_sign(self, ctx:HanaParser.Outer_join_signContext):
        pass

    # Exit a parse tree produced by HanaParser#outer_join_sign.
    def exitOuter_join_sign(self, ctx:HanaParser.Outer_join_signContext):
        pass


    # Enter a parse tree produced by HanaParser#regular_id.
    def enterRegular_id(self, ctx:HanaParser.Regular_idContext):
        pass

    # Exit a parse tree produced by HanaParser#regular_id.
    def exitRegular_id(self, ctx:HanaParser.Regular_idContext):
        pass



del HanaParser