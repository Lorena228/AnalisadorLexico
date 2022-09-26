from ast import Num
from re import match


def program():
    match("block")

def block():
    match("decls")
    match("stmts")


def decls():
    if(token == ''):
        match("decls")
        match("decl")
    elif(token == ''):
        match("∈")

def decl():
    type(id)

def type():
    if(token == ''):
        match("type(Num)")
    elif(token == ''):
        match("basic")

def stmts():
    if(token == ''):
        stmts()
        stmt()

def stmt():  #PEDIR ORIENTAÇÃO
    if(token == ''):
        match("loc[bool]")
    elif(token == ''):
        if(bool):
            match("stmt")
        elif():
            match("stmt")
    elif(token == ''):
        while(bool):
            match("stmt")
    elif(token == ''):
        match("break")
    elif(token == ''):
        match("block")

def loc():
    if(token == ''):
        match("loc[bool]")
    elif(token == ''):
        match("id")

def bool():
    if(token == ''):
        if():
            match("bool")
        if():
            match("join")
    elif(token == ''):
        match("join")

def join():
    if(token == ''):
        match("join")
        match("equality")
    elif(token == ''):
        match("equality")
    
def equality():
    if(token == ''):
        match("equality == rel")
    elif(token == ''):
        match("equality != rel")
    else:
        match("rel")

def rel():
    if(token == ''):
        match("expr < expr")
    elif(token == ''):
        match("expr <= expr")
    elif(token == ''):
        match("expr >= expr")
    elif(token == ''):
        match("expr > expr")
    elif(token == ''):
        match("expr")

def expr():
    if(token == ''):
        match("expr + term")
    elif(token == ''):
        match("expr - term")
    elif(token == ''):
        match("term")
    
def term():
    if(token == ''):
        match("term * unary")
    elif(token == ''):
        match("term / unary")
    elif(token == ''):
        match("unary")

def unary():
    if(token == ''):
        match("! unary")
    elif(token == ''):
        match("- unary")
    elif(token == ''):
        match("factor")

def factor():
    if(token == ''):
        match("(bool)")
    elif(token == ''):
        match("loc")
    elif(token == ''):
        match("num")
    elif(token == ''):
        match("real")
    elif(token == ''):
        match("true")
    elif(token == ''):
        match("false")
