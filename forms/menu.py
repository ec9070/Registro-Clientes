from customtkinter import *
import util.globals as globals
from controllers.client import Client
from CTkMessagebox import CTkMessagebox as Message

class Menu():
    def __init__(self):
        # Size
        self.window = CTk(fg_color="#b7e9ed")
        width = (int(self.window.winfo_screenwidth()))
        height = (int(self.window.winfo_screenheight()))
        w = int(width*0.5)
        h = int(height*0.5)
        globals.setSize(width, height)
        # Position
        self.window.title('Menu Principal')
        globals.c_window(self.window, w, h)
        self.window.resizable(0,0) 
        # Fonts
        titulos = CTkFont(family="Inter", size=18, weight="bold")
        # Buttons
        add = CTkButton(self.window, width=w*0.23, height=h*0.077, fg_color="#4763d6", text_color="white", text="Agregar Cliente", font=titulos, command=self.Agregar)
        add.pack(side=TOP, pady=(75,35))
        search = CTkButton(self.window, width=w*0.23, height=h*0.077, fg_color="#4763d6", text_color="white", text="Buscar por Cedula", font=titulos, command=self.Search)
        search.pack(side=TOP, pady=(0, 35))
        list = CTkButton(self.window, width=w*0.23, height=h*0.077, fg_color="#4763d6", text_color="white", text="Lista de Clientes", font=titulos, command=self.List)
        list.pack(side=TOP, pady=(0, 0))
        self.window.mainloop()

    def Agregar(self):
        self.window.withdraw()
        AddClient(self.window, None)

    def Search(self):
        search_entry = CTkInputDialog(text="Ingrese la cedula:", title="Busqueda")
        globals.c_window(search_entry, 300, 200)
        cedula = search_entry.get_input()
        if cedula:
            client = Client.clientExist(cedula)
            if (client):
                self.window.withdraw()
                AddClient(self.window, client)
            else:
                Message(title="Error", message=f"No se encontró el usuario con la cedula: {cedula}", icon="cancel")
                
    def List(self):
        self.window.withdraw()
        ClientList(self.window)

from forms.addClient import AddClient
from forms.clientList import ClientList      

