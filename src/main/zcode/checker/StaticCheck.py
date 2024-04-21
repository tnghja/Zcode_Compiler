
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
class Sym(Type):
    pass
class FuncSym(Sym):

    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body
class VarSym(Sym):
    def __init__(self, typ = None):
        self.typ = typ    
class ArraySym(Type):
    def __init__(self, eleType,ast = None):
        self.eleType = eleType
        self.ast = ast 
class CannotBeInferredSym(Type): pass
class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast):
        self.ast = ast 
        self.BlockFor = 0
        self.function = None
        self.Return = False
        self.listFunction = {
            "readNumber" : FuncSym([], NumberType(), True),
            "readBool" : FuncSym([], BoolType(), True),
            "readString" : FuncSym([], StringType(), True),
            "writeNumber" : FuncSym([NumberType()], VoidType(), True),
            "writeBool" : FuncSym([BoolType()], VoidType(), True),
            "writeString" : FuncSym([StringType()], VoidType(), True)
        }    
    
    def check(self):
        self.visit(self.ast, [{}])
        return None
    def lType_rType_stmt(self,lType : Type, rType : Type, ast, param = None):
        if isinstance(lType,CannotBeInferredSym) or isinstance(rType,CannotBeInferredSym):
             raise TypeCannotBeInferred(ast)
        elif isinstance(lType,Sym) and isinstance(rType,Sym):
             raise TypeCannotBeInferred(ast)
        elif isinstance(lType,Sym) and isinstance(rType,ArraySym):
            raise TypeCannotBeInferred(ast)
        elif isinstance(lType,ArrayType) and isinstance(rType,ArraySym):
            rType = self.visitArrayLiteral(rType.ast, param, lType)
            self.lType_rType_stmt(lType, rType, ast, param)
        elif isinstance(rType,ArraySym):
            raise TypeCannotBeInferred(ast)
        elif isinstance(lType,Sym) :
             lType.typ = rType
        elif  isinstance(rType,Sym):
             rType.typ = lType
        elif self.compareType(rType,lType) is False:
             raise TypeMismatchInStatement(ast)
    def lType_rType_expr(self, lType : Type, rType : Type,ast, param = None) -> bool:
        if isinstance(lType,CannotBeInferredSym) or isinstance(rType,CannotBeInferredSym):
             return True
        elif isinstance(lType,Sym) and isinstance(rType,Sym):
             return True
        elif isinstance(lType,Sym) and isinstance(rType,ArraySym):
             return True
        elif isinstance(lType,ArrayType) and isinstance(rType,ArraySym):
            rType = self.visitArrayLiteral(rType.ast, param, lType)
            return self.lType_rType_expr(lType, rType, ast, param)
        elif isinstance(rType,ArraySym):
             return True
        elif isinstance(lType,Sym) :
             lType.typ = rType
             return False
        elif isinstance(rType,Sym):
             rType.typ = lType
             return False
        elif self.compareType(rType,lType) is False:
             raise TypeMismatchInExpression(ast)
        else :
             return False
    def compareType(self, lType : Type, rType : Type) -> bool:
        if type(lType) is type(rType):
            if type(lType) is ArrayType and type(rType) is ArrayType:
                if len(lType.size) == len(rType.size) and type(lType.eleType) is type(rType.eleType):
                    for idx in range(len(lType.size)):    
                        if lType.size[idx] != rType.size[idx]:
                            return False
                    return True
                else :
                
                    return False
            return True
        else :
        
            return False
    def visitProgram(self, ast, param):
        param = [{}]    

        for decl in ast.decl:
            self.visit(decl,param) 
        main = False
        for name,func in self.listFunction.items():
            if func.body == False : raise NoDefinition(name)
            if name == "main" and self.compareType(func.typ,VoidType()) and func.param == []:
                main = True
        if not main :
            raise NoEntryPoint()    
        
    def visitVarDecl(self, ast, param):
        if param[0].get(ast.name.name): raise Redeclared(Variable(), ast.name.name)
        param[0][ast.name.name] = VarSym(ast.varType)
        if ast.varInit:    
            rType = self.visit(ast.varInit, param)
            lType = param[0][ast.name.name].typ if param[0][ast.name.name].typ else param[0][ast.name.name]
            self.lType_rType_stmt(lType, rType, ast,param)
    def visitFuncDecl(self, ast, param):
        func = self.listFunction.get(ast.name.name)    
        if func and (func.body  or ast.body is None) :
            raise Redeclared(Function(),ast.name.name)
        if ast.body is None:
            typeParam = []
            for each in ast.param:
                 typeParam.append(each.varType)
            self.listFunction[ast.name.name] = FuncSym(typeParam, None, False)
            return       
        listParam = {} 
        typeParam = [] 
        for each in ast.param:
            if listParam.get(each.name.name) is None :
                listParam[each.name.name] = VarSym(each.varType)
                typeParam.append(each.varType)
            else :
                raise Redeclared(Parameter(),each.name.name) 
        if func:
            ListlType = self.listFunction[ast.name.name].param
            ListrType = typeParam
            if len(ListlType) != len(ListrType):
                 raise Redeclared(Function(),ast.name.name) 
            for i in range(len(ListlType)):
                if self.compareType(ListlType[i],ListrType[i]) is False:
                    raise Redeclared(Function(),ast.name.name)
            self.listFunction[ast.name.name].body = True
        else:
            self.listFunction[ast.name.name] = FuncSym(typeParam, None, True)     
        self.Return = False
        self.function = self.listFunction[ast.name.name] 
        self.visit(ast.body, [listParam] + param)
        if not self.Return:
            if self.listFunction[ast.name.name].typ is None: 
                self.listFunction[ast.name.name].typ = VoidType()
            elif not isinstance(self.listFunction[ast.name.name].typ, VoidType):
                raise TypeMismatchInStatement(Return(None))
    def visitId(self, ast, param):  
        Id = None
        for scope in param:
            Id = scope.get(ast.name)
            if Id is not None :
                break
        if Id is None :
            raise Undeclared(Identifier(),ast.name)
        elif Id.typ:
            return Id.typ
        else :
            return Id
    def visitCallExpr(self, ast, param):
        func = self.listFunction.get(ast.name.name)    
        if func is None : raise Undeclared(Function(),ast.name.name)
        if len(func.param) != len (ast.args) : 
            raise TypeMismatchInExpression(ast)
        for i in range(len(func.param)):
            rType = self.visit(ast.args[i], param)
            lType = self.visit(func.param[i], param)
            cannotBeInferred = self.lType_rType_expr(lType,rType,ast,param)
            if cannotBeInferred : return CannotBeInferredSym()     
        if func.typ is None : 
            return func
        elif self.compareType(func.typ,VoidType()):
            raise TypeMismatchInExpression(ast)
        else :
            return func.typ
    def visitCallStmt(self, ast, param):
        func = self.listFunction.get(ast.name.name)
        #TODO: implement kiểm tra Undeclared
        if func is None : raise Undeclared(Function(),ast.name.name)
        if len(func.param) != len (ast.args) : 
            raise TypeMismatchInStatement(ast)
        for i in range(len(func.param)):
            rType = self.visit(ast.args[i], param)
            lType = self.visit(func.param[i], param)
            self.lType_rType_stmt(lType,rType,ast,param)  
        if func.typ is None:
            self.listFunction[ast.name.name].typ = VoidType()
            return func
        else :
            if self.compareType(func.typ,VoidType()) is False : raise TypeMismatchInStatement(ast)
            return func.typ
    def visitIf(self, ast, param):
        rType = self.visit(ast.expr, param) 
        lType = BoolType()
        self.lType_rType_stmt(lType,rType,ast,param) 
        self.visit(ast.thenStmt, param)    
        if ast.elifStmt :
            for item in ast.elifStmt:
                rType = self.visit(item[0], param) 
                lType = BoolType()
                self.lType_rType_stmt(lType,rType,ast,param) 
                self.visit(item[1], param)           
        if ast.elseStmt:
            self.visit(ast.elseStmt, param)
    def visitFor(self, ast, param):
        rType = self.visit(ast.name, param) 
        lType = NumberType()
        self.lType_rType_stmt(lType,rType,ast,param)  
        rType = self.visit(ast.condExpr, param) 
        lType = BoolType()
        self.lType_rType_stmt(lType,rType,ast,param)       
        rType = self.visit(ast.updExpr, param) 
        lType = NumberType()
        self.lType_rType_stmt(lType,rType,ast,param)       
        self.BlockFor += 1
        self.visit(ast.body, param)
        self.BlockFor -= 1  
    def visitReturn(self, ast, param):
        self.Return = True
        rType = self.visit(ast.expr, param) if ast.expr else VoidType()
        lType = self.function.typ if self.function.typ else self.function
        self.lType_rType_stmt(lType,rType,ast,param)
    def visitAssign(self, ast, param):
        rType = self.visit(ast.rhs, param)
        lType = self.visit(ast.lhs, param) 
        self.lType_rType_stmt(lType,rType,ast,param)
    def visitBinaryOp(self, ast, param):
        op = ast.op
        left = self.visit(ast.left, param)
        if op in ['+', '-', '*', '/', '%']:
            rType = NumberType()
            cannotBeInferred = self.lType_rType_expr(rType,left,ast,param)
            if cannotBeInferred : return CannotBeInferredSym()           
        elif op in ['=', '!=', '<', '>', '>=', '<=']:
            rType = NumberType()
            cannotBeInferred = self.lType_rType_expr(rType,left,ast,param)
            if cannotBeInferred : return CannotBeInferredSym()          
        elif op in ['and', 'or']:
            rType = BoolType()
            cannotBeInferred = self.lType_rType_expr(rType,left,ast,param)
            if cannotBeInferred : return CannotBeInferredSym()
        elif op in ['==']:
            rType = StringType()
            cannotBeInferred = self.lType_rType_expr(rType,left,ast,param)
            if cannotBeInferred : return CannotBeInferredSym()
        elif op in ['...']:
            rType = StringType()
            cannotBeInferred = self.lType_rType_expr(rType,left,ast,param)
            if cannotBeInferred : return CannotBeInferredSym()
        right = self.visit(ast.right, param)  
        if op in ['+', '-', '*', '/', '%']:
            rType = NumberType()
            cannotBeInferred = self.lType_rType_expr(rType,right,ast,param)
            if cannotBeInferred : return CannotBeInferredSym()
            returnType = NumberType()
        elif op in ['=', '!=', '<', '>', '>=', '<=']:
            rType = NumberType()
            cannotBeInferred = self.lType_rType_expr(rType,right,ast,param)
            if cannotBeInferred : return CannotBeInferredSym()
            returnType = BoolType()
        elif op in ['and', 'or']:
            rType = BoolType()
            cannotBeInferred = self.lType_rType_expr(rType,right,ast,param)
            if cannotBeInferred : return CannotBeInferredSym()
            returnType = BoolType()
        elif op in ['==']:
            rType = StringType()
            cannotBeInferred = self.lType_rType_expr(rType,right,ast,param)
            if cannotBeInferred : return CannotBeInferredSym()
            returnType = BoolType()
        elif op in ['...']:
            rType = StringType()
            cannotBeInferred = self.lType_rType_expr(rType,right,ast,param)
            if cannotBeInferred : return CannotBeInferredSym()
            returnType = StringType() 
        return returnType
    def visitUnaryOp(self, ast, param):
        op = ast.op
        typ = self.visit(ast.operand, param)
        if op in ['+', '-']:
            lType = NumberType()
            cannotBeInferred = self.lType_rType_expr(lType,typ,ast,param)
            if cannotBeInferred : return CannotBeInferredSym()
            returnType = NumberType()
        if op in ['not']:
            lType = BoolType()
            cannotBeInferred = self.lType_rType_expr(lType,typ,ast,param)
            if cannotBeInferred : return CannotBeInferredSym()
            returnType = BoolType()
    def visitArrayCell(self, ast, param):
        arr = self.visit(ast.arr, param)
        if isinstance(arr, (BoolType, StringType, NumberType)):
            raise TypeMismatchInExpression(ast)
        elif not isinstance(arr, ArrayType):
            return CannotBeInferredSym()
        for item in ast.idx:
            rType = self.visit(item, param)
            lType = NumberType()
            cannotBeInferred = self.lType_rType_expr(lType,rType,ast,param)
            if cannotBeInferred : return CannotBeInferredSym()
        if len(arr.size) < len(ast.idx): raise TypeMismatchInExpression(ast)
        elif len(arr.size) == len(ast.idx): return arr.eleType
        return ArrayType(arr.size[len(ast.idx):], arr.eleType)   
    def visitArrayLiteral(self, ast, param, mainTyp = None):
        if mainTyp is not None:
            result = mainTyp
            mainTyp = mainTyp.eleType if len(mainTyp.size) == 1 else ArrayType(mainTyp.size[1:], mainTyp.eleType) 
            for item in ast.value:
                rType = self.visit(item, param)   
                if isinstance(rType,CannotBeInferredSym) or isinstance(mainTyp,CannotBeInferredSym):
                    return CannotBeInferredSym()
                if isinstance(mainTyp,ArrayType) and isinstance(rType,ArraySym):
                    mainTyp = self.visitArrayLiteral(rType.ast, param, mainTyp)
                elif isinstance(rType, ArraySym):
                    return CannotBeInferredSym()
                elif isinstance(rType, Sym):
                    rType.typ = mainTyp
            return self.visitArrayLiteral(ast, param)
        mainType = None
        listType = []
        for item in ast.value:
            checkTyp = self.visit(item, param)
            listType += [checkTyp]
            if mainType is None and isinstance(checkTyp, (BoolType, StringType, NumberType, ArrayType)):
                mainType = checkTyp
            elif isinstance(checkTyp, CannotBeInferredSym):
                return CannotBeInferredSym()
        if mainType is None:
            return ArraySym(listType, ast)
        for item in listType:
            if isinstance(item,ArraySym):
                if item.eleType[0].typ :
                    item = ArrayType([len(item.eleType)], item.eleType[0].typ)
            rType = item
            lType = mainType
            cannotBeInferred = self.lType_rType_expr(lType,rType,ast,param=param)
            if cannotBeInferred : return CannotBeInferredSym()
        if type(mainType) in [StringType, BoolType, NumberType]: return ArrayType([len(ast.value)], mainType)
        else: return ArrayType([float(len(ast.value))] + mainType.size, mainType.eleType)
    def visitBlock(self, ast, param):
        paramNew = [{}] + param 
        for item in ast.stmt: 
            self.visit(item,paramNew)   
    def visitContinue(self, ast, param):
        if self.BlockFor == 0: raise MustInLoop(ast)
    def visitBreak(self, ast, param):
        if self.BlockFor == 0: raise MustInLoop(ast)   
    def visitNumberType(self, ast, param): return ast
    def visitBoolType(self, ast, param): return ast
    def visitStringType(self, ast, param): return ast
    def visitArrayType(self, ast, param): return ast
    def visitNumberLiteral(self, ast, param): return NumberType()
    def visitBooleanLiteral(self, ast, param): return BoolType()
    def visitStringLiteral(self, ast, param): return StringType()