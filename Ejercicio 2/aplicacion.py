from tkinter import *
from tkinter import ttk,messagebox

class Aplicacion():
    __ventana=None
    __preciobase=None
    __iva=None
    __preciofinal=None
    __cantIVA=None
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.title("Cálculo de IVA")

        mainframe = ttk.Frame(self.__ventana)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe['borderwidth'] = 2

        self.__preciobase=StringVar()
        self.__iva=StringVar()
        self.__preciofinal=StringVar()
        self.__cantIVA =StringVar()

        ttk.Label(mainframe, text= "Precio sin IVA").grid(column=0, row=0, pady=10, padx=30, sticky=(W))
        ttk.Label(mainframe, text= "IVA").grid(column=0, row=3, pady=10, padx=30, sticky=(W))
        ttk.Label(mainframe, text= "Precio con IVA").grid(column=0, row=4, pady=10, padx=30, sticky=(W))

        ttk.Radiobutton(mainframe, text='IVA 21%', variable=self.__cantIVA, value=0,command=self.obtenerIVA).grid(row =1, column=0, columnspan=1, pady=5, padx=30, sticky=W)
        ttk.Radiobutton(mainframe, text='IVA 10,5%', variable=self.__cantIVA, value=1, command=self.obtenerIVA).grid(row =2, column=0, columnspan=1, pady=5, padx=30,sticky=W)

        self.preciobEntry = ttk.Entry(mainframe, width=15, textvariable=self.__preciobase)
        self.preciobEntry.grid(column=1, row=0, padx=30, pady=10, sticky=(E))

        self.ivaEntry = ttk.Entry(mainframe, width=15, textvariable=self.__iva,state='disabled')
        self.ivaEntry.grid(column=1, row=3, padx=30, pady=10, sticky=(E))

        self.preciofEntry = ttk.Entry(mainframe, width=15,textvariable= self.__preciofinal, state='disabled')
        self.preciofEntry.grid(column=1, row=4, padx=30, pady=10, sticky=(E))

        ttk.Button(mainframe, text="Calcular", command=self.cPrecioFinal).grid(column=0, row=5, padx=30, pady=10, sticky=W)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=1, row=5, padx=30, pady=10)

        self.__ventana.mainloop()
    
    def obtenerIVA(self, *args):
        if self.preciobEntry.get()!='':
            try:
                preciobase = int(self.preciobEntry.get())
                if  self.__cantIVA.get() == '0':
                    valor=str((21*preciobase)/100)
                    self.__iva.set(valor)     
                elif self.__cantIVA.get() == '1':
                    valor=str((10.5*preciobase)/100)
                    self.__iva.set(valor)
            except ValueError:
                messagebox.showerror(title='Error de tipo',message='Debe ingresar un valor numérico')
                self.__preciobase.set('') 

    def cPrecioFinal(self):
        self.__preciofinal.set(int(self.preciobEntry.get())+float(self.__iva.get()))

    

def testAPP():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    testAPP()