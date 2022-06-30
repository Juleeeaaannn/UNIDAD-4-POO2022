from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests

class app(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Cambio a Dolar")
        self.resizable(0,0)
        self.geometry("+500+200")

        self.conversion=None
        r = requests.get('https://www.dolarsi.com/api/api.php?type=dolar') #trae la info de la api y la almacena en una variable
        if 200<=r.status_code<400: # si es el codigo menor a 400 y mayor o igual que 200 es hubo exito en la carga
            self.__datos = r.json() # traemos los datos json
            for i in range(len(self.__datos)):
                if self.__datos[i]['casa']['nombre'] == 'Oficial':# trae el nombre del cambio, si es el oficial entra a la if
                    self.conversion = self.__datos[i]['casa']['venta'] #trae el valor de la venta 
                    self.conversion = self.conversion.replace(',', '.')# transformar comas en .
                    self.conversion = float(self.conversion)#cast a float
                    break
        else: self.conversion=0
        
        self.dolar=DoubleVar()
        self.cDolares=ttk.Entry(self,textvariable=self.dolar,)
        self.cDolares.grid(row=0,column=1)
        self.dolar.trace('w',self.calcular)

        ttk.Label(self,text="Dolares").grid(row=0,column=2)
        ttk.Label(self,text="Pesos").grid(row=1,column=2)
        ttk.Label(self,text="es equivalente a:").grid(row=1,column=0)
        
        self.pesos=DoubleVar()
        self.cPesos=ttk.Label(self,textvariable=self.pesos).grid(row=1,column=1)
        
        ttk.Button(self,text="Salir",command=self.destroy).grid(row=2,column=2)
    
    def calcular(self,*args):
        try:
            self.pesos.set(float(self.conversion)*self.dolar.get()) #Multilica los pesos al valor del dolar actual
        except:
            messagebox.showerror(title='Error',message='Debe ingresar un valor numérico') #Si no se ingresó un número da error
            self.dolar.set(0)

def MiApp():
    app().mainloop()

if __name__=="__main__":
    MiApp()        

