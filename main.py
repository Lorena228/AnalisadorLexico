import lex
import parserSegundo


def main():
    lexico = lex.lexer()
    sintatico = parserSegundo.parser(lexico)


main()
