import ply.lex as lex
import re
import codecs
import os
import sys

tokens = [
    'ID',
    'STRLIT',
    'CHARLIT',
    'NUMBER',
    'DECIMAL',
    'COMENT',
    'GUIONFLECHA',
    'ICOR',
    'DCOR',
    'ILLAVE',
    'DLLAVE',
    'IPAR',
    'DPAR',
    'DOSPTOS',
    'COMA',
    'PTOCOMA',
    'MENORQ',
    'MAYORQ',
    'PUNTO',
    'IGUAL',
    'MAS',
    'MENOS',
    'MUL',
    'DIV',
    'MOD',
    'BARVER',
    'AMP',
    'NOT',
    'RQUEST',
    'MYRIGUAL',
    'MNRIGUAL',
    'IGUALACION',
    'DISTINTO',
    'OR',
    'AND',
    'RSTR'
]

reservadas = {
    'i64': 'I64',
    'f64': 'F64',
    'bool': 'BOOL',
    'char': 'CHAR',
    'String': 'STRING',
    'usize': 'USIZE',
    'let': 'LET',
    'mut': 'MUT',
    'struct': 'STRUCT',
    'as': 'AS',
    'println': 'PRINTLN',
    'true': 'TRUE',
    'false': 'FALSE',
    'fn': 'FN',
    'abs': 'ABS',
    'sqrt': 'SQRT',
    'clone': 'CLONE',
    'new': 'NEW',
    'len': 'LEN',
    'push': 'PUSH',
    'remove': 'REMOVE',
    'contains': 'CONTAINS',
    'insert': 'INSERT',
    'capacity': 'CAPACITY',
    'with_capacity': 'WITH_CAPACITY',
    'to_owned': 'TO_OWNED',
    'to_string': 'TO_STRING',
    'return': 'RETURN',
    'continue': 'CONTINUE',
    'break': 'BREAK',
    'main': 'MAIN',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'loop': 'LOOP',
    'for': 'FOR',
    'in': 'IN',
    'match': 'MATCH',
    'pow': 'POW',
    'powf': 'POWF',
    'Vec': 'VEC',
    'vec': 'VECD'
}

tokens = tokens + list(reservadas.values())

t_RSTR = '&str'
t_GUIONFLECHA = r'\->'
t_MAS = r'\+'
t_MENOS = r'\-'
t_MUL = r'\*'
t_DIV = r'\/'
t_MOD = r'\%'
t_ICOR = r'\['
t_DCOR = r'\]'
t_ILLAVE = r'\{'
t_DLLAVE = r'\}'
t_IPAR = r'\('
t_DPAR = r'\)'
t_DOSPTOS = r':'
t_COMA = r','
t_PTOCOMA = r';'
t_MENORQ = r'<'
t_MAYORQ = r'>'
t_PUNTO = r'\.'
t_IGUAL = r'='
t_BARVER = r'\|'
t_AMP = r'&'
t_NOT = r'!'
t_RQUEST = r'\?'
t_MYRIGUAL = r'>='
t_MNRIGUAL = r'<='
t_IGUALACION = r'=='
t_DISTINTO = r'!='
t_OR = r'\|\|'
t_AND = r'&&'


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reservadas:
        t.value = t.value
        t.type = reservadas.get(t.value, 'ID')
        # print(f'tvalue: {t.value}, ttype: {t.type}')
    return t

def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_COMENT(t):
    r'//.*\n'
    t.lexer.lineno += 1


t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_STRLIT(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # remuevo las comillas dobles
    return t


def t_CHARLIT(t):
    r'\'.*?\''
    t.value = t.value[1:-1]  # remuevo las comillas simples
    return t


def find_column(inp, tk):
    line_start = inp.rfind('\n', 0, tk.lexpos) + 1
    return (tk.lexpos - line_start) + 1


def t_error(t):
    print("caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


# Asociación de operadores y precedencia
precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'MUL', 'DIV'),
    ('right', 'UMENOS'),
)

analizador = lex.lex()

if __name__ == '__main__':
    f = open("./entrada1.txt", "r")
    input = f.read()
    analizador.input(input)

    while True:
        tok = analizador.token()
        if not tok: break
        print(tok)
