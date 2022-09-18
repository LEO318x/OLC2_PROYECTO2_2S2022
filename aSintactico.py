import ply.yacc as yacc
from Abstract.Retorno import Retorno
from Expresion.Acceso import Acceso
from Expresion.AccesoArregloVector import AccesoArregloVector
from Expresion.AccesoId import AccesoID
from Expresion.Logica import Logica
from Expresion.DefStruct import DefStruct
from Expresion.NuevoArreglo import NuevoArreglo
from Expresion.NuevoVector import NuevoVector
from Expresion.Relacional import Relacional
from Instruccion.Asignacion import Asignacion
from Instruccion.AsignacionStruct import AsignacionStruct
from Instruccion.AsignarArreglo import AsignarArreglo
from Instruccion.Casteo import Casteo
from Instruccion.ContainsVector import ContainsVector
from Instruccion.Declaracion import Declaracion, Declaracion_Tipo
from Instruccion.ForIn import ForIn, ForInAV
from Instruccion.Funcion import Funcion
from Instruccion.InsertVector import InsertVector
from Instruccion.Llamar import Llamar
from Instruccion.LlamarExpr import LlamarExpr
from Instruccion.Loop import Loop
from Instruccion.Main import Main
from Instruccion.NewStruct import NewStruct
from Instruccion.RemoveVector import RemoveVector
from Instruccion.Return import Return
from Instruccion.Sentencia import Sentencia
from Nativas.Abs import Abs
from Nativas.CapacityVector import CapacityVector
from Nativas.Clone import Clone
from Nativas.Exponente import Exponente
from Nativas.Len import Len
from Instruccion.PushVector import PushVector
from Nativas.Sqrt import Sqrt
from Nativas.ToOwned import ToOwned
from Nativas.ToString import ToString
from Simbolo.Entorno import Entorno
from Simbolo.Simbolo import Simbolo
from aLexico import tokens, analizador
from aLexico import find_column
from Instruccion.Imprimir import Print
from Instruccion.If import If
from Instruccion.While import While
from Instruccion.Break import Break
from Instruccion.Continue import Continue
from Expresion.Literal import Literal
from Simbolo.Tipo import *
from Expresion.Aritmetica import Aritmetica
from Reporte.Reportes import generarReporteSimbolos, generarReporteErrores

input = ""

# Asociación de operadores y precedencia
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NEGA'),
    ('left', 'IGUALACION', 'DISTINTO'),
    ('left', 'MENORQ', 'MAYORQ', 'MYRIGUAL', 'MNRIGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MUL', 'DIV', 'MOD'),
    ('left', 'IPAR', 'DPAR'),
    ('right', 'UMENOS'),
)


# Inicio sintáctico
def p_init(t):
    'init : instrucciones'
    t[0] = t[1]


def p_lista_instrucciones(t):
    'instrucciones : instrucciones instrucciones_globales'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t):
    'instrucciones : instrucciones_globales'
    t[0] = [t[1]]


def p_instrucciones_globales(t):
    '''instrucciones_globales : structdef
                              | fnmain
                              | fnst
                              | fnwretst'''
    t[0] = t[1]

def p_instruccion_main(t):
    '''fnmain : FN MAIN IPAR DPAR ILLAVE instrucciones_main DLLAVE'''
    t[0] = Main(t.lineno(1), find_column(input, t.slice[1]), t[6])



def p_lista_instrucciones_main(t):
    '''instrucciones_main : instrucciones_main instruccion'''
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion_main(t):
    'instrucciones_main : instruccion'
    t[0] = [t[1]]

def p_instruccion(t):
    '''instruccion : declaracion
                  | declaracion_con_tipo
                  | asignacion
                  | structasig
                  | ifst
                  | whilest
                  | loopst
                  | forinst
                  | llamarfn PTOCOMA
                  | print_inst
                  | breakinst PTOCOMA
                  | continueinst PTOCOMA
                  | returninst PTOCOMA
                  | structdef
                  | vector_push PTOCOMA
                  | vector_insert PTOCOMA
                  '''
    t[0] = t[1]


def p_declaracion(t):
    '''declaracion : LET ID IGUAL expresion PTOCOMA'''
    t[0] = Declaracion(t[2], t[4], False, t.lineno(3), find_column(input, t.slice[3]))


def p_declaracion_mut(t):
    '''declaracion : LET MUT ID IGUAL expresion PTOCOMA'''
    t[0] = Declaracion(t[3], t[5], True, t.lineno(4), find_column(input, t.slice[4]))


