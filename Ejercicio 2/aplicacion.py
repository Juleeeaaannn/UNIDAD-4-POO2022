from tkinter import *
from tkinter import ttk,font,messagebox
import tkinter as tk


class Aplicacion():
    __ventana=None
    __preciobase=None
    __iva=None
    __preciofinal=None

    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.geometry("300x250")
        self.__ventana.title("Cálculo de IVA")

        mainframe = ttk.Frame(self.__ventana)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe['borderwidth'] = 2

        self.__preciobase=tk.IntVar()
        self.__iva=tk.IntVar()
        self.__preciofinal=tk.IntVar

        ttk.Label(mainframe, text= "Precio sin IVA").grid(column=0, row=0, pady=10, padx=30, sticky=(W))
        ttk.Label(mainframe, text= "IVA").grid(column=0, row=3, pady=10, padx=30, sticky=(W))
        ttk.Label(mainframe, text= "Precio con IVA").grid(column=0, row=4, pady=10, padx=30, sticky=(W))

        ttk.Radiobutton(mainframe, text='IVA 21%', value=0, variable=self.__iva, command=self.obtenerIVA()).grid(row =1, column=0, columnspan=1, pady=5, padx=30, sticky='w')
        ttk.Radiobutton(mainframe, text='IVA 10,5%', value=1, variable=self.__iva, command=self.obtenerIVA()).grid(row =2, column=0, columnspan=1, pady=5, padx=30,sticky='w')

        self.preciobEntry = ttk.Entry(mainframe, width=15, textvariable=self.__preciobase)
        self.preciobEntry.grid(column=1, row=0, padx=30, pady=10, sticky=(E))
        self.ivaEntry = ttk.Entry(mainframe, width=15, textvariable=self.__iva)
        self.ivaEntry.grid(column=1, row=3, padx=30, pady=10, sticky=(E))
        self.preciofEntry = ttk.Entry(mainframe, width=15,textvariable= self.__preciofinal)
        self.preciofEntry.grid(column=1, row=4, padx=30, pady=10, sticky=(E))

        ttk.Button(mainframe, text="Calcular", command=self.cPrecioFinal()).grid(column=0, row=5, padx=30, pady=10, sticky=W)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=1, row=5, padx=30, pady=10)

        self.__ventana.mainloop()

    def obtenerIVA(self, *args):
        preciobase = int(self.preciobEntry.get())
        if self.__iva == 0:
            self.__iva.set((21*preciobase)/100)
        else:
            self.__iva.set((10.5*preciobase)/100)

    def cPrecioFinal(self):
        self.__preciofinal.set(self.preciofEntry.get()+self.ivaEntry.get())

def testAPP():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    testAPP()