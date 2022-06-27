from tkinter import *
from tkinter import ttk, messagebox
import math

class Aplicacion():
    __ventana=None
    __peso=None
    __altura=None
    __IMC=None
    __composicon=None
    def __init__(self):
        self.__ventana = Tk()
        #self.__ventana.geometry('480x160')
        self.__ventana.title('CALCULADORA IMC')
        self.__ventana.configure(bg = 'beige')
        mainframe = ttk.Frame(self.__ventana, padding="5 5 5 5")
        mainframe.grid(column=3, row=6, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=400)
        mainframe.rowconfigure(0, weight=200)
        self.__altura = StringVar()
        self.__peso = StringVar()
        self.__IMC = StringVar()
        self.__IMC.set('0')
        self.__altura.set('')
        self.__peso.set('')
        self.__composicon=StringVar()
        
        ttk.Label(mainframe, text="altura:").grid(column=0, row=1, sticky=N)
        ttk.Label(mainframe, text="cm").grid(column=2, row=1)
        self.alturaEntry = ttk.Entry(mainframe, width=50, textvariable=self.__altura)
        self.alturaEntry.grid(column=1, row=1, sticky=(N))
        

        ttk.Label(mainframe, text="peso:").grid(column=0, row=2, sticky=W)
        ttk.Label(mainframe, text="kg").grid(column=2, row=2, sticky=  N)
        self.pesoEntry = ttk.Entry(mainframe, width=50, textvariable=self.__peso)
        self.pesoEntry.grid(column=1, row=2, sticky=N)


        ttk.Label(mainframe, textvariable=self.__IMC).grid(column=1, row=5, sticky=E)
        ttk.Label(mainframe, text="Tu indice de masa corporal es:").grid(column=1, row=5, sticky=W)
        ttk.Label(mainframe, textvariable=self.__composicon).grid(column=1, row=6, sticky=N)
        ttk.Label(mainframe, text="KG/M2").grid(column=2, row=5, sticky=W)
        
        ttk.Button(mainframe, text='Calcular', command=self.calcula).grid(column=1, row=4,sticky=W)
        ttk.Button(mainframe, text='Limpiar', command=self.limpia).grid(column=1, row=4,sticky=E)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.__ventana.mainloop()
    def calcula(self,*args):
        if self.alturaEntry.get()!='' or self.pesoEntry.get()!='':
            try:
                altura=float(self.alturaEntry.get())
                peso=float(self.pesoEntry.get())
                altura=altura/100
                self.__IMC.set(math.trunc(peso/(altura**2)))
                numero=float(self.__IMC.get())
                if(numero < 18.5):
                    self.__composicon.set('Peso inferior al normal')
                elif(numero > 18.5 and numero<24.9):
                    self.__composicon.set('Normal')
                elif(numero>25.0 and numero<29.9):
                    self.__composicon.set('Peso superior al normal')
                elif(numero>30.0):
                    self.__composicon.set('Obesidad')


            except ValueError:
                messagebox.showerror(title='Error de tipo',message='Debe ingresar un valor numérico')
                self.__IMC.set('0')
        else:
            self.__IMC.set('0')
            print('hola')
    def limpia(self,*args):
        self.__altura.set('')
        self.__peso.set('')
def testAPP():
    mi_app = Aplicacion()
if __name__ == '__main__':
    testAPP()