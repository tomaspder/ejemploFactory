
class Persona(object):

    def __init__(self):
        self.nombre = None
        self.edad = None
        self.genero = None

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_genero(self):
        return self.genero

    def get_info_persona(self):
        return ("Informacion de una persona:\n1. Nombre: {n}\n2. Edad: {e}\n3. Genero: {g}".format(
            n=self.get_nombre(), e=self.get_edad(), g=self.get_genero()))

#Creo los constructores de cada genero heredando de la clase Persona
class Femenino(Persona):

    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

class Masculino(Persona):

    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero


class Factoria(object):

    def get_persona(self, nombre, genero, edad):
        if (genero == 'F'):
            return Femenino(nombre, edad, genero)
        elif (genero == 'M'):
            return Masculino(nombre, edad, genero)

#En este caso mi factory funcionaria como interfaz en la que creo un objeto persona segun sea Femenino o Masculino el genero
mi_factoria = Factoria()

persona = mi_factoria.get_persona('Guido Sanchez', 'M', 30)
print (persona.get_info_persona())

persona2 = mi_factoria.get_persona('Maria Ramos','F', 24)
print(persona2.get_info_persona())
