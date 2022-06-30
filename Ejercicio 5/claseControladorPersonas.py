from vistaPersonas import PersonasView, NewPersona
from claseManejadorPersonas import ManejadorPersonas

class ControladorPersonas(object):
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.personas = list(repo.obtenerListaPersonas())
    # comandos de que se ejecutan a través de la vista

    def crearPersona(self):
        nuevoPersona = NewPersona(self.vista).show()
        if nuevoPersona:
            persona = self.repo.agregarPersona(nuevoPersona)
            self.personas.append(persona)
            self.vista.agregarPersona(persona)

    def seleccionarPersona(self, index):
        self.seleccion = index
        persona = self.personas[index]
        self.vista.verPersonaEnForm(persona)

    def modificarPersona(self):
        if self.seleccion==-1:
            return
        rowid = self.personas[self.seleccion].rowid
        detallesPersona = self.vista.obtenerDetalles()
        detallesPersona.rowid = rowid
        persona = self.repo.modificarPersona(detallesPersona)
        self.personas[self.seleccion] = persona
        self.vista.modificarPersona(persona, self.seleccion)
        self.seleccion=-1

    def borrarPersona(self):
        if self.seleccion==-1:
            return
        persona = self.personas[self.seleccion]
        self.repo.borrarPersona(persona)
        self.personas.pop(self.seleccion)
        self.vista.borrarPersona(self.seleccion)
        self.seleccion=-1

    def start(self):
        for c in self.personas:
            self.vista.agregarPersona(c)
        self.vista.mainloop()
        
    def salirGrabarDatos(self):
        self.repo.grabarDatos()
