from tkinter import *
from tkinter import ttk
import requests

class app(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Cambio a Dolar")
        self.resizable(0,0)

        self.conversion=None
        r = requests.get("https://www.dolarsi.com/api/api.php?type=dolar")
        if 200<=r.status_code<400:
            self.__datos = r.json()
            for i in range(len(self.__datos)):
                if self.__datos[i]['casa']['nombre'] == 'Oficial':
                    self.conversion = self.__datos[i]['casa']['venta']
                    self.conversion = self.conversion.replace(',', '.')
                    self.conversion = float(self.conversion)
                    break
        else: self.conversion=0
        
        self.dolar=DoubleVar()
        self.cDolares=ttk.Entry(self,textvariable=self.dolar,)
        self.cDolares.grid(row=0,column=1)
        self.dolar.trace('w',self.calcular)

        ttk.Label(self,text="Dolares").grid(row=0,column=2, pady=15, padx=15)
        ttk.Label(self,text="Pesos").grid(row=1,column=2, pady=15, padx=15)
        ttk.Label(self,text="es equivalente a:").grid(row=1,column=0, pady=15, padx=15)
        
        self.pesos=DoubleVar()
        self.cPesos=ttk.Label(self,textvariable=self.pesos).grid(row=1,column=1)
        self.calcular()
        
        ttk.Button(self,text="Salir",command=self.destroy).grid(row=2,column=2, pady=15, padx=15)
    
    def calcular(self,*args):
        if not self.conversion:
            r = requests.get('https://www.dolarsi.com/api/api.php?type=dolar')
            if 200<=r.status_code<400:
                self.__datos = r.json()
                for i in range(len(self.__datos)):
                    if self.__datos[i]['casa']['nombre'] == 'Oficial':
                        self.conversion = self.__datos[i]['casa']['venta']
                        self.conversion = self.conversion.replace(',', '.')
                        self.conversion = float(self.conversion)
                        break
            else: self.conversion=0
        if type(self.dolar.get())==float: self.pesos.set(round((float(self.conversion)*self.dolar.get()), 2))
        else:self.pesos.set(0)

def MiApp():
    app().mainloop()

if __name__=="__main__":
    MiApp()        

