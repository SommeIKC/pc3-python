from math import pi


class circulo:
    def __init__(self,radio) :
        self.radio=radio
    def calcular_area(self):
        print(pi*pow(self.radio,2))

circulo1=circulo(8)
circulo1.calcular_area()