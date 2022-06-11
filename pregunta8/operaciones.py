def suma(a: float,b: float):
    try:
        print(f"{float(a)+float(b)}")
    except ValueError:
        print("Tipo de dato no valido")
def resta(a: float,b: float):
    try:
        print(f"{float(a)-float(b)}")
    except ValueError:
        print("Tipo de dato no valido")
def multiplicacion(a: float,b: float):
    try:
        print(f"{float(a)*float(b)}")
    except ValueError:
        print("Tipo de dato no valido")
def division(a: float,b: float):
    try:
        print(f"{float(a)/float(b)}")
    except ValueError:
        print("Tipo de dato no valido")
    except ZeroDivisionError:
        print("Division entre cero no existe")