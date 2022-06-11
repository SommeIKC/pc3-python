


from math import sqrt


class Punto:
    eje_x=0
    eje_y=0
    
    def __init__(self,*args) :
        for i in range(len(args)):
            if(i==0):
                self.eje_x=args[i]
                self.eje_y=0
            elif(i==1):
                self.eje_y=args[i]
            
    def __str__(self):
        return (f"({self.eje_x},{self.eje_y})")
    def cuadrante(self):
        if(self.eje_x==0 and self.eje_y==0):
            print("Esta sobre el origen")
        elif(self.eje_x==0  and self.eje_y!=0):
            print("Esta sobre el eje Y")
        elif(self.eje_x!=0 and self.eje_y==0):
            print("Esta sobre el eje X")
        elif(self.eje_x>0 and self.eje_y>0):
            print("Esta en el I cuadrante")
        elif(self.eje_x<0 and self.eje_y>0):
            print("Esta en el II cuadrante")
        elif(self.eje_x<0 and self.eje_y<0):
            print("ESta en el III cuadrante")
        else:
            print("Esta en el IV cuadrante")
    def vector(self, punto):
        vector1=Punto()
        if (isinstance(punto,Punto)):
            type(punto)==Punto
            vector1.eje_x=punto.eje_x - self.eje_x
            vector1.eje_y=punto.eje_y - self.eje_y
            print(vector1)
    def distancia(self,punto):
        if (isinstance(punto,Punto)):
            type(punto)==Punto
            print(f"La distancia es: {sqrt(pow((punto.eje_x - self.eje_x),2)+pow((punto.eje_y - self.eje_y),2))}")
class Rectangulo:
    punto1=Punto(0,0)
    punto2=Punto(0,0)
    def __init__(self,*args) -> None:
        for i in range(len(args)):
            if(i==0 and isinstance(args[i],Punto)):
                self.punto1=args[i]    
                self.punto2=Punto(0,0)
            elif(i==1 and isinstance(args[i],Punto)):
                self.punto2=args[i]
    def base(self):
        self.base=abs(self.punto2.eje_x - self.punto1.eje_x)
        print(f"la base es: {self.base}")
    def altura(self):
        self.altura=abs(self.punto2.eje_y - self.punto1.eje_y)
        print(f"la altura es: {self.altura}")
    def area(self):
        self.area=self.altura*self.base
        print(f"El area es : {self.area}")
a=Punto(2,3)
b=Punto(5,5)
c=Punto(-3,-1)
d=Punto()
a.cuadrante()
c.cuadrante()
d.cuadrante()
a.vector(b)
b.vector(a)
rectangulo1=Rectangulo(a,b)
rectangulo1.base()
rectangulo1.altura()
rectangulo1.area()