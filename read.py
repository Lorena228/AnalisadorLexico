import os

def lerTxt():
    pathInitial = os.path.join('./')
    file = open(f'{pathInitial}\\'+'test.txt', 'r')
    arq = []

    lines = file.readlines()

    for line in lines:
        for character in line:
            arq.append(character)

    return arq