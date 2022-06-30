from tkinter import *
from tkinter import ttk,font,messagebox


class Aplicacion():
    __ventana=None
    __altura=None
    __peso=None
    __imc=None
    __imcTexto=None
    def __init__(self):
        #Creación de la ventana
        self.__ventana = Tk()
        self.__ventana.title("IMC")
        self.__ventana.geometry("500x200+500+300")
        self.__ventana.resizable(0,0)

        #Definición de elementos
        self.fuente = font.Font(weight='bold')
        
        self.__altura=DoubleVar()
        self.__peso=IntVar()
        self.__imc=StringVar()
        self.__imcTexto=StringVar()
        self.marco1=ttk.Frame(self.__ventana,borderwidth=2)
        self.lblEncabezado=ttk.Label(self.marco1,text="Calculadora de IMC",background='#EDEDED')

        self.marcoAltura=ttk.Frame(self.marco1,borderwidth=6)
        self.cAltura = ttk.Entry(self.marcoAltura, textvariable=self.__altura,width=30)
        self.lblAltura=ttk.Label(self.marcoAltura,text="Altura")
        self.lblEtqCM=ttk.Label(self.marcoAltura,text="m",background="#EDEDED")

        self.separ1 = ttk.Separator(self.marco1, orient="horizontal")

        self.marcoPeso=ttk.Frame(self.marco1,borderwidth=6)
        self.cPeso= ttk.Entry(self.marcoPeso, textvariable=self.__peso,width=30)
        self.lblPeso=ttk.Label(self.marcoPeso,text="Peso")
        self.lblEtqKG=ttk.Label(self.marcoPeso,text="kg",background="#EDEDED")
        
        self.separ2 = ttk.Separator(self.marco1, orient="horizontal")
        
        ttk.Style().configure("TButton",foreground="#006400")
        self.btCalcular=ttk.Button(self.marco1,text='Calcular',command=self.calcular)    
        self.btLimpiar=ttk.Button(self.marco1,text='Limpiar',command=self.limpiar)

        self.separ3 = ttk.Separator(self.marco1, orient="horizontal")

        ttk.Style().configure("BG.TFrame",background="#8FBC8F")
        ttk.Style().configure("BG.TLabel",foreground="#006400",background="#8FBC8F")
        self.marco2=ttk.Frame(self.__ventana,style="BG.TFrame")
        self.lblResultado=ttk.Label(self.marco2,text="Tu indice de masa corporal es: ",style="BG.TLabel")
        self.lblIndice=ttk.Label(self.marco2,textvariable=self.__imc,style="BG.TLabel",font=font.Font(weight='bold',size=10))
        self.lblTipoPeso=ttk.Label(self.marco2,textvariable=self.__imcTexto,font=font.Font(size=18),style="BG.TLabel",border=5)

        #UBICACION DE LOS ELEMENTOS
        self.marco1.pack(side="top")
        self.lblEncabezado.pack(side="top")

        self.marcoAltura.pack(side='top',fill="both",expand=True)
        self.lblAltura.pack(side="left")
        self.cAltura.pack(side="left",fill="both",expand=True)
        self.lblEtqCM.pack(side="right")

        self.separ1.pack(side="top",fill="both",expand=True)

        self.marcoPeso.pack(side="top",fill="both",expand=True)
        self.lblPeso.pack(side="left")
        self.cPeso.pack(side="left",fill="both",expand=True)
        self.lblEtqKG.pack(side="right")
        
        self.separ2.pack(side='top',fill="both",expand=True)
        
        self.btCalcular.pack(side='left',anchor='w',padx=50)
        self.btLimpiar.pack(side='right',padx=10)

        self.separ3.pack(side='top',fill="both",expand=True)

        self.marco2.pack(side='bottom',pady=10)
        self.lblTipoPeso.pack(side='bottom')    
        self.lblResultado.pack(side='left',anchor="nw")
        self.lblIndice.pack(after=self.lblResultado)

        #Limpia las entradas
        self.limpiar()

        #ATAJOS O VINCULACIONES
        self.btCalcular.bind("<Enter>", lambda event: self.calcular())

        #FINALIZAR CON:
        self.cAltura.focus_set()
        self.__ventana.mainloop()

    def calcular(self, *args):
        if (self.cAltura.get()!='') and self.cPeso.get()!='':
            try:
                altura=float(self.cAltura.get())
                peso=int(self.cPeso.get())
                if altura!=0: 
                    imc=peso/(altura**2)
                    self.__imc.set("{:.2f} Kg/m2".format(imc))
                    if imc<18.5: self.__imcTexto.set("Peso inferior al normal")
                    elif 18.5<=imc<25: self.__imcTexto.set("Peso normal")
                    elif 25<=imc<30: self.__imcTexto.set("Peso superior al normal")
                    elif 30<=imc: self.__imcTexto.set("Peso obeso")
                
            except ValueError:
                messagebox.showerror(title='Error de tipo',
                message='Debe ingresar un valor numérico')
                self.__altura.set('')
                self.cAltura.focus()
            except ZeroDivisionError:
                messagebox.showerror(title='Error de valor',
                message='La altura no puede ser 0')
                self.__altura.set('')
                self.cAltura.focus()
        else: self.__imc.set('')

    def limpiar(self, *args):
        self.__altura.set('')
        self.__peso.set('')
        self.__imc.set('')

def testAPP():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    testAPP()