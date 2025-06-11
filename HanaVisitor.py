# Generated from C:/Users/harip/Desktop/SQL-vs/antlr-saphana/Hana.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .HanaParser import HanaParser
else:
    from HanaParser import HanaParser

# This class defines a complete generic visitor for a parse tree produced by HanaParser.

class HanaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HanaParser#swallow_to_semi.
    def visitSwallow_to_semi(self, ctx:HanaParser.Swallow_to_semiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#compilation_unit.
    def visitCompilation_unit(self, ctx:HanaParser.Compilation_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#sql_script.
    def visitSql_script(self, ctx:HanaParser.Sql_scriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#unit_statement.
    def visitUnit_statement(self, ctx:HanaParser.Unit_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#set_schema.
    def visitSet_schema(self, ctx:HanaParser.Set_schemaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#drop_procedure.
    def visitDrop_procedure(self, ctx:HanaParser.Drop_procedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#create_procedure_body.
    def visitCreate_procedure_body(self, ctx:HanaParser.Create_procedure_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#param_name.
    def visitParam_name(self, ctx:HanaParser.Param_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#param_type.
    def visitParam_type(self, ctx:HanaParser.Param_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#sql_type.
    def visitSql_type(self, ctx:HanaParser.Sql_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#table_type.
    def visitTable_type(self, ctx:HanaParser.Table_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#table_type_definition.
    def visitTable_type_definition(self, ctx:HanaParser.Table_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#column_list_definition.
    def visitColumn_list_definition(self, ctx:HanaParser.Column_list_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#column_elem.
    def visitColumn_elem(self, ctx:HanaParser.Column_elemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#column_name.
    def visitColumn_name(self, ctx:HanaParser.Column_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#data_type.
    def visitData_type(self, ctx:HanaParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#parameter.
    def visitParameter(self, ctx:HanaParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#parameter_clause.
    def visitParameter_clause(self, ctx:HanaParser.Parameter_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#lang.
    def visitLang(self, ctx:HanaParser.LangContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#security_mode.
    def visitSecurity_mode(self, ctx:HanaParser.Security_modeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#default_schema_name.
    def visitDefault_schema_name(self, ctx:HanaParser.Default_schema_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#view_name.
    def visitView_name(self, ctx:HanaParser.View_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_decl_list.
    def visitProc_decl_list(self, ctx:HanaParser.Proc_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_decl.
    def visitProc_decl(self, ctx:HanaParser.Proc_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_decl_op.
    def visitProc_decl_op(self, ctx:HanaParser.Proc_decl_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_variable.
    def visitProc_variable(self, ctx:HanaParser.Proc_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_table_variable.
    def visitProc_table_variable(self, ctx:HanaParser.Proc_table_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#variable_name_list.
    def visitVariable_name_list(self, ctx:HanaParser.Variable_name_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#array_datatype.
    def visitArray_datatype(self, ctx:HanaParser.Array_datatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#array_constructor.
    def visitArray_constructor(self, ctx:HanaParser.Array_constructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_default.
    def visitProc_default(self, ctx:HanaParser.Proc_defaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_cursor.
    def visitProc_cursor(self, ctx:HanaParser.Proc_cursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_cursor_param_list.
    def visitProc_cursor_param_list(self, ctx:HanaParser.Proc_cursor_param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#variable_name.
    def visitVariable_name(self, ctx:HanaParser.Variable_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#cursor_name.
    def visitCursor_name(self, ctx:HanaParser.Cursor_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_cursor_param.
    def visitProc_cursor_param(self, ctx:HanaParser.Proc_cursor_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_condition.
    def visitProc_condition(self, ctx:HanaParser.Proc_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#sql_error_code.
    def visitSql_error_code(self, ctx:HanaParser.Sql_error_codeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_handler_list.
    def visitProc_handler_list(self, ctx:HanaParser.Proc_handler_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_handler.
    def visitProc_handler(self, ctx:HanaParser.Proc_handlerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_condition_value_list.
    def visitProc_condition_value_list(self, ctx:HanaParser.Proc_condition_value_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_condition_value.
    def visitProc_condition_value(self, ctx:HanaParser.Proc_condition_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_stmt_list.
    def visitProc_stmt_list(self, ctx:HanaParser.Proc_stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_stmt.
    def visitProc_stmt(self, ctx:HanaParser.Proc_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_sql.
    def visitProc_sql(self, ctx:HanaParser.Proc_sqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#update_stmt.
    def visitUpdate_stmt(self, ctx:HanaParser.Update_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#insert_stmt.
    def visitInsert_stmt(self, ctx:HanaParser.Insert_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_signal.
    def visitProc_signal(self, ctx:HanaParser.Proc_signalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_resignal.
    def visitProc_resignal(self, ctx:HanaParser.Proc_resignalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#signal_value.
    def visitSignal_value(self, ctx:HanaParser.Signal_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#signal_name.
    def visitSignal_name(self, ctx:HanaParser.Signal_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#set_signal_info.
    def visitSet_signal_info(self, ctx:HanaParser.Set_signal_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#message_string.
    def visitMessage_string(self, ctx:HanaParser.Message_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_if.
    def visitProc_if(self, ctx:HanaParser.Proc_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_elsif_list.
    def visitProc_elsif_list(self, ctx:HanaParser.Proc_elsif_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_else.
    def visitProc_else(self, ctx:HanaParser.Proc_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_block.
    def visitProc_block(self, ctx:HanaParser.Proc_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_block_option.
    def visitProc_block_option(self, ctx:HanaParser.Proc_block_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_assign.
    def visitProc_assign(self, ctx:HanaParser.Proc_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_single_assign.
    def visitProc_single_assign(self, ctx:HanaParser.Proc_single_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#unnest_function.
    def visitUnnest_function(self, ctx:HanaParser.Unnest_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#table_name.
    def visitTable_name(self, ctx:HanaParser.Table_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#as_col_names.
    def visitAs_col_names(self, ctx:HanaParser.As_col_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#column_name_list.
    def visitColumn_name_list(self, ctx:HanaParser.Column_name_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_call.
    def visitProc_call(self, ctx:HanaParser.Proc_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#param_list.
    def visitParam_list(self, ctx:HanaParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_param.
    def visitProc_param(self, ctx:HanaParser.Proc_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#named_param.
    def visitNamed_param(self, ctx:HanaParser.Named_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#procedure_body.
    def visitProcedure_body(self, ctx:HanaParser.Procedure_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#procedure_body_.
    def visitProcedure_body_(self, ctx:HanaParser.Procedure_body_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#parameter_name.
    def visitParameter_name(self, ctx:HanaParser.Parameter_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#for_each_row.
    def visitFor_each_row(self, ctx:HanaParser.For_each_rowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#alter_attribute_definition.
    def visitAlter_attribute_definition(self, ctx:HanaParser.Alter_attribute_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#attribute_definition.
    def visitAttribute_definition(self, ctx:HanaParser.Attribute_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#alter_collection_clauses.
    def visitAlter_collection_clauses(self, ctx:HanaParser.Alter_collection_clausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#dependent_handling_clause.
    def visitDependent_handling_clause(self, ctx:HanaParser.Dependent_handling_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#dependent_exceptions_part.
    def visitDependent_exceptions_part(self, ctx:HanaParser.Dependent_exceptions_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#type_definition.
    def visitType_definition(self, ctx:HanaParser.Type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#object_type_def.
    def visitObject_type_def(self, ctx:HanaParser.Object_type_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#object_as_part.
    def visitObject_as_part(self, ctx:HanaParser.Object_as_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#object_under_part.
    def visitObject_under_part(self, ctx:HanaParser.Object_under_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#nested_table_type_def.
    def visitNested_table_type_def(self, ctx:HanaParser.Nested_table_type_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#sqlj_object_type.
    def visitSqlj_object_type(self, ctx:HanaParser.Sqlj_object_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#type_body.
    def visitType_body(self, ctx:HanaParser.Type_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#type_body_elements.
    def visitType_body_elements(self, ctx:HanaParser.Type_body_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#map_order_func_declaration.
    def visitMap_order_func_declaration(self, ctx:HanaParser.Map_order_func_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#subprog_decl_in_type.
    def visitSubprog_decl_in_type(self, ctx:HanaParser.Subprog_decl_in_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_decl_in_type.
    def visitProc_decl_in_type(self, ctx:HanaParser.Proc_decl_in_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#func_decl_in_type.
    def visitFunc_decl_in_type(self, ctx:HanaParser.Func_decl_in_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#constructor_declaration.
    def visitConstructor_declaration(self, ctx:HanaParser.Constructor_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#modifier_clause.
    def visitModifier_clause(self, ctx:HanaParser.Modifier_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#object_member_spec.
    def visitObject_member_spec(self, ctx:HanaParser.Object_member_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#sqlj_object_type_attr.
    def visitSqlj_object_type_attr(self, ctx:HanaParser.Sqlj_object_type_attrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#element_spec.
    def visitElement_spec(self, ctx:HanaParser.Element_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#element_spec_options.
    def visitElement_spec_options(self, ctx:HanaParser.Element_spec_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#subprogram_spec.
    def visitSubprogram_spec(self, ctx:HanaParser.Subprogram_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#type_procedure_spec.
    def visitType_procedure_spec(self, ctx:HanaParser.Type_procedure_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#type_function_spec.
    def visitType_function_spec(self, ctx:HanaParser.Type_function_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#constructor_spec.
    def visitConstructor_spec(self, ctx:HanaParser.Constructor_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#map_order_function_spec.
    def visitMap_order_function_spec(self, ctx:HanaParser.Map_order_function_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#pragma_clause.
    def visitPragma_clause(self, ctx:HanaParser.Pragma_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#pragma_elements.
    def visitPragma_elements(self, ctx:HanaParser.Pragma_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#type_elements_parameter.
    def visitType_elements_parameter(self, ctx:HanaParser.Type_elements_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#create_sequence.
    def visitCreate_sequence(self, ctx:HanaParser.Create_sequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#sequence_spec.
    def visitSequence_spec(self, ctx:HanaParser.Sequence_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#sequence_start_clause.
    def visitSequence_start_clause(self, ctx:HanaParser.Sequence_start_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#invoker_rights_clause.
    def visitInvoker_rights_clause(self, ctx:HanaParser.Invoker_rights_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#compiler_parameters_clause.
    def visitCompiler_parameters_clause(self, ctx:HanaParser.Compiler_parameters_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#call_spec.
    def visitCall_spec(self, ctx:HanaParser.Call_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#java_spec.
    def visitJava_spec(self, ctx:HanaParser.Java_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#c_spec.
    def visitC_spec(self, ctx:HanaParser.C_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#c_agent_in_clause.
    def visitC_agent_in_clause(self, ctx:HanaParser.C_agent_in_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#c_parameters_clause.
    def visitC_parameters_clause(self, ctx:HanaParser.C_parameters_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#default_value_part.
    def visitDefault_value_part(self, ctx:HanaParser.Default_value_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#declare_spec.
    def visitDeclare_spec(self, ctx:HanaParser.Declare_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#variable_declaration.
    def visitVariable_declaration(self, ctx:HanaParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#subtype_declaration.
    def visitSubtype_declaration(self, ctx:HanaParser.Subtype_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#cursor_declaration.
    def visitCursor_declaration(self, ctx:HanaParser.Cursor_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#parameter_spec.
    def visitParameter_spec(self, ctx:HanaParser.Parameter_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#exception_declaration.
    def visitException_declaration(self, ctx:HanaParser.Exception_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#pragma_declaration.
    def visitPragma_declaration(self, ctx:HanaParser.Pragma_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#record_declaration.
    def visitRecord_declaration(self, ctx:HanaParser.Record_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#record_type_dec.
    def visitRecord_type_dec(self, ctx:HanaParser.Record_type_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#field_spec.
    def visitField_spec(self, ctx:HanaParser.Field_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#record_var_dec.
    def visitRecord_var_dec(self, ctx:HanaParser.Record_var_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#table_declaration.
    def visitTable_declaration(self, ctx:HanaParser.Table_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#table_type_dec.
    def visitTable_type_dec(self, ctx:HanaParser.Table_type_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#table_indexed_by_part.
    def visitTable_indexed_by_part(self, ctx:HanaParser.Table_indexed_by_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#varray_type_def.
    def visitVarray_type_def(self, ctx:HanaParser.Varray_type_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#table_var_dec.
    def visitTable_var_dec(self, ctx:HanaParser.Table_var_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#seq_of_statements.
    def visitSeq_of_statements(self, ctx:HanaParser.Seq_of_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#label_declaration.
    def visitLabel_declaration(self, ctx:HanaParser.Label_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#statement.
    def visitStatement(self, ctx:HanaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#assignment_statement.
    def visitAssignment_statement(self, ctx:HanaParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#continue_statement.
    def visitContinue_statement(self, ctx:HanaParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#exit_statement.
    def visitExit_statement(self, ctx:HanaParser.Exit_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#goto_statement.
    def visitGoto_statement(self, ctx:HanaParser.Goto_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#if_statement.
    def visitIf_statement(self, ctx:HanaParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#elsif_part.
    def visitElsif_part(self, ctx:HanaParser.Elsif_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#else_part.
    def visitElse_part(self, ctx:HanaParser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#loop_statement.
    def visitLoop_statement(self, ctx:HanaParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#cursor_loop_param.
    def visitCursor_loop_param(self, ctx:HanaParser.Cursor_loop_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#forall_statement.
    def visitForall_statement(self, ctx:HanaParser.Forall_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#bounds_clause.
    def visitBounds_clause(self, ctx:HanaParser.Bounds_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#between_bound.
    def visitBetween_bound(self, ctx:HanaParser.Between_boundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#lower_bound.
    def visitLower_bound(self, ctx:HanaParser.Lower_boundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#upper_bound.
    def visitUpper_bound(self, ctx:HanaParser.Upper_boundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#null_statement.
    def visitNull_statement(self, ctx:HanaParser.Null_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#raise_statement.
    def visitRaise_statement(self, ctx:HanaParser.Raise_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#return_statement.
    def visitReturn_statement(self, ctx:HanaParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#function_call.
    def visitFunction_call(self, ctx:HanaParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#body.
    def visitBody(self, ctx:HanaParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#exception_clause.
    def visitException_clause(self, ctx:HanaParser.Exception_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#exception_handler.
    def visitException_handler(self, ctx:HanaParser.Exception_handlerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#trigger_block.
    def visitTrigger_block(self, ctx:HanaParser.Trigger_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#block.
    def visitBlock(self, ctx:HanaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#sql_statement.
    def visitSql_statement(self, ctx:HanaParser.Sql_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#execute_immediate.
    def visitExecute_immediate(self, ctx:HanaParser.Execute_immediateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#dynamic_returning_clause.
    def visitDynamic_returning_clause(self, ctx:HanaParser.Dynamic_returning_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#data_manipulation_language_statements.
    def visitData_manipulation_language_statements(self, ctx:HanaParser.Data_manipulation_language_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#cursor_manipulation_statements.
    def visitCursor_manipulation_statements(self, ctx:HanaParser.Cursor_manipulation_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#close_statement.
    def visitClose_statement(self, ctx:HanaParser.Close_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#open_statement.
    def visitOpen_statement(self, ctx:HanaParser.Open_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#fetch_statement.
    def visitFetch_statement(self, ctx:HanaParser.Fetch_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#open_for_statement.
    def visitOpen_for_statement(self, ctx:HanaParser.Open_for_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#transaction_control_statements.
    def visitTransaction_control_statements(self, ctx:HanaParser.Transaction_control_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#set_transaction_command.
    def visitSet_transaction_command(self, ctx:HanaParser.Set_transaction_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#set_constraint_command.
    def visitSet_constraint_command(self, ctx:HanaParser.Set_constraint_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#commit_statement.
    def visitCommit_statement(self, ctx:HanaParser.Commit_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#write_clause.
    def visitWrite_clause(self, ctx:HanaParser.Write_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#rollback_statement.
    def visitRollback_statement(self, ctx:HanaParser.Rollback_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#savepoint_statement.
    def visitSavepoint_statement(self, ctx:HanaParser.Savepoint_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#explain_statement.
    def visitExplain_statement(self, ctx:HanaParser.Explain_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#select_statement.
    def visitSelect_statement(self, ctx:HanaParser.Select_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#subquery_factoring_clause.
    def visitSubquery_factoring_clause(self, ctx:HanaParser.Subquery_factoring_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#factoring_element.
    def visitFactoring_element(self, ctx:HanaParser.Factoring_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#search_clause.
    def visitSearch_clause(self, ctx:HanaParser.Search_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#cycle_clause.
    def visitCycle_clause(self, ctx:HanaParser.Cycle_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#subquery.
    def visitSubquery(self, ctx:HanaParser.SubqueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#subquery_operation_part.
    def visitSubquery_operation_part(self, ctx:HanaParser.Subquery_operation_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#subquery_basic_elements.
    def visitSubquery_basic_elements(self, ctx:HanaParser.Subquery_basic_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#query_block.
    def visitQuery_block(self, ctx:HanaParser.Query_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#selected_element.
    def visitSelected_element(self, ctx:HanaParser.Selected_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#from_clause.
    def visitFrom_clause(self, ctx:HanaParser.From_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#select_list_elements.
    def visitSelect_list_elements(self, ctx:HanaParser.Select_list_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#table_ref_list.
    def visitTable_ref_list(self, ctx:HanaParser.Table_ref_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#table_ref.
    def visitTable_ref(self, ctx:HanaParser.Table_refContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#table_ref_aux.
    def visitTable_ref_aux(self, ctx:HanaParser.Table_ref_auxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#join_clause.
    def visitJoin_clause(self, ctx:HanaParser.Join_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#join_on_part.
    def visitJoin_on_part(self, ctx:HanaParser.Join_on_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#join_using_part.
    def visitJoin_using_part(self, ctx:HanaParser.Join_using_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#outer_join_type.
    def visitOuter_join_type(self, ctx:HanaParser.Outer_join_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#query_partition_clause.
    def visitQuery_partition_clause(self, ctx:HanaParser.Query_partition_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#flashback_query_clause.
    def visitFlashback_query_clause(self, ctx:HanaParser.Flashback_query_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#pivot_clause.
    def visitPivot_clause(self, ctx:HanaParser.Pivot_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#pivot_element.
    def visitPivot_element(self, ctx:HanaParser.Pivot_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#pivot_for_clause.
    def visitPivot_for_clause(self, ctx:HanaParser.Pivot_for_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#pivot_in_clause.
    def visitPivot_in_clause(self, ctx:HanaParser.Pivot_in_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#pivot_in_clause_element.
    def visitPivot_in_clause_element(self, ctx:HanaParser.Pivot_in_clause_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#pivot_in_clause_elements.
    def visitPivot_in_clause_elements(self, ctx:HanaParser.Pivot_in_clause_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#unpivot_clause.
    def visitUnpivot_clause(self, ctx:HanaParser.Unpivot_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#unpivot_in_clause.
    def visitUnpivot_in_clause(self, ctx:HanaParser.Unpivot_in_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#unpivot_in_elements.
    def visitUnpivot_in_elements(self, ctx:HanaParser.Unpivot_in_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#hierarchical_query_clause.
    def visitHierarchical_query_clause(self, ctx:HanaParser.Hierarchical_query_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#start_part.
    def visitStart_part(self, ctx:HanaParser.Start_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#group_by_clause.
    def visitGroup_by_clause(self, ctx:HanaParser.Group_by_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#group_by_elements.
    def visitGroup_by_elements(self, ctx:HanaParser.Group_by_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#rollup_cube_clause.
    def visitRollup_cube_clause(self, ctx:HanaParser.Rollup_cube_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#grouping_sets_clause.
    def visitGrouping_sets_clause(self, ctx:HanaParser.Grouping_sets_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#grouping_sets_elements.
    def visitGrouping_sets_elements(self, ctx:HanaParser.Grouping_sets_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#having_clause.
    def visitHaving_clause(self, ctx:HanaParser.Having_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#model_clause.
    def visitModel_clause(self, ctx:HanaParser.Model_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#cell_reference_options.
    def visitCell_reference_options(self, ctx:HanaParser.Cell_reference_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#return_rows_clause.
    def visitReturn_rows_clause(self, ctx:HanaParser.Return_rows_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#reference_model.
    def visitReference_model(self, ctx:HanaParser.Reference_modelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#main_model.
    def visitMain_model(self, ctx:HanaParser.Main_modelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#model_column_clauses.
    def visitModel_column_clauses(self, ctx:HanaParser.Model_column_clausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#model_column_partition_part.
    def visitModel_column_partition_part(self, ctx:HanaParser.Model_column_partition_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#model_column_list.
    def visitModel_column_list(self, ctx:HanaParser.Model_column_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#model_column.
    def visitModel_column(self, ctx:HanaParser.Model_columnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#model_rules_clause.
    def visitModel_rules_clause(self, ctx:HanaParser.Model_rules_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#model_rules_part.
    def visitModel_rules_part(self, ctx:HanaParser.Model_rules_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#model_rules_element.
    def visitModel_rules_element(self, ctx:HanaParser.Model_rules_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#cell_assignment.
    def visitCell_assignment(self, ctx:HanaParser.Cell_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#model_iterate_clause.
    def visitModel_iterate_clause(self, ctx:HanaParser.Model_iterate_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#until_part.
    def visitUntil_part(self, ctx:HanaParser.Until_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#order_by_clause.
    def visitOrder_by_clause(self, ctx:HanaParser.Order_by_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#order_by_elements.
    def visitOrder_by_elements(self, ctx:HanaParser.Order_by_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#for_update_clause.
    def visitFor_update_clause(self, ctx:HanaParser.For_update_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#for_update_of_part.
    def visitFor_update_of_part(self, ctx:HanaParser.For_update_of_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#for_update_options.
    def visitFor_update_options(self, ctx:HanaParser.For_update_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#update_statement.
    def visitUpdate_statement(self, ctx:HanaParser.Update_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#update_set_clause.
    def visitUpdate_set_clause(self, ctx:HanaParser.Update_set_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#column_based_update_set_clause.
    def visitColumn_based_update_set_clause(self, ctx:HanaParser.Column_based_update_set_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#delete_statement.
    def visitDelete_statement(self, ctx:HanaParser.Delete_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#insert_statement.
    def visitInsert_statement(self, ctx:HanaParser.Insert_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#declare_statement.
    def visitDeclare_statement(self, ctx:HanaParser.Declare_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#exception_statement.
    def visitException_statement(self, ctx:HanaParser.Exception_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_condition_value_.
    def visitProc_condition_value_(self, ctx:HanaParser.Proc_condition_value_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#single_table_insert.
    def visitSingle_table_insert(self, ctx:HanaParser.Single_table_insertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#multi_table_insert.
    def visitMulti_table_insert(self, ctx:HanaParser.Multi_table_insertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#multi_table_element.
    def visitMulti_table_element(self, ctx:HanaParser.Multi_table_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#conditional_insert_clause.
    def visitConditional_insert_clause(self, ctx:HanaParser.Conditional_insert_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#conditional_insert_when_part.
    def visitConditional_insert_when_part(self, ctx:HanaParser.Conditional_insert_when_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#conditional_insert_else_part.
    def visitConditional_insert_else_part(self, ctx:HanaParser.Conditional_insert_else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#insert_into_clause.
    def visitInsert_into_clause(self, ctx:HanaParser.Insert_into_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#values_clause.
    def visitValues_clause(self, ctx:HanaParser.Values_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#merge_statement.
    def visitMerge_statement(self, ctx:HanaParser.Merge_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#merge_update_clause.
    def visitMerge_update_clause(self, ctx:HanaParser.Merge_update_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#merge_element.
    def visitMerge_element(self, ctx:HanaParser.Merge_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#merge_update_delete_part.
    def visitMerge_update_delete_part(self, ctx:HanaParser.Merge_update_delete_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#merge_insert_clause.
    def visitMerge_insert_clause(self, ctx:HanaParser.Merge_insert_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#selected_tableview.
    def visitSelected_tableview(self, ctx:HanaParser.Selected_tableviewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#lock_table_statement.
    def visitLock_table_statement(self, ctx:HanaParser.Lock_table_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#wait_nowait_part.
    def visitWait_nowait_part(self, ctx:HanaParser.Wait_nowait_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#lock_table_element.
    def visitLock_table_element(self, ctx:HanaParser.Lock_table_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#lock_mode.
    def visitLock_mode(self, ctx:HanaParser.Lock_modeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#general_table_ref.
    def visitGeneral_table_ref(self, ctx:HanaParser.General_table_refContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#static_returning_clause.
    def visitStatic_returning_clause(self, ctx:HanaParser.Static_returning_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#error_logging_clause.
    def visitError_logging_clause(self, ctx:HanaParser.Error_logging_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#error_logging_into_part.
    def visitError_logging_into_part(self, ctx:HanaParser.Error_logging_into_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#error_logging_reject_part.
    def visitError_logging_reject_part(self, ctx:HanaParser.Error_logging_reject_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#dml_table_expression_clause.
    def visitDml_table_expression_clause(self, ctx:HanaParser.Dml_table_expression_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#table_collection_expression.
    def visitTable_collection_expression(self, ctx:HanaParser.Table_collection_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#subquery_restriction_clause.
    def visitSubquery_restriction_clause(self, ctx:HanaParser.Subquery_restriction_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#sample_clause.
    def visitSample_clause(self, ctx:HanaParser.Sample_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#seed_part.
    def visitSeed_part(self, ctx:HanaParser.Seed_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#cursor_expression.
    def visitCursor_expression(self, ctx:HanaParser.Cursor_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#expression_list.
    def visitExpression_list(self, ctx:HanaParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#condition.
    def visitCondition(self, ctx:HanaParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#condition_wrapper.
    def visitCondition_wrapper(self, ctx:HanaParser.Condition_wrapperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#condition_.
    def visitCondition_(self, ctx:HanaParser.Condition_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#predicate.
    def visitPredicate(self, ctx:HanaParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#comparison_predicate.
    def visitComparison_predicate(self, ctx:HanaParser.Comparison_predicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#relational_operator.
    def visitRelational_operator(self, ctx:HanaParser.Relational_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#range_predicate.
    def visitRange_predicate(self, ctx:HanaParser.Range_predicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#in_predicate.
    def visitIn_predicate(self, ctx:HanaParser.In_predicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#exist_predicate.
    def visitExist_predicate(self, ctx:HanaParser.Exist_predicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#like_predicate.
    def visitLike_predicate(self, ctx:HanaParser.Like_predicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#null_predicate.
    def visitNull_predicate(self, ctx:HanaParser.Null_predicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#expression__list.
    def visitExpression__list(self, ctx:HanaParser.Expression__listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#expression_.
    def visitExpression_(self, ctx:HanaParser.Expression_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#correlation_name.
    def visitCorrelation_name(self, ctx:HanaParser.Correlation_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#operator.
    def visitOperator(self, ctx:HanaParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#case_expression_.
    def visitCase_expression_(self, ctx:HanaParser.Case_expression_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#simple_case_expression_.
    def visitSimple_case_expression_(self, ctx:HanaParser.Simple_case_expression_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#search_case_expression_.
    def visitSearch_case_expression_(self, ctx:HanaParser.Search_case_expression_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#function_expression_.
    def visitFunction_expression_(self, ctx:HanaParser.Function_expression_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#aggregate_expression_.
    def visitAggregate_expression_(self, ctx:HanaParser.Aggregate_expression_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#agg_name.
    def visitAgg_name(self, ctx:HanaParser.Agg_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#delimiter.
    def visitDelimiter(self, ctx:HanaParser.DelimiterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#aggregate_order_by_clause.
    def visitAggregate_order_by_clause(self, ctx:HanaParser.Aggregate_order_by_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#expression.
    def visitExpression(self, ctx:HanaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#expression_wrapper.
    def visitExpression_wrapper(self, ctx:HanaParser.Expression_wrapperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#logical_and_expression.
    def visitLogical_and_expression(self, ctx:HanaParser.Logical_and_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#negated_expression.
    def visitNegated_expression(self, ctx:HanaParser.Negated_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#equality_expression.
    def visitEquality_expression(self, ctx:HanaParser.Equality_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#multiset_expression.
    def visitMultiset_expression(self, ctx:HanaParser.Multiset_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#multiset_type.
    def visitMultiset_type(self, ctx:HanaParser.Multiset_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#relational_expression.
    def visitRelational_expression(self, ctx:HanaParser.Relational_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#relational_expression_operator.
    def visitRelational_expression_operator(self, ctx:HanaParser.Relational_expression_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#compound_expression.
    def visitCompound_expression(self, ctx:HanaParser.Compound_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#like_type.
    def visitLike_type(self, ctx:HanaParser.Like_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#like_escape_part.
    def visitLike_escape_part(self, ctx:HanaParser.Like_escape_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#in_elements.
    def visitIn_elements(self, ctx:HanaParser.In_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#between_elements.
    def visitBetween_elements(self, ctx:HanaParser.Between_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#concatenation.
    def visitConcatenation(self, ctx:HanaParser.ConcatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#concatenation_wrapper.
    def visitConcatenation_wrapper(self, ctx:HanaParser.Concatenation_wrapperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#additive_expression.
    def visitAdditive_expression(self, ctx:HanaParser.Additive_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#multiply_expression.
    def visitMultiply_expression(self, ctx:HanaParser.Multiply_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#datetime_expression.
    def visitDatetime_expression(self, ctx:HanaParser.Datetime_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#interval_expression.
    def visitInterval_expression(self, ctx:HanaParser.Interval_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#model_expression.
    def visitModel_expression(self, ctx:HanaParser.Model_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#model_expression_element.
    def visitModel_expression_element(self, ctx:HanaParser.Model_expression_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#single_column_for_loop.
    def visitSingle_column_for_loop(self, ctx:HanaParser.Single_column_for_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#for_like_part.
    def visitFor_like_part(self, ctx:HanaParser.For_like_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#for_increment_decrement_type.
    def visitFor_increment_decrement_type(self, ctx:HanaParser.For_increment_decrement_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#multi_column_for_loop.
    def visitMulti_column_for_loop(self, ctx:HanaParser.Multi_column_for_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#unary_expression.
    def visitUnary_expression(self, ctx:HanaParser.Unary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#case_statement.
    def visitCase_statement(self, ctx:HanaParser.Case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#simple_case_statement.
    def visitSimple_case_statement(self, ctx:HanaParser.Simple_case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#simple_case_when_part.
    def visitSimple_case_when_part(self, ctx:HanaParser.Simple_case_when_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#searched_case_statement.
    def visitSearched_case_statement(self, ctx:HanaParser.Searched_case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#searched_case_when_part.
    def visitSearched_case_when_part(self, ctx:HanaParser.Searched_case_when_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#case_else_part.
    def visitCase_else_part(self, ctx:HanaParser.Case_else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#atom.
    def visitAtom(self, ctx:HanaParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#expression_or_vector.
    def visitExpression_or_vector(self, ctx:HanaParser.Expression_or_vectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#vector_expr.
    def visitVector_expr(self, ctx:HanaParser.Vector_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#quantified_expression.
    def visitQuantified_expression(self, ctx:HanaParser.Quantified_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#standard_function.
    def visitStandard_function(self, ctx:HanaParser.Standard_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#over_clause_keyword.
    def visitOver_clause_keyword(self, ctx:HanaParser.Over_clause_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#within_or_over_clause_keyword.
    def visitWithin_or_over_clause_keyword(self, ctx:HanaParser.Within_or_over_clause_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#standard_prediction_function_keyword.
    def visitStandard_prediction_function_keyword(self, ctx:HanaParser.Standard_prediction_function_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#over_clause.
    def visitOver_clause(self, ctx:HanaParser.Over_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#windowing_clause.
    def visitWindowing_clause(self, ctx:HanaParser.Windowing_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#windowing_type.
    def visitWindowing_type(self, ctx:HanaParser.Windowing_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#windowing_elements.
    def visitWindowing_elements(self, ctx:HanaParser.Windowing_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#using_clause.
    def visitUsing_clause(self, ctx:HanaParser.Using_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#using_element.
    def visitUsing_element(self, ctx:HanaParser.Using_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#collect_order_by_part.
    def visitCollect_order_by_part(self, ctx:HanaParser.Collect_order_by_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#within_or_over_part.
    def visitWithin_or_over_part(self, ctx:HanaParser.Within_or_over_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#cost_matrix_clause.
    def visitCost_matrix_clause(self, ctx:HanaParser.Cost_matrix_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#xml_passing_clause.
    def visitXml_passing_clause(self, ctx:HanaParser.Xml_passing_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#xml_attributes_clause.
    def visitXml_attributes_clause(self, ctx:HanaParser.Xml_attributes_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#xml_namespaces_clause.
    def visitXml_namespaces_clause(self, ctx:HanaParser.Xml_namespaces_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#xml_table_column.
    def visitXml_table_column(self, ctx:HanaParser.Xml_table_columnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#xml_general_default_part.
    def visitXml_general_default_part(self, ctx:HanaParser.Xml_general_default_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#xml_multiuse_expression_element.
    def visitXml_multiuse_expression_element(self, ctx:HanaParser.Xml_multiuse_expression_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#xmlroot_param_version_part.
    def visitXmlroot_param_version_part(self, ctx:HanaParser.Xmlroot_param_version_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#xmlroot_param_standalone_part.
    def visitXmlroot_param_standalone_part(self, ctx:HanaParser.Xmlroot_param_standalone_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#xmlserialize_param_enconding_part.
    def visitXmlserialize_param_enconding_part(self, ctx:HanaParser.Xmlserialize_param_enconding_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#xmlserialize_param_version_part.
    def visitXmlserialize_param_version_part(self, ctx:HanaParser.Xmlserialize_param_version_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#xmlserialize_param_ident_part.
    def visitXmlserialize_param_ident_part(self, ctx:HanaParser.Xmlserialize_param_ident_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#sql_plus_command.
    def visitSql_plus_command(self, ctx:HanaParser.Sql_plus_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#whenever_command.
    def visitWhenever_command(self, ctx:HanaParser.Whenever_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#set_command.
    def visitSet_command(self, ctx:HanaParser.Set_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#exit_command.
    def visitExit_command(self, ctx:HanaParser.Exit_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#prompt_command.
    def visitPrompt_command(self, ctx:HanaParser.Prompt_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#partition_extension_clause.
    def visitPartition_extension_clause(self, ctx:HanaParser.Partition_extension_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#column_alias.
    def visitColumn_alias(self, ctx:HanaParser.Column_aliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#table_alias.
    def visitTable_alias(self, ctx:HanaParser.Table_aliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#alias_quoted_string.
    def visitAlias_quoted_string(self, ctx:HanaParser.Alias_quoted_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#where_clause.
    def visitWhere_clause(self, ctx:HanaParser.Where_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#current_of_clause.
    def visitCurrent_of_clause(self, ctx:HanaParser.Current_of_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#into_clause.
    def visitInto_clause(self, ctx:HanaParser.Into_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#xml_column_name.
    def visitXml_column_name(self, ctx:HanaParser.Xml_column_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#cost_class_name.
    def visitCost_class_name(self, ctx:HanaParser.Cost_class_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#attribute_name.
    def visitAttribute_name(self, ctx:HanaParser.Attribute_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#savepoint_name.
    def visitSavepoint_name(self, ctx:HanaParser.Savepoint_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#rollback_segment_name.
    def visitRollback_segment_name(self, ctx:HanaParser.Rollback_segment_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#table_var_name.
    def visitTable_var_name(self, ctx:HanaParser.Table_var_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#schema_name.
    def visitSchema_name(self, ctx:HanaParser.Schema_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#routine_name.
    def visitRoutine_name(self, ctx:HanaParser.Routine_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#package_name.
    def visitPackage_name(self, ctx:HanaParser.Package_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#implementation_type_name.
    def visitImplementation_type_name(self, ctx:HanaParser.Implementation_type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#reference_model_name.
    def visitReference_model_name(self, ctx:HanaParser.Reference_model_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#main_model_name.
    def visitMain_model_name(self, ctx:HanaParser.Main_model_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#aggregate_function_name.
    def visitAggregate_function_name(self, ctx:HanaParser.Aggregate_function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#query_name.
    def visitQuery_name(self, ctx:HanaParser.Query_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#constraint_name.
    def visitConstraint_name(self, ctx:HanaParser.Constraint_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#label_name.
    def visitLabel_name(self, ctx:HanaParser.Label_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#type_name.
    def visitType_name(self, ctx:HanaParser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#sequence_name.
    def visitSequence_name(self, ctx:HanaParser.Sequence_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#exception_name.
    def visitException_name(self, ctx:HanaParser.Exception_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#function_name.
    def visitFunction_name(self, ctx:HanaParser.Function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#proc_name.
    def visitProc_name(self, ctx:HanaParser.Proc_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#trigger_name.
    def visitTrigger_name(self, ctx:HanaParser.Trigger_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#variable_name_old.
    def visitVariable_name_old(self, ctx:HanaParser.Variable_name_oldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#index_name.
    def visitIndex_name(self, ctx:HanaParser.Index_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#cursor_name_old.
    def visitCursor_name_old(self, ctx:HanaParser.Cursor_name_oldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#record_name.
    def visitRecord_name(self, ctx:HanaParser.Record_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#collection_name.
    def visitCollection_name(self, ctx:HanaParser.Collection_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#link_name.
    def visitLink_name(self, ctx:HanaParser.Link_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#column_name_old.
    def visitColumn_name_old(self, ctx:HanaParser.Column_name_oldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#tableview_name.
    def visitTableview_name(self, ctx:HanaParser.Tableview_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#char_set_name.
    def visitChar_set_name(self, ctx:HanaParser.Char_set_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#keep_clause.
    def visitKeep_clause(self, ctx:HanaParser.Keep_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#function_argument.
    def visitFunction_argument(self, ctx:HanaParser.Function_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#function_argument_analytic.
    def visitFunction_argument_analytic(self, ctx:HanaParser.Function_argument_analyticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#function_argument_modeling.
    def visitFunction_argument_modeling(self, ctx:HanaParser.Function_argument_modelingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#respect_or_ignore_nulls.
    def visitRespect_or_ignore_nulls(self, ctx:HanaParser.Respect_or_ignore_nullsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#argument.
    def visitArgument(self, ctx:HanaParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#type_spec.
    def visitType_spec(self, ctx:HanaParser.Type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#datatype.
    def visitDatatype(self, ctx:HanaParser.DatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#precision_part.
    def visitPrecision_part(self, ctx:HanaParser.Precision_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#native_datatype_element.
    def visitNative_datatype_element(self, ctx:HanaParser.Native_datatype_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#bind_variable.
    def visitBind_variable(self, ctx:HanaParser.Bind_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#bind_sql_error_code.
    def visitBind_sql_error_code(self, ctx:HanaParser.Bind_sql_error_codeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#const_sql_error_code.
    def visitConst_sql_error_code(self, ctx:HanaParser.Const_sql_error_codeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#bind_sql_error_message.
    def visitBind_sql_error_message(self, ctx:HanaParser.Bind_sql_error_messageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#const_sql_error_message.
    def visitConst_sql_error_message(self, ctx:HanaParser.Const_sql_error_messageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#general_element.
    def visitGeneral_element(self, ctx:HanaParser.General_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#general_element_part.
    def visitGeneral_element_part(self, ctx:HanaParser.General_element_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#table_element.
    def visitTable_element(self, ctx:HanaParser.Table_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#constant.
    def visitConstant(self, ctx:HanaParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#numeric.
    def visitNumeric(self, ctx:HanaParser.NumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#numeric_negative.
    def visitNumeric_negative(self, ctx:HanaParser.Numeric_negativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#quoted_string.
    def visitQuoted_string(self, ctx:HanaParser.Quoted_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#id.
    def visitId(self, ctx:HanaParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#id_expression.
    def visitId_expression(self, ctx:HanaParser.Id_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#not_equal_op.
    def visitNot_equal_op(self, ctx:HanaParser.Not_equal_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#greater_than_or_equals_op.
    def visitGreater_than_or_equals_op(self, ctx:HanaParser.Greater_than_or_equals_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#less_than_or_equals_op.
    def visitLess_than_or_equals_op(self, ctx:HanaParser.Less_than_or_equals_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#concatenation_op.
    def visitConcatenation_op(self, ctx:HanaParser.Concatenation_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#outer_join_sign.
    def visitOuter_join_sign(self, ctx:HanaParser.Outer_join_signContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HanaParser#regular_id.
    def visitRegular_id(self, ctx:HanaParser.Regular_idContext):
        return self.visitChildren(ctx)



del HanaParser