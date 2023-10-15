from ply.yacc import yacc

from flecha.ast.case_expr import *
from flecha.ast.expression import *
from flecha.ast.program import Program, Def
from flecha.lexer import Lexer


class Parser:
    tokens = Lexer.tokens

    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIV', 'MOD')
    )

    def __init__(self):
        self.__lexer = Lexer().build()
        self.__yacc = yacc(module=self)

    def p_program_empty(self, p):
        """program :"""
        p[0] = Program()

    def p_program(self, p):
        """program : program definition"""
        program = p[1]
        p[0] = program.append(p[2])

    def p_def(self, p):
        """definition : DEF LOWERID parameters DEFEQ expression"""
        p[0] = Def(p[2], build_expression(p[3], p[5]))

    def p_parameters_empty(self, p):
        """parameters :"""
        p[0] = []

    def p_parameters(self, p):
        """parameters : parameters LOWERID"""
        p[0] = p[1] + [p[2]]

    # TODO: add sequenceExpr
    def p_expression(self, p):
        """expression : outerExpr"""
        p[0] = p[1]

    # TODO: add letExpr | lambdaExpr
    def p_outer_expr(self, p):
        """outerExpr :  ifExpr
                      | caseExpr
                      | innerExpr"""
        p[0] = p[1]

    def p_case_expr(self, p):
        """caseExpr : CASE innerExpr caseBranches"""
        p[0] = CaseExpr(p[2], p[3])

    def p_case_branches_empty(self, p):
        """caseBranches :"""
        p[0] = CaseBranches([])

    def p_case_branches_case_branch(self, p):
        """caseBranches : caseBranches caseBranch"""
        p[0] = p[1].append(p[2])

    def p_case_branch(self, p):
        """caseBranch : PIPE UPPERID parameters ARROW innerExpr"""
        p[0] = CaseBranch(p[2], p[3], p[5])

    def p_if_expr(self, p):
        """ifExpr : IF innerExpr THEN innerExpr elseBranches"""
        p[0] = build_if(p[2], p[4], p[5])

    def p_else_branches_elif(self, p):
        """elseBranches : ELIF innerExpr THEN innerExpr elseBranches"""
        p[0] = build_else(build_if(p[2], p[4], p[5]))

    def p_else_branches_else(self, p):
        """elseBranches : ELSE innerExpr"""
        p[0] = build_else(p[2])


    # TODO: add binaryExpr | unaryExpr
    def p_inner_expr(self, p):
        """innerExpr : applyExpr"""
        p[0] = p[1]

    def p_apply_expr_base(self, p):
        """applyExpr : atomicExpr"""
        p[0] = p[1]

    def p_apply_expr(self, p):
        """applyExpr : applyExpr atomicExpr"""
        p[0] = ApplyExpr(p[1], p[2])

    def p_atomic_expr(self, p):
        """atomicExpr :   LOWERID
                        | UPPERID
                        | NUMBER
                        | CHAR
                        | STRING"""
        p[0] = build_atomic(p.slice[1].type, p[1])

    def p_atomic_expr_paren(self, p):
        """atomicExpr : LPAREN expression RPAREN"""
        p[0] = p[2]

    def p_error(self, p):
        print(f'Syntax error: {p.value!r} | At line: {p.lineno}')

    def parse(self, input):
        output = self.__yacc.parse(input, lexer=self.__lexer)
        return output

    def __str__(self):
        return 'Welcome to Flecha (=>) Language :D\n'