def p_declaracion_struct_mut(t):
    '''declaracion : LET MUT ID IGUAL ID ILLAVE  strattrexpre DLLAVE PTOCOMA'''
    t[0] = Declaracion(t[3], NewStruct(t.lineno(1), find_column(input, t.slice[1]), t[5], t[7]), True, t.lineno(4), find_column(input, t.slice[4]))


def p_declaracion_struct(t):
    '''declaracion : LET ID IGUAL ID ILLAVE  strattrexpre DLLAVE PTOCOMA'''
    t[0] = Declaracion(t[2], NewStruct(t.lineno(1), find_column(input, t.slice[1]), t[4], t[6]), False, t.lineno(3), find_column(input, t.slice[3]))


def p_strattrexpre(t):
    '''strattrexpre : strattrexpre COMA strattrexpr '''
    t[1].append(t[3])
    t[0] = t[1]


def p_strattrexpr(t):
    '''strattrexpre : strattrexpr'''
    t[0] = [t[1]]


def p_strattrexpro(t):
    '''strattrexpr : ID DOSPTOS expresion'''
    t[0] = {t[1]: t[3]}


def p_strattrexpro2(t):
    '''strattrexpr : ID DOSPTOS expresion2'''
    t[0] = {t[1]: t[3]}


def p_strexpr2(t):
    '''expresion2 : ID ILLAVE strattrexpre DLLAVE'''
    t[0] = NewStruct(t.lineno(1), find_column(input, t.slice[1]), t[1], t[3])


def p_structcamp(t):
    '''expresion : expresion PUNTO ID'''
    t[0] = AccesoID(t.lineno(2), find_column(input, t.slice[2]), t[1], t[3])


def p_declaracion_con_tipo(t):
    '''declaracion_con_tipo : LET ID DOSPTOS tipo_dato IGUAL expresion PTOCOMA'''
    t[0] = Declaracion_Tipo(t[2], t[6], t[4], False, t.lineno(5), find_column(input, t.slice[5]))


def p_declaracion_con_tipo_mut(t):
    '''declaracion_con_tipo : LET MUT ID DOSPTOS tipo_dato IGUAL expresion PTOCOMA'''
    t[0] = Declaracion_Tipo(t[3], t[7], t[5], True, t.lineno(6), find_column(input, t.slice[6]))


def p_declaracion_con_tipo_struct_mut(t):
    '''declaracion_con_tipo : LET MUT ID DOSPTOS tipo_dato IGUAL ID ILLAVE  strattrexpre DLLAVE PTOCOMA'''
    t[0] = Declaracion_Tipo(t[3], NewStruct(t.lineno(1), find_column(input, t.slice[1]), t[7], t[9]), t[5], True, t.lineno(1), find_column(input, t.slice[1]))


def p_declaracion_con_tipo_struct(t):
    '''declaracion_con_tipo : LET ID DOSPTOS tipo_dato IGUAL ID ILLAVE  strattrexpre DLLAVE PTOCOMA'''
    t[0] = Declaracion_Tipo(t[2], NewStruct(t.lineno(1), find_column(input, t.slice[1]), t[6], t[8]), t[4], False, t.lineno(1), find_column(input, t.slice[1]))


def p_structasig(t):
    '''structasig : lsacceso IGUAL expresion PTOCOMA'''
    t[0] = AsignacionStruct(t.lineno(2), find_column(input, t.slice[2]), t[1], t[3])

def p_lstasig(t):
    '''lsacceso : lsacceso PUNTO ID '''
    t[1].append(t[3])
    t[0] = t[1]


def p_lsasigo(t):
    '''lsacceso : ID PUNTO ID'''
    t[0] = [t[1], t[3]]

def p_tipo_dato(t):
    '''tipo_dato : I64
                 | F64
                 | USIZE
                 | STRING
                 | RSTR
                 | CHAR
                 | BOOL
                 | ID'''

    #t[0] = BuscarTipo(t.lineno(1), find_column(input, t.slice[1]), t[1])
    tipo = ""
    match t[1]:
        case 'i64':
            tipo = TIPO_DATO.INTEGER
        case 'f64':
            tipo = TIPO_DATO.FLOAT
        case 'usize':
            tipo = TIPO_DATO.INTEGER
        case 'bool':
            tipo = TIPO_DATO.BOOL
        case 'String':
            tipo = TIPO_DATO.STRING
        case '&str':
            tipo = TIPO_DATO.RSTR
        case 'char':
            tipo = TIPO_DATO.CHAR
        case _:
            if t.slice[1].type == "ID":
                tipo = TIPO_DATO.STRUCT
            else:
                tipo = TIPO_DATO.TYPE
    t[0] = tipo


