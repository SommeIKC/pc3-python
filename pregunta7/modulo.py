


from random import randint



def random_numeros():
    lista=[]
    for i in range(0,20):
        a=(randint(0,100))
        lista.append(a)
    return lista
def mostrar_lista(lista: list):
    print(lista)
def ordenar_lista(lista:list):
    lista.sort()
    print(lista)
