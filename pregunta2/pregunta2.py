def calificaciones():
    try:
        
        numeros=input("Ingrese las notas por separacion de comas")
        lista_notas=numeros.split(',')
        for i in range(len(lista_notas)):
            lista_notas[i]=round(float(lista_notas[i]))
        return lista_notas
    except ValueError:
        print("Los valores introducidos no pueden ser convertidos debido a un error de tipeo o formato")
        calificaciones()    
print(calificaciones())
