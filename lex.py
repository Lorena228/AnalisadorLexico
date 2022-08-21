import os
import tag

spacingChar = ['\n', '\t', ' ']
organizationChar = ['[', ']', '{', '}', '(', ')', ';']

words = []


def lertxt():
    #Essa parte é pra informar o caminho do arquivo independente onde esteja
    caminho1 = input('Onde está o seu arquivo test.txt?')
    parte = caminho1.replace('\\', '\\\\')
    arquivo = input('Qual o nome do seu arquivo? (ex.:test.txt)')
    caminho2 = caminho1 + "\\" + arquivo
    arq = []
    #Aqui o arquivo é chamado
    with open(caminho2) as teste:
        lines = teste.readlines()  #Aqui lê o arquivo e guarda na variável

    for line in lines:
        for character in line:
            arq.append(character)

    return arq


def preLexer(lex):
    return {'lexeme': lex}


def lexer():
    lex = ''
    list = []
    preLexemes = []

    arq = lertxt()
    for i, char in enumerate(arq):
        if (char in spacingChar
            ):  #identificar o espaço ou quebra de linha e segui em frente
            list.append(lex)
            lex = ''
        elif (char
              in organizationChar):  #identifica os caracteres de organização
            list.append(lex)
            list.append(char)
            lex = ''
        else:
            lex = lex + char

    listPolluted = list.copy()  #faz cópia de list
    list.clear()  #limpa a lista original

    for i in range(len(listPolluted)):  #limpa os espaços em branco
        if listPolluted[i] != '':
            list.append(listPolluted[i])

    for j in list:  #adiciona os lexemas ao dicionário
        preLexer(j)['width'] = len(preLexer(j)) #mostra o tamanho dos lexemas
        if preLexer(j)['lexeme']=='if':
            preLexer(j)['tag']=tag.IF
        elif preLexer(j)['lexeme']=='else':
            preLexer(j)['tag'] = tag.ELSE
        elif preLexer(j)['lexeme']=='false':
            preLexer(j)['tag'] = tag.FALSE
        elif preLexer(j)['lexeme'] == 'true':
            preLexer(j)['tag'] = tag.TRUE
        elif preLexer(j)['lexeme'] == 'and':
            preLexer(j)['tag'] = tag.AND
        elif preLexer(j)['lexeme'] == 'or':
            preLexer(j)['tag'] == tag.OR
        elif preLexer(j)['lexeme'] == 'do':
            preLexer(j)['tag'] == tag.DO
        elif preLexer(j)['lexeme'] == 'while':
            preLexer(j)['tag'] == tag.WHILE
        elif preLexer(j)['lexeme'] == 'float' or preLexer(j)['lexeme'] == 'bool' or preLexer(j)['lexeme'] == 'int':
            preLexer(j)['tag'] == tag.BASIC
        #elif preLexer(j)['lexeme'] == 't':
            #preLexer(j)['tag'] == tag.TEMP
        elif preLexer(j)['lexeme'] == '!=':
            preLexer(j)['lexeme']== tag.NO_EQUAL
        elif preLexer(j)['lexeme'] == 'break':
            preLexer(j)['lexeme'] == tag.BREAK
        elif preLexer(j)['lexeme'] == '>=':
            preLexer(j)['lexeme'] == tag.GREAT_EQUAL
        #elif preLexer(j)['lexeme'] == '-':
            #preLexer(j)['lexeme'] == tag.MINUS
        elif preLexer(j)['lexeme'] == '<=':
            preLexer(j)['lexeme'] == tag.LOW_EQUAL
        #elif preLexer(j)['lexeme'] == 'index':
            #preLexer(j)['lexeme'] == tag.INDEX
        #elif preLexer(j)['lexeme'] == 'for':
            #preLexer(j)['tag'] == tag.FOR
        preLexemes.append(preLexer(j))
        print(preLexemes, '\n')
    words = preLexemes





#def lerTxt():
#pathInitial = os.path.join('./')
# file = open(f'{pathInitial}\\'+'test.txt', 'r')
#arq = []

#lines = file.readlines()

#for line in lines:
#   for character in line:
#        arq.append(character)

#return arq

# Exemplo de vetor contendo os lexemes
#lexemes = ["Token: {'tag': '{'}", "Token: {'tag': 257, 'lexeme': 'int', 'width': 4}", "Token: {'tag': 264, 'lexeme': 'i'}"]

# Parte responsável por salvar os tokens em um arquivo
# path = os.path.join('./')
# #saveFile = open(f'{path}\\'+'output.txt', 'w')
# for i in range(len(lexemes)):
#     saveFile.writelines(lexemes[i]+'\n')
# saveFile.close()

# # Exibe os tokens contidos no arquivo em print's
# output = open('output.txt', 'r')
# lines = output.readlines()
# for line in lines:
#     print(line.strip())
