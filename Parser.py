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
    else:
        match("∈")

def decl():
    type(id)

def type():
    if():
        match("type(Num)")
    else:
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
    
def equality:
