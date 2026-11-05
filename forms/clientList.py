import util.globals as globals
from customtkinter import *
from CTkTable import *
from controllers.client import Client
from controllers.terapy import Terapy
from CTkMessagebox import CTkMessagebox as Message
import re

class ClientList():
    def __init__(self, main, filtered = False, client = None):
        # Size
        self.main = main
        self.f_tabla = None
        self.filtered = filtered
        self.clients = Client.getClients()
        if client:
            self.cedula = client[1]
        self.terapies = Terapy.getAll()
        size = globals.getSize()
        self.w = int(size[0]*0.8)
        self.h = int(size[1]*0.8)
        self.window = CTkToplevel(fg_color="white")
        self.window.title("Lista de Clientes")
        globals.c_window(self.window,self.w,self.h)
        self.window.protocol("WM_DELETE_WINDOW", self.close)
        # Fonts
        # self.TituloSuperior = CTkFont(family="Inter", size=25, weight="bold")
        self.encabezados = CTkFont(family="Inter", size=18, weight="bold")
        self.texto = CTkFont(family="Intern", size=16, weight="normal")
        self.f_btn = CTkFont(family="Intern", size=16, weight="bold")
        # Busqueda
        busqueda = CTkFrame(self.window, fg_color="white")
        busqueda.pack(side=TOP, fill="x", padx=(30,0), pady=(25,0))
        busquedaLabel = CTkLabel(busqueda, text="Ingrese Cedula:", fg_color="white", bg_color="white", font=self.encabezados, text_color="black")
        busquedaLabel.grid(row=0, column=0, sticky="w")
        self.busqueda_entry = CTkEntry(busqueda, width=238, text_color="black", fg_color="white", font=self.texto, border_width=3, border_color="#BDBDE1")
        self.busqueda_entry.grid(row=0, column=1, padx=(15,0))
        btn_bucar = CTkButton(busqueda, text="Buscar", text_color="white", font=self.f_btn, fg_color="#4763d6", corner_radius=0, command=self.filter)
        btn_bucar.grid(row=0,column=5,sticky="w",padx=(20,0))
        if (self.filtered):
            self.busqueda_entry.insert(0,self.cedula)
            self.filter()
        else:
            self.Table(self.terapies)  

    def close(self):
        self.main.deiconify()
        self.window.destroy()

    def filter(self):
        list = []
        client = None
        cedula = self.busqueda_entry.get()
        if (cedula):
            client = self.getClientCedula(cedula)
            if (client):
                self.filtered = True
                for x in self.terapies:
                    if (x[1] == client[0]):
                        list.append(x)
                self.Table(list)
            else:
                Message(title="Error", message="No se econtraron clientes con esa cedula", icon="cancel")
        else:
            self.filtered = False
            self.Table(self.terapies)

    def Table(self, list):
        if self.f_tabla:
            self.f_tabla.destroy()
        self.f_tabla = CTkScrollableFrame(self.window, fg_color="white", bg_color="white", corner_radius=0)
        self.f_tabla.pack(side=TOP, fill="both", expand=True, pady=(20,0))
        if len(list)>0:
            rows = (len(list)+1)
            self.tabla = CTkTable(self.f_tabla, row=rows, column=6, font=self.texto, colors=["white","#ECE9E9"], text_color="black", justify="center", command = self.Actions)
            self.tabla.pack(expand=True, fill="both", pady=(5,0), padx=(0,10))
            self.tabla.insert(0,0,value="Fecha")
            self.tabla.insert(0,1,value="Cedula")
            self.tabla.insert(0,2,value="Nombre")
            self.tabla.insert(0,3,value="Monto")
            self.tabla.insert(0,4,value="", state="disabled")
            self.tabla.insert(0,5,value="", state="disabled")
            i = 1
            for item in list:
                terapy = item
                client = self.getClient(terapy[1])
                self.tabla.insert(i,0,value=terapy[5])
                self.tabla.insert(i,1,value=client[1])
                self.tabla.insert(i,2,value=client[2])
                self.tabla.insert(i,3,value=terapy[3])
                self.tabla.insert(i,4,value="Ver detalles",hover=True,hover_color="#64A1DA",corner_radius=0, textvariable=terapy[0])
                self.tabla.insert(i,5,value="Ver info cliente",hover=True,hover_color="#64A1DA",corner_radius=0)
                i = i+1

    def Actions(self, arg):
        cedula = self.tabla.get(arg["row"],1)
        client = self.getClientCedula(cedula)
        if (re.search("Ver detalles", arg["value"])):
            id = arg["args"]["textvariable"]
            self.window.destroy()
            terapy = self.getTerapy(id)
            Details(self.main, client, self.filtered, terapy)
        if (re.search("Ver info cliente", arg["value"])):
            self.window.destroy()
            Details(self.main, client, self.filtered)
        
    def getClient(self, id):
        for item in self.clients:
            client = item
            if (client[0] == id):
                return client
        return None

    def getClientCedula(self, cedula):
        for item in self.clients:
            if (item[1] == cedula):
                return item
        return None

    def getTerapy(self, id):
        for item in self.terapies:
            if (item[0] == id):
                return item
        return None
                
from forms.details import Details