def p_tipo_dato_arr(t):
    '''tipo_dato : AMP MUT ICOR tipo_dato DCOR
                | AMP MUT ICOR tipo_dato PTOCOMA expresion DCOR
                | ICOR tipo_dato PTOCOMA expresion DCOR'''
    t[0] = TIPO_DATO.ARRAY


def p_tipo_dato_vector(t):
    '''tipo_dato : AMP MUT VEC MENORQ tipo_dato MAYORQ
                | VEC MENORQ tipo_dato MAYORQ'''
    t[0] = TIPO_DATO.VECT


def p_asignacion(t):
    '''asignacion : ID IGUAL expresion PTOCOMA'''
    t[0] = Asignacion(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))


def p_asignacionarr(t):
    '''asignacion : expresion ICOR expresion DCOR IGUAL expresion PTOCOMA'''
    t[0] = AsignarArreglo(t.lineno(2), find_column(input, t.slice[2]), t[1], t[3], t[6])

def p_ifst(t):
    '''ifst : IF expresion st elsest'''
    # print(f'g_if{t[3]}')
    t[0] = If(t.lineno(1), find_column(input, t.slice[1]), t[2], t[3], t[4])


def p_elsest(t):
    '''elsest : ELSE st
              | ELSE ifst
              | '''

    if len(t) > 1:
        t[0] = t[2]
    else:
        t[0] = None


def p_whilest(t):
    '''whilest : WHILE expresion st '''
    t[0] = While(t.lineno(1), find_column(input, t.slice[1]), t[2], t[3])


def p_loopst(t):
    '''loopst : LOOP st'''
    t[0] = Loop(t.lineno(1), find_column(input, t.slice[1]), t[2])


def p_forinst(t):
    '''forinst : FOR ID IN expresion PUNTO PUNTO expresion st'''
    t[0] = ForIn(t.lineno(1), find_column(input, t.slice[1]), t[2], t[4], t[7], t[8])


def p_forinstexpr(t):
    '''forinst : FOR ID IN expresion st'''
    t[0] = ForInAV(t.lineno(1), find_column(input, t.slice[1]), t[2], t[4], t[5])


def p_breakinst(t):
    '''breakinst : BREAK'''
    t[0] = Break(t.lineno(1), find_column(input, t.slice[1]))


def p_continueinst(t):
    '''continueinst : CONTINUE'''
    t[0] = Continue(t.lineno(1), find_column(input, t.slice[1]))


def p_returninst(t):
    '''returninst : RETURN expresion
                | RETURN expresion2 '''
    t[0] = Return(t.lineno(1), find_column(input, t.slice[1]), t[2])


def p_fnst(t):
    '''fnst : FN ID IPAR lparams DPAR st'''
    t[0] = Funcion(t.lineno(1), find_column(input, t.slice[1]), t[2], t[6], t[4])


def p_fnsto(t):
    '''fnst : FN ID IPAR DPAR st'''
    t[0] = Funcion(t.lineno(1), find_column(input, t.slice[1]), t[2], t[5], None)


def p_fnwithreturn(t):
    '''fnwretst : FN ID IPAR lparams DPAR GUIONFLECHA tipo_dato st'''
    t[0] = Funcion(t.lineno(1), find_column(input, t.slice[1]), t[2], t[8], t[4], t[7])


def p_fnwithreturno(t):
    '''fnwretst : FN ID IPAR DPAR GUIONFLECHA tipo_dato st'''
    t[0] = Funcion(t.lineno(1), find_column(input, t.slice[1]), t[2], t[7], None, t[6])


def p_lparams(t):
    '''lparams : lparams COMA ID DOSPTOS tipo_dato'''
    # t[1].append(t[3] + ":" + str(t[5]))
    t[1].append(Simbolo(t[3], None, t[5], False))
    t[0] = t[1]


def p_lparamso(t):
    '''lparams : ID DOSPTOS tipo_dato'''
    # t[0] = [t[1] + ":" + str(t[3])]
    t[0] = [Simbolo(t[1], None, t[3], False)]


def p_llamarfn(t):
    '''llamarfn : ID IPAR llparams DPAR'''
    t[0] = Llamar(t.lineno(1), find_column(input, t.slice[1]), t[1], t[3])


