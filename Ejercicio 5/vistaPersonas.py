import tkinter as tk
from tkinter import Button, Entry, Label, StringVar, Toplevel, messagebox
from clasePersona import Persona

class PersonaList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar(self, persona, index=tk.END):
        text = "{}, {}".format(persona.getApellido(), persona.getNombre())
        self.lb.insert(index, text)

    def borrar(self, index):
        self.lb.delete(index, index)

    def modificar(self, persona, index):
        self.borrar(index)
        self.insertar(persona, index)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)

class PersonaForm(tk.LabelFrame):
    fields = ("Apellido", "Nombre", "Teléfono", "Altura", "Peso")
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Persona", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()
        self.peso=StringVar(); self.entries[4].configure(textvariable=self.peso)
        self.altura=StringVar(); self.entries[3].configure(textvariable=self.altura)

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry
        
    def mostrarEstadoPersonaEnFormulario(self, persona):
        # a partir de un persona, obtiene el estado
        # y establece en los valores en el formulario de entrada
        values = (persona.getApellido(), persona.getNombre(), persona.getTelefono(),persona.getAltura(),persona.getPeso())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def crearPersonaDesdeFormulario(self):
        #obtiene los valores de los campos del formulario
        #para crear un nuevo persona
        values = [e.get() for e in self.entries]
        persona=None
        try:
            persona = Persona(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return persona
    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
    

class NewPersona(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.persona = None
        self.form = PersonaForm(self)
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)
    def confirmar(self):
        self.persona = self.form.crearPersonaDesdeFormulario()
        if self.persona:
            self.destroy()
    def show(self):
        self.grab_set()
        self.wait_window()
        return self.persona

class UpdatePersonaForm(PersonaForm):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.btn_imc = tk.Button(self, text="Ver IMC",command=self.ImcView)
        self.btn_imc["state"]="disabled"
        self.btn_save = tk.Button(self, text="Guardar")
        self.btn_delete = tk.Button(self, text="Borrar")
        self.btn_imc.pack(side='right', ipadx=5, padx=5, pady=5)
        self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
    
    def mostrarEstadoPersonaEnFormulario(self, persona):
        super().mostrarEstadoPersonaEnFormulario(persona)
        self.btn_imc["state"]="active"
    def limpiar(self):
        super().limpiar()
        self.btn_imc["state"]="disabled"

    def ImcView(self):
        ImcView=tk.Toplevel()
        imc=StringVar()
        contextura=StringVar()
        if int(self.altura.get())>0: varimc=(int(self.peso.get())/((float(self.altura.get())/100)**2))
        else: varimc=0
        imc.set("{:.2f}".format(varimc))
        cImc=tk.Entry(ImcView,textvariable=imc)
        lblImc=tk.Label(ImcView,text="Imc")

        if varimc==0: contextura.set("----")
        elif varimc<18.5: contextura.set("Peso inferior al normal")
        elif 18.5<=varimc<25: contextura.set("Peso normal")
        elif 25<=varimc<30: contextura.set("Peso superior al normal")
        elif 30<=varimc: contextura.set("Sobrepeso")
        lblCompCorp=tk.Entry(ImcView,textvariable=contextura)
        lblCompCorpText=Label(ImcView,text="Composicion Corporal")
        cImc.configure(state="readonly")
        lblCompCorp.configure(state="readonly")

        btnVolver=tk.Button(ImcView,text="Volver",command=ImcView.destroy)

        lblImc.grid(row=0,column=0)
        cImc.grid(row=0,column=1,columnspan=2)
        lblCompCorpText.grid(row=1,column=0)
        lblCompCorp.grid(row=1,column=1,columnspan=2)
        btnVolver.grid(row=2,column=1)

    def bind_save(self, callback):
        self.btn_save.config(command=callback)
    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)
        self.btn_imc["state"]="disabled"

class PersonasView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Personas")
        self.list = PersonaList(self, height=15)
        self.form = UpdatePersonaForm(self)
        self.btn_new = tk.Button(self, text="Agregar Persona")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)

    def setControlador(self, ctrl):
        #vincula la vista con el controlador
        self.btn_new.config(command=ctrl.crearPersona)
        self.list.bind_doble_click(ctrl.seleccionarPersona)
        self.form.bind_save(ctrl.modificarPersona)
        self.form.bind_delete(ctrl.borrarPersona)

    def agregarPersona(self, persona):
        self.list.insertar(persona)

    def modificarPersona(self, persona, index):
        self.list.modificar(persona, index)

    def borrarPersona(self, index):
        self.form.limpiar()
        self.list.borrar(index)

    #obtiene los valores del formulario y crea un nuevo persona
    def obtenerDetalles(self):
        return self.form.crearPersonaDesdeFormulario()
        
    #Ver estado de Persona en formulario de personas
    def verPersonaEnForm(self, persona):
        self.form.mostrarEstadoPersonaEnFormulario(persona)
