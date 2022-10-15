#Terminais não podem ser substituídos
#Não-terminais podem ser substituídos
#decls ou decl é uma declaração na gramática
#stmts ou stmt é um comando na gramática
import sys, os

sys.path.insert(1, os.path.abspath('./Lexer'))
import tag

num = 0
output = []

tags1 = ['[', ']', '{', '}', '(', ')']
tags2 = [tag.AND, tag.BASIC, tag.BREAK, tag.DO, tag.ELSE, tag.EQUAL, tag.FALSE,tag.GREAT_EQUAL, tag.ID, tag.IF, tag.INDEX, tag.LOW_EQUAL, tag.MINUS,tag.NUM, tag.NO_EQUAL, tag.WHILE, tag.OR, tag.REAL, tag.TEMP, tag.TRUE]


def terminal(): # Debugar aqui
    global num, output, tags1, tags2
    node = ''
    if 'lexeme' in output[num].keys():
        node = output[num]['lexeme']
    else:
        node = output[num]['tag']

    if output[num]['tag'] in tags1:
        tree = {'node': node, 'sonNodes': None}
    elif output[num]['tag'] in tags2:
        if output[num]['tag'] == tags2[0]:
            tree = {'node': 'AND','sonNodes': [{'node': node,'sonNodes': None}]}
        elif output[num]['tag'] == tags2[1]:
            tree = {'node': 'BASIC','sonNodes': [{'node': node,'sonNodes': None}]}
        elif output[num]['tag'] == tags2[2]:
            tree = {'node': 'BREAK','sonNodes': [{'node': node,'sonNodes': None}]}
        elif output[num]['tag'] == tags2[3]:
            tree = {'node': 'DO','sonNodes': [{'node': node,'sonNodes': None}]}
        elif output[num]['tag'] == tags2[4]:
            tree = {'node': 'ELSE','sonNodes': [{'node': node,'sonNodes': None}]}
        elif output[num]['tag'] == tags2[5]:
            tree = {'node': 'EQUAL','sonNodes': [{'node': node,'sonNodes': None}]}
        elif output[num]['tag'] == tags2[6]:
            tree = {'node': 'FALSE','sonNodes': [{'node': node,'sonNodes': None}]}
        elif output[num]['tag'] == tags2[7]:
            tree = {'node': 'GREAT EQUAL','sonNodes': [{'node': node,'sonNodes': None}]}
        elif output[num]['tag'] == tags2[8]:
            tree = {'node': 'ID','sonNodes': [{'node': node,'sonNodes': None}]}
        elif output[num]['tag'] == tags2[9]:
            tree = {'node': 'IF','sonNodes': [{'node': node,'sonNodes': None}]}
        elif output[num]['tag'] == tags2[10]:
            tree = {'node': 'INDEX','sonNodes': [{'node': node,'sonNodes': None}]}
        elif output[num]['tag'] == tags2[11]:
            tree = {'node': 'LOW EQUAL','sonNodes': [{'node': node,'sonNodes': None}]}
        elif output[num]['tag'] == tags2[12]:
            tree = {'node': 'MINUS','sonNodes': [{'node': node,'sonNodes': None}]}
        elif output[num]['tag'] == tags2[13]:
            tree = {'node': 'NUM','sonNodes': [{'node': node,'sonNodes': None}]}
        elif output[num]['tag'] == tags2[14]:
            tree = {'node': 'NO EQUAL','sonNodes': [{'node': node,'sonNodes': None}]}
        elif output[num]['tag'] == tags2[15]:
            tree = {'node': 'WHILE','sonNodes': [{'node': node,'sonNodes': None}]}
        elif output[num]['tag'] == tags2[16]:
            tree = {'node': 'OR','sonNodes': [{'node': node,'sonNodes': None}]}
        elif output[num]['tag'] == tags2[17]:
            tree = {'node': 'REAL','sonNodes': [{'node': node,'sonNodes': None}]}
        elif output[num]['tag'] == tags2[18]:
            tree = {'node': 'TEMP','sonNodes': [{'node': node,'sonNodes': None}]}
        elif output[num]['tag'] == tags2[19]:
            tree = {'node': 'TRUE','sonNodes': [{'node': node,'sonNodes': None}]}
    num += 1
    return tree


def ttype():
    global num, output
    tree = {}

    while(True):
        if(output[num - 1]['tag'] == ';'):
            num -= 2
            if((output[num - 3]['tag'] == '[') and (output[num - 1]['tag'] == ']')):
                gtype = num
                num -= 4
                tree = {'node': 'type', 'sonNodes': [ttype()]}
                num = gtype
                num -= 1
                tree['sonNodes'].append({'node': output[num], 'sonNodes': None})
                num -= 1
                tree['sonNodes'].append({'node': 'NUM', 'sonNodes': [{'node': output[num]['value'], 'sonNodes': None}]})
                num -= 1
                tree['sonNodes'].append({'node': output[num]['tag'], 'sonNodes': None})
                return tree
            else:
                num -= 1
        elif(output[num - 1]['tag'] == '{'):
            try:
                teste = output[num]['tag'] == tag.BASIC
            except:
                print(f'ERRO - linha: {output[num]["line"]}')
            tree = {'node': 'BASIC', 'sonNodes': [{'node': output[num]['lexeme'], 'sonNodes': None}]}
            return tree
    


