def lexer():
    caminho1 = input('Onde está o seu arquivo test.txt?')
    parte = caminho1.replace('\\', '\\\\')
    arquivo = input('Qual o nome do seu arquivo? (ex.:test.txt)')
    caminho2 = caminho1 + "\\" + arquivo
    print("Caminho:", caminho2)
    with open(caminho2) as teste:
        ""
