from ast import Num
from re import match


def program():
    match("block")

def block():
    match("decls")
    match("stmts")


def decls():
    if():
        match("decls")
        match("decl")
    elif():
        match("∈")

def decl():
    type(id)

def type():
    if():
        match("type(Num)")
    elif():
        match("basic")

def stmts():
    if():
        stmts()
        stmt()

def stmt():  #PEDIR ORIENTAÇÃO
    if():
        match("loc[bool]")
    elif():
        if(bool):
            match("stmt")
        elif():
            match("stmt")
    elif():
        while(bool):
            match("stmt")
    elif():
        match("break")
    elif():
        match("block")

def loc():
    if():
        match("loc[bool]")
    elif():
        match("id")

def bool():
    if():
        if():
            match("bool")
        if():
            match("join")
    elif():
        match("join")

def join():
    if():
        match("join")
        match("equality")
    elif():
        match("equality")
    
def equality():
    if():
        match("equality == rel")
    elif():
        match("equality != rel")
    else:
        match("rel")

def rel():
    if():
        match("expr < expr")
    elif():
        match("expr <= expr")
    elif():
        match("expr >= expr")
    elif():
        match("expr > expr")
    elif():
        match("expr")

def expr():
    if():
        match("expr + term")
    elif():
        match("expr - term")
    elif():
        match("term")
    
def term():
    if():
        match("term * unary")
    elif():
        match("term / unary")
    elif():
        match("unary")

def unary():
    if():
        match("! unary")
    elif():
        match("- unary")
    elif():
        match("factor")

def factor():
    if():
        match("(bool)")
    elif():
        match("loc")
    elif():
        match("num")
    elif():
        match("real")
    elif():
        match("true")
    elif():
        match("false")
