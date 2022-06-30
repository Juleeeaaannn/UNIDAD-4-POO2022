from tkinter import *
from tkinter import messagebox
import tkinter as tk
import requests
from ObjectEncoder import Objectencoder

class App:
    __ventana = None
    __nombre = None
    __capital = None
    __canthab = None
    __cantdptos = None
    __temperatura = None
    __senstermica = None
    __humedad = None
    __nuevaprovincia = None
    __indice = None
    __datos = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Lista de Provincias')
        self.__ventana.geometry('633x325')
        self.__ventana.resizable(0, 0)
        self.__ventana['borderwidth'] = 0
        opts = {'fill': 'both', 'expand': 'True', 'padx': '5', 'pady': '5'}

        frame = tk.Frame(self.__ventana)
        frame.pack(side=LEFT, **opts)
        self.__listbox = tk.Listbox(frame)
        self.__listbox.pack(side=LEFT, fill=Y, pady=10, ipadx=25)
        scroll = tk.Scrollbar(frame, command=self.__listbox.yview)
        scroll.pack(fill=Y, expand=True)
        self.__listbox.config(yscrollcommand=scroll.set)
        self.cargarprovincias()
        self.dobleclick(self.ponerprovincia)  # Doble click pone provincia en labelframe y la funcion agrega los datos del tiempo

        frame1 = tk.LabelFrame(self.__ventana, text='Provincia')
        frame1.pack(side=TOP, padx=0, pady=10, ipadx=35)
        frame2 = tk.Frame(self.__ventana)
        frame2.pack(side=BOTTOM, **opts)
        frame5 = tk.Frame(frame1)
        frame5.pack(side=BOTTOM, **opts)
        tk.Button(frame2, text='Agregar provincia', command=self.agregarprovvista).pack(side=TOP, pady=5)
        frame3 = tk.Frame(frame1)
        frame3.pack(side=LEFT, **opts)
        tk.Label(frame3, text='Nombre').pack(side=TOP, **opts)
        tk.Label(frame3, text='Capital').pack(side=TOP, **opts)
        tk.Label(frame3, text='Cantidad de habitantes').pack(side=TOP, **opts)
        tk.Label(frame3, text='Cantidad de departamentos/partidos').pack(side=TOP, **opts)
        tk.Label(frame3, text='Temperatura').pack(side=TOP, **opts)
        tk.Label(frame3, text='Sensación térmica').pack(side=TOP, **opts)
        tk.Label(frame3, text='Humedad').pack(side=TOP, **opts)

        frame4 = tk.Frame(frame1)
        frame4.pack(side=RIGHT, **opts)
        self.__indice = StringVar()
        self.__nombre = StringVar()
        self.__capital = StringVar()
        self.__canthab = StringVar()
        self.__cantdptos = StringVar()
        self.__temperatura = StringVar()
        self.__senstermica = StringVar()
        self.__humedad = StringVar()

        self.nombreentry = tk.Entry(frame4, textvariable=self.__nombre)
        self.nombreentry.pack(side=TOP, **opts)
        self.capitalentry = tk.Entry(frame4, textvariable=self.__capital)
        self.capitalentry.pack(side=TOP, **opts)
        self.canthabentry = tk.Entry(frame4, textvariable=self.__canthab)
        self.canthabentry.pack(side=TOP, **opts)
        self.cantdptosentry = tk.Entry(frame4, textvariable=self.__cantdptos)
        self.cantdptosentry.pack(side=TOP, **opts)
        self.temperaturaentry = tk.Entry(frame4, textvariable=self.__temperatura)
        self.temperaturaentry.pack(side=TOP, **opts)
        self.senstermicaentry = tk.Entry(frame4, textvariable=self.__senstermica)
        self.senstermicaentry.pack(side=TOP, **opts)
        self.humedadentry = tk.Entry(frame4, textvariable=self.__humedad)
        self.humedadentry.pack(side=TOP, **opts)

        self.nombreentry.focus()
        self.__ventana.mainloop()

    def agregarprovvista(self): #Nueva ventana que permite la creacion de una nueva provincia
        self.__nuevaprovincia = Toplevel()
        self.__nuevaprovincia.title('Nueva Provincia')
        self.__nuevaprovincia.geometry('400x250')
        self.__nuevaprovincia.resizable(0, 0)
        opts = {'padx': '5', 'pady': '5'}
        lframe = tk.LabelFrame(self.__nuevaprovincia, text='Provincia')
        lframe.pack(padx=10, pady=10)
        frame1 = tk.Frame(lframe)
        frame1.pack(side=LEFT, **opts)
        tk.Label(frame1, text='Nombre').pack(side=TOP, **opts)
        tk.Label(frame1, text='Capital').pack(side=TOP, **opts)
        tk.Label(frame1, text='Cantidad de habitantes').pack(side=TOP, **opts)
        tk.Label(frame1, text='Cantidad de departamentos/partidos').pack(side=TOP, **opts)

        frame2 = tk.Frame(lframe)
        frame2.pack(side=RIGHT, **opts)

        self.__nombre1 = StringVar()
        self.__capital1 = StringVar()
        self.__canthab1 = StringVar()
        self.__cantdptos1 = StringVar()

        nombreentry = tk.Entry(frame2, textvariable=self.__nombre1)
        nombreentry.pack(side=TOP, **opts)
        capitalentry = tk.Entry(frame2, textvariable=self.__capital1)
        capitalentry.pack(side=TOP, **opts)
        canthabentry = tk.Entry(frame2, textvariable=self.__canthab1)
        canthabentry.pack(side=TOP, **opts)
        cantdptosentry = tk.Entry(frame2, textvariable=self.__cantdptos1)
        cantdptosentry.pack(side=TOP, **opts)
        tk.Button(self.__nuevaprovincia, text='Confirmar', command=self.agregarprovincia).pack(side=TOP, pady=20)

    # Agrega provincia a json
    def agregarprovincia(self):
        obj = Objectencoder()
        if self.__nombre1.get() == '' or self.__capital1.get() == '' or self.__canthab1.get() == '' or self.__cantdptos1.get() == '':
            messagebox.showerror('Error', 'Debe ingresar todos los datos de la provincia')
        else:
            dic = {'Provincia': {'Nombre': self.__nombre1.get(), 'Capital': self.__capital1.get(),
                                 'Canthab': self.__canthab1.get(), 'Cantdptos': self.__cantdptos1.get()}}
            dic1 = obj.lectura('datos.json')
            if dic1 is None:
                dic1 = [dic]
            else:
                dic1.append(dic)
            obj.guardado(dic1, 'datos.json')
            self.__listbox.delete(0, len(self.__datos))
            self.cargarprovincias()
            self.__nuevaprovincia.destroy()

    # Carga en memoria temporal las provincia del archivo json
    def cargarprovincias(self):
        obj = Objectencoder()
        self.__datos = obj.lectura('datos.json')
        self.__datos = sorted(self.__datos, key=lambda p: p['Provincia']['Nombre'])
        for i in range(len(self.__datos)):
            provincia = str(self.__datos[i]['Provincia']['Nombre'])
            self.__listbox.insert(i, provincia)

    # Vincula el doble click
    def dobleclick(self, callback):
        handler = lambda _: callback(self.__listbox.curselection()[0])
        self.__listbox.bind('<Double-Button-1>', handler)

    # Carga los datos de una provincia en el formulario
    def ponerprovincia(self, i):
        self.__indice.set(i)
        self.__nombre.set(self.__datos[i]['Provincia']['Nombre'])
        self.__capital.set(self.__datos[i]['Provincia']['Capital'])
        self.__canthab.set(self.__datos[i]['Provincia']['Canthab'])
        self.__cantdptos.set(self.__datos[i]['Provincia']['Cantdptos'])
        r = requests.get( #Trae los datos de la api buscasndo a la provincia por el nombre que se envia como paramentro en el link
            'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=3679ee8c1733ba53da9da5954bfd6511'.format(
                self.__nombre.get()))
        datos = r.json()
        tem = datos['main']['temp'] #Busca por las claves cada uno de los valores que se quieren mostrar en la pantalla
        sen = datos['main']['feels_like']
        hum = datos['main']['humidity']
        self.__temperatura.set(tem) #Se setean los valores obtenidos para mostrarlos
        self.__senstermica.set(sen)
        self.__humedad.set(hum)