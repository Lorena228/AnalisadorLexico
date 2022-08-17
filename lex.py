def lexer():
    #Essa parte é pra informar o caminho do arquivo independente onde esteja
    caminho1 = input('Onde está o seu arquivo test.txt?')
    parte = caminho1.replace('\\', '\\\\')
    arquivo = input('Qual o nome do seu arquivo? (ex.:test.txt)')
    caminho2 = caminho1 + "\\" + arquivo
    #Aqui o arquivo é chamado
    with open(caminho2) as teste:
        ""
