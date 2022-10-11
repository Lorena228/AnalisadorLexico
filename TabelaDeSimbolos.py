# NESTE CÓDIGO É ULTILIZADO A ESTRUTURA DE PILHA
stackInitial = []
indexStack = -1

# FUNÇAO RESPONSÁVEL POR ALOCAR UM LISTA PARA DETERMINADOR ESCOPO
# O PARAMÊTRO newStack DIZ RESPEITO A SER UMA NOVA LISTA (REPRESENTA O ESCOPO) SERÁ CRIADA
def allocate(newStack):
    global stackInitial

    if (newStack):
        global indexStack

        stackInitial.append([])
        indexStack = indexStack + 1
    
    return indexStack

# FUNÇÃO RESPONSÁVEL POR ADICIONAR ELEMENTOS A TABELA DE SÍMBOLOS DE DETERMINADO ESCOPO
# O PARAMÊTRO index INDICA O ESCOPO (LISTA) ONDE DEVE SER INSERIRO O SÍMBOLO
# O PARAMÊTRO name INDICA O NOME DO SÍMBOLO
# O PARAMÊTRO attribute INDICA O ATRIBUTO DO SÍMBOLO
def addInStack(index, name, attribute):
    global stackInitial

    stackInitial[index].append({"name": name, "attribute": attribute})

# FUNÇÃO RESPONSÁVEL POR REMOVER ELEMENTOS DA TABELA DE SÍMBOLOS DE DETERMINADO ESCOPO
# O PARAMÊTRO index INDICA O ESCOPO (LISTA) ONDE DEVER SER REMOVIDO O SÍMBOLO
# O PARAMÊTRO name INDICA O NOME DO SÍMBOLO QUE DEVE SER REMOVIDO
def removeInStack(index, name):
    global stackInitial
    
    for i in stackInitial[index]:
        if (i["name"] == name):
            stackInitial[index].remove(i)

# FUNÇÃO RESPONSÁVEL POR DETERMINAR SE UM SÍMBOLO PODE SER INSERIDO OU NÃO
# O PARAMÊTRO index INDICA O ESCOPO (LISTA) ONDE DEVE SER INSERIRO O SÍMBOLO
# O PARAMÊTRO name INDICA O NOME DO SÍMBOLO
# O PARAMÊTRO attribute INDICA O ATRIBUTO DO SÍMBOLO
def insert(index, name, attribute):
    global stackInitial

    if (len(stackInitial[index]) > 0):
        for i in stackInitial[index]:
            if (i["name"] == name):
                print("Multiple defined names")
                return False
        addInStack(index, name, attribute)
    else:
        addInStack(index, name, attribute)

# FUNÇÃO RESPONSÁVEL POR DETERMINAR SE UM SÍMBOLO PODE SER INSERIDO OU NÃO
# O PARAMÊTRO index INDICA O ESCOPO (LISTA) ONDE DEVER SER REMOVIDO O SÍMBOLO
# O PARAMÊTRO name INDICA O NOME DO SÍMBOLO QUE DEVE SER REMOVIDO
def delete(index, name):
    global stackInitial

    for i in stackInitial[index]:
        if (i["name"] == name):
            removeInStack(index, name)

# FUNÇÃO RESPONSÁVEL PELA PROCURA DE UM SÍMBOLO NA TEBELA DE SÍMBOLOS
# O PARAMÊTRO stack E A TABELA EM SÍ (LISTA INCIAL)
# O PARAMÊTRO name INDICA O NOME DO SÍMBOLO A SER ENCONTRADO
def lookup(stack, name):
    for i in reversed(range(len(stack))):
        for j in reversed(range(len(stack[i]))):
            if (stack[i][j]["name"] == name):
                return stack[i][j]
    print("use of the undeclared name")
    return False

# FUNÇÃO RESPONSÁVEL POR UNIR TODAS AS FUNÇÕES ACIMA EM UM SÓ CHAMADA
# O PARAMÊTRO newStack DIZ RESPEITO A SER UMA NOVA LISTA (REPRESENTA O ESCOPO) SERÁ CRIADA
# O PARAMÊTRO command DIZ RESPEITO AO COMANDO QUE SERÁ REALIZADO (INSERIR OU REMOVER)
# O PARAMÊTRO name INDICA O NOME DO SÍMBOLO
# O PARAMÊTRO attribute INDICA O ATRIBUTO DO SÍMBOLO
def main(newStack, command, name, attribute):
    
    index = allocate(newStack)
    if (command == 'insert'):
        insert(index, name, attribute)
    elif (command == 'delete'):
        delete(index, name)
