from clasePersona import Persona
from claseManejadorPersonas import ManejadorPersonas
from claseObjectEncoder import ObjectEncoder

def testPersonas(manejadorC): #Crea el archivo Json y lo carga
    persona1=Persona('Rueda', 'Melisa','(264)4777222',182,65)
    persona2=Persona('López', 'Carlos','(261)4888111',175,75)
    persona3=Persona('Pérez', 'Maira', '(264)5111222',192,102)
    persona4=Persona('Altamirano', 'Sandra','(263)6478912',165,74)
    persona5=Persona('Artime', 'Luis', '(264)4558699',162,86)
    manejadorC.agregarPersona(persona1)
    manejadorC.agregarPersona(persona2)
    manejadorC.agregarPersona(persona3)
    manejadorC.agregarPersona(persona4)
    manejadorC.agregarPersona(persona5)

if __name__=='__main__':
    jF = ObjectEncoder('personas.json')
    manejador=ManejadorPersonas()
    #testPersonas(manejador)
    diccionario=jF.leerJSONArchivo()
    manejador=jF.decodificarDiccionario(diccionario)
    manejador.mostrarPersonas()
    diccionarioManejador=manejador.toJSON()
    jF.guardarJSONArchivo(diccionarioManejador)