def p_llamarfno(t):
    '''llamarfn : ID IPAR DPAR'''
    t[0] = Llamar(t.lineno(1), find_column(input, t.slice[1]), t[1], [])


def p_llparams(t):
    '''llparams : llparams COMA expresion'''
    t[1].append(t[3])
    t[0] = t[1]


def p_llparamso(t):
    '''llparams : expresion '''
    t[0] = [t[1]]


def p_st(t):
    '''st : ILLAVE instrucciones_main DLLAVE
          | ILLAVE DLLAVE'''
    # print(f't[2]: {t.slice[2].type}')
    if t.slice[2].type == 'instrucciones_main':
        t[0] = Sentencia(t.lineno(1), find_column(input, t.slice[1]), t[2])
    else:
        t[0] = Sentencia(t.lineno(1), find_column(input, t.slice[1]), None)


def p_structdef(t):
    '''structdef : STRUCT ID ILLAVE strattrs DLLAVE'''
    t[0] = DefStruct(t.lineno(1), find_column(input, t.slice[1]), t[2], t[4])


def p_strattrs(t):
    '''strattrs : strattrs COMA strattr'''
    t[1].append(t[3])
    t[0] = t[1]


def p_strattro(t):
    '''strattrs : strattr'''
    t[0] = [t[1]]


def p_strattr(t):
    '''strattr : ID DOSPTOS tipo_dato'''
    #print(f'gstr: {t[3]}')
    t[0] = {t[1]: Retorno('', t[3])}


def p_vectoresdef(t):
    '''instrvec : VECD NOT ICOR lsexprev DCOR'''
    t[0] = NuevoVector(t.lineno(1), find_column(input, t.slice[1]), t[4])

def p_lsexprev(t):
    '''lsexprev : lsexprev COMA expresion'''
    t[1].append(t[3])
    t[0] = t[1]

def p_lsexprevo(t):
    '''lsexprev : expresion'''
    t[0] = [t[1]]


def p_exprev(t):
    '''expresion : instrvec'''
    t[0] = t[1]


def p_print(t):
    '''print_inst : PRINTLN NOT IPAR lexpresion DPAR PTOCOMA'''

    instr = Print(t.lineno(1), find_column(input, t.slice[1]), t[4])
    t[0] = instr


def p_lprint(t):
    '''lexpresion : lexpresion COMA expresion'''
    t[1].append(t[3])
    t[0] = t[1]


def p_lprinto(t):
    '''lexpresion : expresion'''
    t[0] = [t[1]]


def p_expresion_aritmetica(t):
    '''expresion : expresion MAS expresion
                | expresion MENOS expresion
                | expresion MUL expresion
                | expresion DIV expresion
                | expresion MOD expresion
                | I64 DOSPTOS DOSPTOS POW IPAR expresion COMA expresion DPAR
                | F64 DOSPTOS DOSPTOS POWF IPAR expresion COMA expresion DPAR '''

    if t[2] == '+':
        # print(f'|--->{t[1]}')
        t[0] = Aritmetica(t[1], TIPO_OPERACION.SUMA, t[3], t.lineno(2), find_column(input, t.slice[2]), None)
    elif t[2] == '-':
        t[0] = Aritmetica(t[1], TIPO_OPERACION.RESTA, t[3], t.lineno(2), find_column(input, t.slice[2]), None)
    elif t[2] == '*':
        t[0] = Aritmetica(t[1], TIPO_OPERACION.MULTI, t[3], t.lineno(2), find_column(input, t.slice[2]), None)
    elif t[2] == '/':
        t[0] = Aritmetica(t[1], TIPO_OPERACION.DIV, t[3], t.lineno(2), find_column(input, t.slice[2]), None)
    elif t[2] == '%':
        t[0] = Aritmetica(t[1], TIPO_OPERACION.MOD, t[3], t.lineno(2), find_column(input, t.slice[2]), None)
    elif t.slice[4].type == 'POW':
        t[0] = Exponente(t[6], TIPO_OPERACION.EXPO, t[8], t.lineno(5), find_column(input, t.slice[5]))
    elif t.slice[4].type == 'POWF':
        t[0] = Exponente(t[6], TIPO_OPERACION.EXPO, t[8], t.lineno(5), find_column(input, t.slice[5]))


def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec UMENOS'
    t[0] = Aritmetica(None, None, t[2], t.lineno(1), find_column(input, t.slice[1]), True)


