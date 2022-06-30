from clasePersona import Persona
class ManejadorPersonas:
    indice=0
    __personas=None

    def __init__(self):
        self.__personas=[]

    def agregarPersona(self, persona):
        persona.rowid=ManejadorPersonas.indice
        ManejadorPersonas.indice+=1
        self.__personas.append(persona)

    def getListaPersonas(self):
        return self.__personas

    def deletePersona(self, persona):
        #indice=self.obtenerIndicePersona(persona)
        indice=self.__personas.index(persona) #busca la persona en la lista de personas
        self.__personas.pop(indice) #elimina a la persona en el indice encontrado

    def updatePersona(self, persona):#Actualiza a una persona
        indice=self.obtenerIndicePersona(persona)
        self.__personas[indice]=persona
        
    def obtenerIndicePersona(self, persona):#busca el indice de la persona que recibe como parametro
        bandera = False
        i=0
        while not bandera and i < len(self.__personas):
            if self.__personas[i].rowid == persona.rowid:
                bandera=True
            else:
                i+=1
        return i
        
    def mostrarPersonas(self):#Muestra las personas
        for persona in self.__personas: #REcorre la lista de personas
            print(persona.getNombre(),persona.getApellido())

    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                personas=[persona.toJSON() for persona in self.__personas]
                )
        return d

