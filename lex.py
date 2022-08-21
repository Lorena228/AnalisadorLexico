import os
import tag

spacingChar = ['\n', '\t', ' ']
organizationChar = ['[', ']', '{', '}', '(', ')', ';']

words = []


def lertxt():
    global spacingChar
    #Essa parte é pra informar o caminho do arquivo independente onde esteja
    caminho1 = input('Onde está o seu arquivo test.txt?')
    #parte = caminho1.replace('\\', '\\\\')
    arquivo = input('Qual o nome do seu arquivo? (ex.:test.txt)')
    caminho2 = caminho1 + "\\" + arquivo
    #caminho2 = caminho1 + "/" + arquivo
    arq = []
    #Aqui o arquivo é chamado
    file = open(caminho2)
    lines = file.readlines()  #Aqui lê o arquivo e guarda na variável
    for char in spacingChar:
        for line in lines:
            if line.startswith(char):
                lines[lines.index(line)] = line.replace(char, '')
            if line.endswith(char):
                lines[lines.index(line)] = line.replace(char, '')

    for line in lines:
        for character in line:
            arq.append(character)

    return arq


def preLexer(lex):
    if (lex.isdigit()):
        procurado = lex.find('.')  #verifica se existe '.' no número
        if (procurado > -1 and procurado <
            (len(lex) - 1)):  #se existir retorna a posição do '.'
            return {'value': float(lex)}
        elif (procurado == -1):  #se não existir retorna -1
            return {'value': int(lex)}
        else:
            print('Erro!')
            exit()
    return {'lexeme': lex}


def newTag(token):
    if ('lexeme' in token.keys()):
        if token['lexeme'] == 'if':
            token['tag'] = tag.IF
        elif token['lexeme'] == 'else':
            token['tag'] = tag.ELSE
        elif token['lexeme'] == 'false':
            token['tag'] = tag.FALSE
        elif token['lexeme'] == 'true':
            token['tag'] = tag.TRUE
        elif token['lexeme'] == 'and':
            token['tag'] = tag.AND
        elif token['lexeme'] == 'or':
            token['tag'] = tag.OR
        elif token['lexeme'] == 'do':
            token['tag'] = tag.DO
        elif token['lexeme'] == 'while':
            token['tag'] = tag.WHILE
        #width
        elif token['lexeme'] == 'float':
            token['width'] = 8
            token['tag'] = tag.BASIC
        elif token['lexeme'] == 'int':
            token['width'] = 4
            token['tag'] = tag.BASIC
        elif token['lexeme'] == 'char':
            token['width'] == 1
            token['tag'] = tag.BASIC
        #end_width
        elif token['lexeme'] == '!=':
            token['tag'] = tag.NO_EQUAL
        elif token['lexeme'] == 'break':
            token['tag'] = tag.BREAK
        elif token['lexeme'] == '>=':
            token['tag'] = tag.GREAT_EQUAL
        elif token['lexeme'] == '<=':
            token['tag'] = tag.LOW_EQUAL
        elif token['lexeme'] == '=' or token['lexeme'] == '>' or token[
                'lexeme'] == '<':  #Esses símbolos são a própria tag
            token['tag'] = token['lexeme']
            token.pop('lexeme')
        elif token['lexeme'] == '[' or token['lexeme'] == ']' or token[
                'lexeme'] == '{' or token['lexeme'] == '}' or token[
                    'lexeme'] == '(' or token['lexeme'] == ')' or token[
                        'lexeme'] == ';':
            token['tag'] = token['lexeme']
            token.pop('lexeme')
        else:
            token['tag'] = tag.ID
    elif ('value' in token.keys()):  #Verifica se tem a chave 'value'
        if (isinstance(token['value'], int)):
            token['tag'] = tag.NUM
        else:
            token['tag'] = tag.REAL
    return token  #Token pronto


def lexer():
    global spacingChar
    lex = ''
    list = []
    preLexemes = []

    arq = lertxt()

    for i, char in enumerate(arq):
        if (char == spacingChar[2]):  #identifica o espaço, formas as palavras
            list.append(lex)
            lex = ''
        elif (char
              in organizationChar):  #identifica os caracteres de organização
            list.append(lex)
            list.append(char)
            lex = ''
        else:
            lex = lex + char

    roda = True

    while (roda):  #elima os espaços em branco
        if ('' in list):
            index = list.index('')
            list.pop(index)
        else:
            roda = False

    for j in list:
        token = preLexer(j)
        token = newTag(token)  #Amazena o token pronto na variável token
        preLexemes.append(token)  #Adiciona o token na lista preLexemes

    for cont in preLexemes:
        print(cont, '\n')
    words = preLexemes


# Parte responsável por salvar os tokens em um arquivo
#path = os.path.join('./')
# #saveFile = open(f'{path}\\'+'output.txt', 'w')
# for i in range(len(lexemes)):
#     saveFile.writelines(lexemes[i]+'\n')
# saveFile.close()

# # Exibe os tokens contidos no arquivo em print's
# output = open('output.txt', 'r')
# lines = output.readlines()
# for line in lines:
#     print(line.strip())

# Exemplo de vetor contendo os lexemes
#lexemes = ["Token: {'tag': '{'}", "Token: {'tag': 257, 'lexeme': 'int', 'width': 4}", "Token: {'tag': 264, 'lexeme': 'i'}"]