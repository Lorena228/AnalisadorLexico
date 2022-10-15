import os
import Lexer.tag as tag

spacingChar = ['\n', '\t', ' ']
organizationChar = ['[', ']', '{', '}', '(', ')', ';']

words = []


def lertxt():
    global spacingChar
    #Essa parte é pra informar o caminho do arquivo independente onde esteja
    caminho = input('Onde está o seu arquivo? ->')
    #parte = caminho1.replace('\\', '\\\\')
    arquivo = input('Qual o nome do seu arquivo? (ex.:test.txt) ->')
    caminho_do_arquivo = ''
    if os.name == 'nt':
        caminho_do_arquivo = caminho + "\\" + arquivo
    elif os.name == 'posix':
        caminho_do_arquivo = caminho + "/" + arquivo #PARA LINUX
    else:
        print("ERRO: Sistema não suporta esse compilador")
    arq = [[]]
    #Aqui o arquivo é chamado
    file = open(caminho_do_arquivo)
    lines = file.readlines()  #Aqui lê o arquivo e guarda na variável
    for char in spacingChar:  #\n e \t
        for line in lines:
            if line.startswith(char):
                lines[lines.index(line)] = line.replace(char, '')
            if line.endswith(char):
                lines[lines.index(line)] = line.replace(char, '')

    num_line = 0
    for line in lines:
        for character in line:
            arq[num_line].append(character)
        arq.append([])
        num_line += 1

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


# Parte responsável por salvar os tokens em um arquivo
def saveFile():
    global words
    path = os.path.join(
        'C:\\Users\\Lgscc\\OneDrive\\Documentos\\Github Desktop\\AnalisadorLexico'
    )
    #path = os.path.join('./') PARA LUNIX
    #salva o novo arquivo nesse caminho
    saveFile = open(f'{path}\\' + 'outputLexer.txt', 'w')
    for i in range(len(words)):  #escreve as palavras no arquivo
        saveFile.write(f'Token: {words[i]} \n')
    saveFile.close()
    return saveFile.name


def exibirTokens():  # Exibe os tokens contidos no arquivo em print's
    path = os.path.join(
        'C:\\Users\\Lgscc\\OneDrive\\Documentos\\Github Desktop\\AnalisadorLexico'
    )  #abre o arquivo
    #path = os.path.join('./') PARA LUNIX
    output = open(f'{path}\\' + 'outputLexer.txt', 'r')
    lines = output.readlines()  #lê o arquivo
    output.close()
    for line in lines:  #print
        print(line.strip())

    return f'{path}\\' + 'outputLexer.txt'  #retorna o caminho


def lexer():
    global spacingChar, words
    lex = ''
    list = []

    arq = lertxt()

    num_line = 0
    for line in arq:
        num_line += 1
        list.append(f"'{num_line}'")
        for i, char in enumerate(line):
            if (char == spacingChar[2]
                ):  #identifica o espaço e formas as palavras
                list.append(lex)
                lex = ''
            elif (char in organizationChar
                  ):  #identifica os caracteres de organização
                list.append(lex)
                list.append(char)
                lex = ''
            else:
                lex = lex + char

    roda = True

    while (roda):  #elimina os espaços em branco
        if ('' in list):
            index = list.index('')
            list.pop(index)
        else:
            roda = False

    linha = 1
    for j in list:
        validador = 0
        for value in range(linha, num_line):
            if j == f"'{value}'":
                linha = value
                validador = 1
                break
        if validador == 1:
            continue
        token = preLexer(j)
        token = newTag(token)  #Amazena o token pronto na variável token
        token['line'] = linha
        words.append(token)  #Adiciona o token na lista preLexemes

    words.pop()

    return words
