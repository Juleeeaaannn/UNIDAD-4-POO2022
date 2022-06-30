from clasePersona import Persona
from claseObjectEncoder import ObjectEncoder
from claseManejadorPersonas import ManejadorPersonas

class RespositorioPersonas(object): #Lee y actualiza el archivo JSON que contiene la informacion de todas las personas
    __conn=None
    __manejador=None
    def __init__(self, conn):
        self.__conn = conn
        diccionario=self.__conn.leerJSONArchivo()
        self.__manejador=self.__conn.decodificarDiccionario(diccionario)

    def to_values(self, persona):
        return persona.getApellido(), persona.getNombre(), persona.getEmail(), persona.getTelefono()

    def obtenerListaPersonas(self):
        return self.__manejador.getListaPersonas()

    def agregarPersona(self, persona):
        self.__manejador.agregarPersona(persona)
        return persona

    def modificarPersona(self, persona):
        self.__manejador.updatePersona(persona)
        return persona

    def borrarPersona(self, persona):
        self.__manejador.deletePersona(persona)

    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())
