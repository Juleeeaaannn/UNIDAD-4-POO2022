import json
from pathlib import Path
from claseManejadorPersonas import ManejadorPersonas
from clasePersona import Persona
class ObjectEncoder(object):
    __pathArchivo=None
    def __init__(self, pathArchivo):
        self.__pathArchivo=pathArchivo
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='ManejadorPersonas':
                personas=d['personas']
                manejador=class_()
                for i in range(len(personas)):
                    dPersona=personas[i]
                    class_name=dPersona.pop('__class__')
                    class_=eval(class_name)
                    atributos=dPersona['__atributos__']
                    unPersona=class_(**atributos)
                    manejador.agregarPersona(unPersona)
            return manejador
    def guardarJSONArchivo(self, diccionario):
        with Path(self.__pathArchivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
    def leerJSONArchivo(self):
        with Path(self.__pathArchivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario

