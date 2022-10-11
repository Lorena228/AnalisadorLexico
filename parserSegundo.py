import tag
#pesquisar as tags Minus, Index...
#


def endTree(root):
    root = {'node': None, 'left': None, 'right': None}


def basic(root):
    if root['node'] == None:
        root['node'] = 'basic'
        root['right'] = {'node': tag.ID}
    else:
        print('erro de sintaxe')


def identifier(root):
    if not root.key('left'):
        if root['node'] == tag.ID:
            root['left'] = None
            root['right'] = None
    else:
        if root['left'] == None:
            identifier(root['right'])
        else:
            identifier(root['left'])


def parser(lexico):

    parents = []
    root = {'node': None, 'left': None, 'right': None}

    for token in lexico:
        if token['tag'] == '{' or token['tag'] == "(" or token['tag'] == "[":
            parents.append('[')
            endTree()
        elif token['tag'] == '}' or token['tag'] == ")" or token['tag'] == "]":
            parents.pop()
            endTree()
        elif token['tag'] == ';':
            endTree()
        elif token['tag'] == tag.BASIC:
            basic(root)
        elif token['tag'] == tag.ID:
            identifier()