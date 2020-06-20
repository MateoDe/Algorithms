import random

def binary_search(lista, beginning, end, objective, counter):
    counter = counter + 1
    print(f'Step: {counter}')
    if beginning > end:
        return False
    
    middle = (beginning + end) // 2

    if lista[middle] == objective:
        return True
    elif lista[middle] < objective:
        return binary_search(lista, middle + 1, end, objective, counter)
    else:
        return binary_search(lista, beginning, middle - 2, objective, counter)


if __name__ == '__main__':
    size_of_the_list = int(input('What size does the list have: '))
    objective = int(input('What number is your objective? '))

    lista = sorted([random.randint(0, 100) for i in range(size_of_the_list)]) #The sorted list is created 

    found = binary_search(lista, 0, len(lista), objective, 0)

    print(lista)
    print(f'The element {objective} {"is" if found else "was not found"} in the list')