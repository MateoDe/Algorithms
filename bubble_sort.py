import random


def bubble_sort(lista):
    lenght = len(lista)

    for i in range(lenght):
        for j in range(0, lenght - i - 1):

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista


if __name__ == '__main__': 
    size_of_the_list = int(input('What size does the list have: '))

    lista = [random.randint(0, 100) for i in range(size_of_the_list)] #The sorted list is created
    print(lista)

    sorted_list = bubble_sort(lista)
    print(sorted_list)


