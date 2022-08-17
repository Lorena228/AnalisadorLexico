import os

def lexer():
    #Essa parte é pra informar o caminho do arquivo independente onde esteja
    caminho1 = input('Onde está o seu arquivo test.txt?')
    parte = caminho1.replace('\\', '\\\\')
    arquivo = input('Qual o nome do seu arquivo? (ex.:test.txt)')
    caminho2 = caminho1 + "\\" + arquivo
    #Aqui o arquivo é chamado
    with open(caminho2) as teste:
        ""

    # Exemplo de vetor contendo os lexemes
    lexemes = ["Token: {'tag': '{'}", "Token: {'tag': 257, 'lexeme': 'int', 'width': 4}", "Token: {'tag': 264, 'lexeme': 'i'}"]
    
    # Parte responsável por salvar os tokens em um arquivo
    path = os.path.join('./')
    saveFile = open(f'{path}\\'+'output.txt', 'w')
    for i in range(len(lexemes)):
        saveFile.writelines(lexemes[i]+'\n')
    saveFile.close()
    
    # Exibe os tokens contidos no arquivo em print's
    output = open('output.txt', 'r')
    lines = output.readlines()
    for line in lines:
        print(line.strip())