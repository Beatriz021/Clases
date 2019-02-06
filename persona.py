#crear una carpeta que se llame claases y dentro de los 
#archivos dino.py persona.py

#crear una clases Persona() que tenga como atributos nombre, edad 
#y profesión. Al instanciar la clases tiene que saludar igual que
#el dino diciendo sus atributos

class Persona:
    def __init__(self, un_nombre="",una_edad=0,una_profesion=""):
        self.nombre=un_nombre
        self.edad=una_edad
        self.profesion=una_profesion
        print("Hola!. Mi nombre es ",self.nombre,"tengo",self.edad,"soy",self.profesion)

objeto=Persona("Myrian",17,"Estudiante")