def p_expresion_agrupacion(t):
    'expresion : IPAR expresion DPAR'
    t[0] = t[2]

def p_arregloacceso(t):
    '''expresion : expresion ICOR expresion DCOR'''
    t[0] = AccesoArregloVector(t.lineno(2), find_column(input, t.slice[2]), t[1], t[3])


def p_expresion_relacional(t):
    '''expresion : expresion MAYORQ expresion
                        | expresion MENORQ expresion
                        | expresion MYRIGUAL expresion
                        | expresion MNRIGUAL expresion
                        | expresion IGUALACION expresion
                        | expresion DISTINTO expresion'''
    if t.slice[2].type == 'MAYORQ':
        t[0] = Relacional(t[1], TIPO_RELACIONAL.MAYOR, t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t.slice[2].type == 'MENORQ':
        t[0] = Relacional(t[1], TIPO_RELACIONAL.MENOR, t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t.slice[2].type == 'MYRIGUAL':
        t[0] = Relacional(t[1], TIPO_RELACIONAL.MAYORIGUAL, t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t.slice[2].type == 'MNRIGUAL':
        t[0] = Relacional(t[1], TIPO_RELACIONAL.MENORIGUAL, t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t.slice[2].type == 'IGUALACION':
        t[0] = Relacional(t[1], TIPO_RELACIONAL.IGUALACION, t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t.slice[2].type == 'DISTINTO':
        t[0] = Relacional(t[1], TIPO_RELACIONAL.DISTINTO, t[3], t.lineno(2), find_column(input, t.slice[2]))


def p_expresion_logica(t):
    '''expresion : expresion AND expresion
                 | expresion OR expresion
                 | NOT expresion %prec NEGA'''
    # print(f'gtipo: {t.slice[2].type}, gvalor {t[1]}')
    if t.slice[2].type == 'AND':
        t[0] = Logica(t[1], TIPO_LOGICO.AND, t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t.slice[2].type == 'OR':
        t[0] = Logica(t[1], TIPO_LOGICO.OR, t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t.slice[1].type == 'NOT':
        t[0] = Logica(None, TIPO_LOGICO.NOT, t[2], t.lineno(1), find_column(input, t.slice[1]))


def p_expresion_casteo_primitiva(t):
    '''expresion : expresion AS tipo_dato '''
    t[0] = Casteo(t.lineno(2), find_column(input, t.slice[2]), t[3], t[1])


def p_llamarfncomoexpr(t):
    '''expresion : ID IPAR llparams DPAR'''
    t[0] = LlamarExpr(t.lineno(1), find_column(input, t.slice[1]), t[1], t[3])


def p_llamarfncomoexpro(t):
    '''expresion : ID IPAR DPAR'''
    t[0] = LlamarExpr(t.lineno(1), find_column(input, t.slice[1]), t[1], [])


def p_expresion_tostring(t):
    '''expresion : expresion PUNTO TO_STRING IPAR DPAR'''
    t[0] = ToString(t.lineno(2), find_column(input, t.slice[2]), t[1])


def p_expresion_toowned(t):
    '''expresion : expresion PUNTO TO_OWNED IPAR DPAR'''
    t[0] = ToOwned(t.lineno(2), find_column(input, t.slice[2]), t[1])


def p_expresion_clone(t):
    '''expresion : expresion PUNTO CLONE IPAR DPAR'''
    t[0] = Clone(t.lineno(2), find_column(input, t.slice[2]), t[1])


def p_expresion_abs(t):
    '''expresion : expresion PUNTO ABS IPAR DPAR'''
    t[0] = Abs(t.lineno(2), find_column(input, t.slice[2]), t[1])


def p_expresion_sqrt(t):
    '''expresion : expresion PUNTO SQRT IPAR DPAR'''
    t[0] = Sqrt(t.lineno(2), find_column(input, t.slice[2]), t[1])


def p_expresion_len(t):
    '''expresion : expresion PUNTO LEN IPAR DPAR'''
    t[0] = Len(t.lineno(2), find_column(input, t.slice[2]), t[1])


def p_instr_pushv(t):
    '''vector_push : ID PUNTO PUSH IPAR expresion DPAR
                    | ID PUNTO PUSH IPAR expresion2 DPAR'''
    t[0] = PushVector(t.lineno(3), find_column(input, t.slice[3]), t[1], t[5])


def p_expresion_capacityv(t):
    '''expresion : expresion PUNTO CAPACITY IPAR DPAR'''
    t[0] = CapacityVector(t.lineno(3), find_column(input, t.slice[3]), t[1])


def p_expresion_with_capacityv(t):
    '''expresion : VEC DOSPTOS DOSPTOS WITH_CAPACITY IPAR expresion DPAR'''
    t[0] = NuevoVector(t.lineno(1), find_column(input, t.slice[1]), [], t[6])


def p_expresion_newv(t):
    '''expresion : VEC DOSPTOS DOSPTOS NEW IPAR DPAR'''
    t[0] = NuevoVector(t.lineno(1), find_column(input, t.slice[1]), [])


# def p_instr_removev(t):
#     '''vector_remove : ID PUNTO REMOVE IPAR expresion DPAR'''
#     t[0] = RemoveVector(t.lineno(1), find_column(input, t.slice[1]), t[1], t[5])


def p_expresion_removev(t):
    '''expresion : expresion PUNTO REMOVE IPAR expresion DPAR'''
    t[0] = RemoveVector(t.lineno(3), find_column(input, t.slice[3]), t[1], t[5])

def p_expresion_containsv(t):
    '''expresion : expresion PUNTO CONTAINS IPAR expresion DPAR'''
    t[0] = ContainsVector(t.lineno(3), find_column(input, t.slice[3]), t[1], t[5])


def p_instr_insertv(t):
    ''' vector_insert : ID PUNTO INSERT IPAR expresion COMA expresion DPAR'''
    t[0] = InsertVector(t.lineno(1), find_column(input, t.slice[1]), t[1], t[5], t[7])


def p_array(t):
    '''expresion : ICOR laexpre DCOR'''
    t[0] = NuevoArreglo(t.lineno(1), find_column(input, t.slice[1]), t[2])
    #t[0] = NuevoArreglo(t.lineno(1), find_column(input, t.slice[1]), t[2])


def p_lexpre(t):
    '''laexpre : laexpre COMA expresion'''
    t[1].append(t[3])
    t[0] = t[1]


def p_lexpreo(t):
    '''laexpre : expresion'''
    t[0] = [t[1]]


# .------------------------.
# | Expresiones Primitivas |
# '------------------------'

def p_expresion_primitiva(t):
    '''expresion : NUMBER
                | DECIMAL
                | ID
                | STRLIT
                | CHARLIT
                | TRUE
                | FALSE '''

    # print(f'gtipo: {t.slice[1].type}, gvalor {t[1]}')
    if t.slice[1].type == 'NUMBER':
        # print(f'Linea: {t.lineno(1)}, Columna: {find_column(input, t.slice[1])}')
        t[0] = Literal(t[1], TIPO_DATO.INTEGER, t.lineno(1), find_column(input, t.slice[1]))
    elif t.slice[1].type == 'DECIMAL':
        t[0] = Literal(t[1], TIPO_DATO.FLOAT, t.lineno(1), find_column(input, t.slice[1]))
    elif t.slice[1].type == 'ID':
        t[0] = Acceso(t[1], t.lineno(1), find_column(input, t.slice[1]))
    elif t.slice[1].type == 'STRLIT':
        t[0] = Literal(t[1], TIPO_DATO.RSTR, t.lineno(1), find_column(input, t.slice[1]))
    elif t.slice[1].type == 'CHARLIT':
        t[0] = Literal(t[1], TIPO_DATO.CHAR, t.lineno(1), find_column(input, t.slice[1]))
    elif t.slice[1].type == 'TRUE':
        t[0] = Literal(t[1], TIPO_DATO.BOOL, t.lineno(1), find_column(input, t.slice[1]))
    elif t.slice[1].type == 'FALSE':
        t[0] = Literal(t[1], TIPO_DATO.BOOL, t.lineno(1), find_column(input, t.slice[1]))


def p_empty(t):
    'empty :'
    pass


def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)


# Parser
parser = yacc.yacc()


def analizar(entrada):
    #print(f'{entrada}')
    input = entrada
    resultado = parser.parse(input)
    env = Entorno("Global", None)
    for i in resultado:
        i.ejecutar(env)
    generarReporteSimbolos()
    generarReporteErrores()

if __name__ == '__main__':
    f = open("./entrada1.txt", "r")

    input = f.read()
    resultado = parser.parse(input)
    env = Entorno("Global", None)
    for i in resultado:
        i.ejecutar(env)

    generarReporteSimbolos()
    generarReporteErrores()