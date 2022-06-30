import re
class Persona:
    telefonoRegex = re.compile(r"\([0-9]{3}\)[0-9]{7}")

    __apellido=None
    __nombre=None
    __email=None
    __altura=None
    __peso=None
    def __init__(self, apellido, nombre,telefono,altura,peso): 
        self.__apellido=self.requerido(apellido, 'Apellido es un valor requerido')
        self.__nombre = self.__nombre=self.requerido(nombre, 'Nombre es un valor requerido')
        self.__telefono = self.formatoValido(telefono, Persona.telefonoRegex, 'Teléfono no tiene formato correcto')
        self.__altura = self.requerido(altura, 'Altura es un valor requerido')
        self.__peso = self.requerido(peso, 'Peso es un valor requerido')

    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getTelefono(self):
        return self.__telefono
    def getAltura(self):
        return self.__altura
    def getPeso(self):
        return self.__peso
    def getIMC(self):
        return self.__peso/(self.__altura**2)

    def requerido(self, valor, mensaje): #Verifica que se haya ingresado un valor o lanza error
        if not valor:
            raise ValueError(mensaje)
        return valor

    def formatoValido(self, valor, regex, mensaje):#Valida el formato del numero de telefono ingresado
        if not valor or not regex.match(valor):
            raise ValueError(mensaje)
        return valor

    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                                    apellido=self.__apellido,
                                    nombre=self.__nombre,
                                    telefono=self.__telefono,
                                    altura=self.__altura,
                                    peso=self.__peso
                                )
                )
        return d

