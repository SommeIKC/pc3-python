class Rectangulo:
    def __init__(self,largo,ancho) -> None:
        self.largo=largo
        self.ancho=ancho
    def calcular_area(self):
        print(f"El area es {self.ancho*self.largo}")

rectangulo=Rectangulo(10,5)
rectangulo.calcular_area()