def decl():
    global num, output
    tree = {'node': 'decl','sonNodes': [ttype()]}
    tree['sonNodes'].append({'node': 'ID', 'sonNodes': [{'node': output[num], 'sonNodes': None}]})
    num += 1
    tree['sonNodes'].append({'node': output[num], 'sonNodes': None})
    return tree


def decls():
    global num
    tree = {}
    compare1 = output[num]['tag'] != tag.WHILE
    compare2 = output[num]['tag'] != tag.IF
    compare3 = output[num]['tag'] != tag.DO
    compare4 = (output[num - 1]['tag'] != ';') or (output[num]['tag'] != tag.ID)
    compare5 = output[num]['tag'] != '{'

    while((compare1) and (compare2) and (compare3) and (compare4) and (compare5)):
        if(output[num]['tag'] == ';'):
            num += 1
            tree = {'node': 'decls', 'sonNodes': [decls()]}
            tree['sonNodes'].append(decl())
        else:
            num += 1
    else:
        tree = None
    return tree


def factor():
    tree = {}
    try:
        tree = {'node': 'factor', 'sonNodes': [loc()]}
    except:
        tree = {'node': 'factor', 'sonNodes': [terminal()]}
        if output[num]['tag'] == 262 or output[num] == 274:
            tree['sonNodes'].append(bbool())
            tree['sonNodes'].append(terminal())
    return tree


def unary():
    tree = {}
    try:
        tree = {'node': 'unary', 'sonNodes': [terminal(),unary()]}
    except:
        tree = {'node': 'unary','sonNodes': [factor()]}
    return tree


def term():
    tree = {}
    try:
        tree = {'node': 'term', 'sonNodes':[term(),terminal(),unary()]}
    except:
        tree = {'node':'term','sonNodes':[unary()]}
    return tree


def expr():
    tree = {}
    try:
        tree = {'node':'expr', 'sonNodes': [expr(),terminal(),term()]}
    except:
        tree = {'node':'expr','sonNodes': [term()]}
    return tree


def rel():
    global tags2
    tree = {'node': 'rel', 'sonNodes': [expr()]}
    if output[num]['tag'] in tags2:
        tree['sonNodes'].append(terminal())
        tree['sonNodes'].append(expr())
    return tree


def equality():
    tree = {}
    try:
        tree = {'node': 'equality', 'sonNodes': [equality(),terminal(),rel()]}
    except:
        tree = {'node':'equality','sonNodes': [rel()]}
    return tree


def join():
    tree = {}
    try:
        tree = {'node': 'join', 'sonNodes': [join(),terminal(),equality()]}
    except:
        tree = {'node':'join','sonNodes': [equality()]}
    return tree


def bbool():
    tree = {}
    try:
        tree = {'node': 'bool', 'sonNodes': [bbool(),terminal(),join()]}
    except:
        tree = {'node':'bool','sonNodes': [join()]}
    return tree


def loc():
    tree = {}
    try:
        tree = {'node': 'loc', 'sonNodes': [loc(),terminal(),bbool(),terminal()]}
    except:
        tree = {'node':'loc','sonNodes': [terminal()]}
    return tree


def stmt():
    tree = {}
    try:
        tree = {'node': 'stmt', 'sonNodes': [terminal()]}
    except:
        try:  #stmt -> loc = bool;
            tree = {'node':'stmt','sonNodes': [loc(),terminal(),bbool(),terminal()]}
        except:  ##stmt -> block;
            tree = {'node': 'stmt', 'sonNodes': [block()]}
    try:  #stmt -> break
        tree['sonNodes'].append(terminal())
    except:  #stmt -> do stmt while (bool);
        tree['sonNodes'].append(stmt())
        tree['sonNodes'].append(terminal())
        tree['sonNodes'].append(terminal())
        tree['sonNodes'].append(bbool())
        tree['sonNodes'].append(terminal())
        tree['sonNodes'].append(terminal())
    try:  #identificar se é um break
        tree['sonNodes'].append(bbool())
    except:
        return tree
    tree['sonNodes'].append(terminal())
    tree['sonNodes'].append(terminal())
    tree['sonNodes'].append(stmt())
    if output[num]['tag'] in tags2:
        tree['sonNodes'].append(terminal())
        tree['sonNodes'].append(stmt())
    return tree


def stmts():
    if (output[num]['tag'] not in tags1) and (output[num]['tag'] not in tags2):
        tree = {'node': 'stmts', 'sonNodes': [stmts(),stmt()]}
    else:
        tree = {'node': 'stmts','sonNodes': [terminal()]}
    return tree


def block():
    global num, gdecls
    tree = {'node':'block','sonNodes': [output[num]]}
    num += 1
    tree['sonNodes'].append(decls())
    tree['sonNodes'].append(stmts())
    tree['sonNodes'].append(output[num])
    return tree


def program():
    tree = {'node': 'program', 'sonNodes': [block()]}
    return tree


def parser(lexico):
    global output
    output = lexico.copy()
    root = program()
