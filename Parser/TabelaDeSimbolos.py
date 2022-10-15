stackInitial = []
indexStack = -1

def allocate(newStack):
    global stackInitial

    if (newStack):
        global indexStack

        stackInitial.append([])
        indexStack = indexStack + 1
    
    return indexStack

def addInStack(index, name, attribute):
    global stackInitial

    stackInitial[index].append({"name": name, "attribute": attribute})

def removeInStack(index, name):
    global stackInitial
    
    for i in stackInitial[index]:
        if (i["name"] == name):
            stackInitial[index].remove(i)

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

def delete(index, name):
    global stackInitial

    for i in stackInitial[index]:
        if (i["name"] == name):
            removeInStack(index, name)

def lookup(stack, name):
    for i in reversed(range(len(stack))):
        for j in reversed(range(len(stack[i]))):
            if (stack[i][j]["name"] == name):
                return stack[i][j]
    print("use of the undeclared name")
    return False


def main(newStack, command, name, attribute):
    
    index = allocate(newStack)
    if (command == 'insert'):
        insert(index, name, attribute)
    elif (command == 'delete'):
        delete(index, name)

main(True, 'insert', 'a', {'size': 81})
main(False, 'insert', 'b', {'size': 8})
main(False, 'insert', 'b', {'size': 8})
main(False, 'insert', 'c', {'size': 8})

main(True, 'insert', 'a', {'size': 82})
main(False, 'insert', 'b', {'size': 8})
main(False, 'insert', 'b', {'size': 8})
main(False, 'insert', 'c', {'size': 8})

main(True, 'insert', 'a', {'size': 83})
main(False, 'insert', 'b', {'size': 8})
main(False, 'insert', 'b', {'size': 8})
main(False, 'insert', 'c', {'size': 8})

main(True, 'insert', 'a', {'size': 84})
main(False, 'insert', 'b', {'size': 8})
main(False, 'insert', 'b', {'size': 8})
main(False, 'insert', 'c', {'size': 8})

main(True, 'insert', 'a', {'size': 85})
main(False, 'insert', 'b', {'size': 8})
main(False, 'insert', 'b', {'size': 8})
main(False, 'insert', 'c', {'size': 8})

print(stackInitial)

print(lookup(stackInitial, 'a'))
