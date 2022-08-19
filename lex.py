import os

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
