class Alumno:
    def __init__(self,nombre,num_registro) -> None:
        self.nombre=nombre
        self.num_registro=num_registro
    def Display(self):
        print(f'''
        Estudiante : {self.nombre}
        N° de registro: {self.num_registro}
        ''')
    def setAge(self,edad):
        self.edad=edad
        print(f"Edad asignada {self.edad}")
    def setNota(self,*notas):
        self.notas=[notas]
        print(f"Notas asignadas {self.notas}")
alumno1=Alumno("Ivan",15)
alumno1.setAge(18)
alumno1.setNota(18,19,20)