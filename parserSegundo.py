from ast import Break
from logging import root
from mailbox import NotEmptyError
from turtle import right
import tag
# {}
# block -> closer "}" | Coisas dentro do bloco

#tokens = [
#    {'tag':'{'},
#    {'lexema':'int','tag': 257},
#    {'lexema': 'i','tag': 264},
#    {'tag': ';'},
#    {'tag':'}'}
#    ]

def endTree(root):
    root = {'node': None, 'left': None, 'right': None}


def basic(root):
    if not root['node']:
        root['node'] = 'basic'
        root['right'] = {'node': tag.ID}
    else:
        basic(root['right'])


def identifier(root):
    if not root.key('left'):
        if root['node'] == tag.ID:
            root['left'] = None
            root['right'] = None
    else:
        if root['left'] == None:
            identifier(root['right'])
        else:
            identifier(root['left'])

def bbreak(root):
    if root['node'] == None:
        root['node'] = tag.BREAK
        root['right'] = None
        root['left'] = None
    else root['right'] or root['left'] == not None:
        print('Erro de sintaxe')

def do():

def eelse():

def equal():

def ffalse():

def greatEqual():

def iif():

def index():

def lowEqual():

def minus():

def noEqual():

def num():

def oor():

def real():

def temp():

def ttrue():

def wwhile():


def parser(lexico):

    parents = []
    root = {'node': None, 'left': None, 'right': None}

    for token in lexico:
    if token['tag'] == '{':
        parents.append('[')
        endTree()
        continue
    elif token['tag'] == '}':
        parents.pop()
        continue
    elif token['tag'] == ';':
        endTree()
        continue
    elif token['tag'] == tag.BASIC:
        basic(root)
        continue
    elif token['tag'] == tag.ID:
        identifier()
    elif token['tag'] == tag.AND:
        aand()
        continue
    elif token['tag'] == tag.BREAK:
        bbreak()
        continue
    elif token['tag'] == tag.DO:
        do()
        continue
    elif token['tag'] == tag.ELSE:
        eelse()
        continue
    elif token['tag'] == tag.EQUAL:
        equal()
        continue
    elif token['tag'] == tag.FALSE:
        ffalse()
        continue
    elif token['tag'] == tag.GREAT_EQUAL:
        greatEqual()
        continue
    elif token['tag'] == tag.IF:
        iif()
        continue
    elif token['tag'] == tag.INDEX:
        index()
        continue
    elif token['tag'] == tag.LOW_EQUAL:
        lowEqual()
        continue
    elif token['tag'] == tag.MINUS:
        minus()
        continue
    elif token['tag'] == tag.NO_EQUAL:
        noEqual()
        continue
    elif token['tag'] == tag.NUM:
        num()
        continue
    elif token['tag'] == tag.OR:
        oor()
        continue
    elif token['tag'] == tag.REAL:
        real()
        continue
    elif token['tag'] == tag.TEMP:
        temp()
        continue
    elif token['tag'] == tag.TRUE:
        ttrue()
        continue
    elif token['tag'] == tag.WHILE:
        wwhile()
        continue
