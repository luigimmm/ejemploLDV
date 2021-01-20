class Person:
    nombre=""
    edad=1
    def __init__(self) -> None:
        self.edad = 18
        self.registo = 0
        print("Primera funcion")
    
    def hablar(self,msg):
        print(self.nombre+": "+msg)

class Estudiante(Person):
    nivel="Primaria"
    
    def __init__(self,nivel="Primaria") -> None:        
        super().__init__()
        self.nivel=nivel
        if self.nivel=="Primaria":
            self.edad=6
        
        
    def estudiar(self):
        self.hablar("Estudio que estudio")


elEstudiante=Estudiante()
elEstudiante.nombre = "Luis"

elEstudiante.hablar("Hola a todos!!")
print(elEstudiante.edad)
elEstudiante.estudiar()


