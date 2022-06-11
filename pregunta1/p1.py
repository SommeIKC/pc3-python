
def fraccion_enteros():
    try:
        variable_x=int(input("Ingrese el primer numero (X):"))
        variable_y=int(input("Ingrese el segundo numero (Y):"))
        if(variable_y<variable_x)and(variable_y!=0):
            print("X debe ser mayor que Y")
            fraccion_enteros()
        else:
            division=variable_x/variable_y
            division=round(division,2)
            if(1>=division>0.99):
                print("F")
            elif(division<0.01):
                print("E")
            else:
                print(f"{division*100}%")
    except ValueError:
        print("Deben ser enteros, vuelva a intentarlo")
        fraccion_enteros()
    except ZeroDivisionError:
        print("Y debe ser diferente de cero, vuelva a intentarlo")
        fraccion_enteros()
    
fraccion_enteros()  