import Lexer.lex as lex
import Parser.parser1 as parser1


def main():
    lexico = lex.lexer()
    sintatico = parser1.parser(lexico)


main()
