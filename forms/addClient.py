import util.globals as globals
from customtkinter import *
from datetime import datetime
from CTkMessagebox import CTkMessagebox as Message
from controllers.client import Client
from controllers.terapy import Terapy

class AddClient():
    def __init__(self, main, client):
        # Size
        self.main = main
        self.client = client
        size = globals.getSize()
        self.w = int(size[0]*0.8)
        self.h = int(size[1]*0.8)
        self.window = CTkToplevel(fg_color="#b7e9ed")
        # self.window.minsize(self.w, self.h)
        # Position
        if client:
            self.window.title("Cliente")
        else:
            self.window.title("Agregar Cliente")
        globals.c_window(self.window, self.w, self.h)
        self.window.protocol("WM_DELETE_WINDOW", self.close)
        # Fonts
        self.bold = CTkFont(family="Intern", size=16, weight="bold")
        self.normal = CTkFont(family="Intern", size=16, weight="normal")
        # Form
        self.form()

    def close(self):
        self.main.deiconify()
        self.window.destroy()

    def form(self):
        form = CTkScrollableFrame(self.window, width=(self.w*0.5), height=(self.h*0.93)-48, fg_color="white", bg_color="white")
        form.pack(side=TOP,  fill='y', pady=(self.h*0.03, self.h*0.03), expand=True)
        # Cedula
        labelCedula = CTkLabel(form, text="Cedula: ", text_color="black", font=self.bold, fg_color="white")
        labelCedula.pack(pady=(self.h*0.03,0), padx=(self.w*0.077,0), anchor="w")
        self.cedula = CTkEntry(form, width=(self.w*0.333), height=45, border_width=3, border_color="#BDBDE1", fg_color="white", font=self.normal, corner_radius=0, text_color="black")
        self.cedula.pack(padx=(self.w*0.077,0), pady=(self.h*0.004,0), anchor="w")
        # Nombre
        labelNombre = CTkLabel(form, text="Nombre: ", text_color="black", font=self.bold, fg_color="white")
        labelNombre.pack(pady=(self.h*0.03,0), padx=(self.w*0.077,0), anchor="w")
        self.nombre = CTkEntry(form, width=(self.w*0.333), height=45, border_width=3, border_color="#BDBDE1", fg_color="white", font=self.normal, corner_radius=0, text_color="black")
        self.nombre.pack(padx=(self.w*0.077,0), pady=(self.h*0.004,0), anchor="w")
        # Correo
        labelCorreo = CTkLabel(form, text="Correo: ", text_color="black", font=self.bold, fg_color="white")
        labelCorreo.pack(pady=(self.h*0.03,0), padx=(self.w*0.077,0), anchor="w")
        self.correo = CTkEntry(form, width=(self.w*0.333), height=45, border_width=3, border_color="#BDBDE1", fg_color="white", font=self.normal, corner_radius=0, text_color="black")
        self.correo.pack(padx=(self.w*0.077,0), pady=(self.h*0.004,0), anchor="w")
        # Telefono
        labelTelefono = CTkLabel(form, text="Telefono: ", text_color="black", font=self.bold, fg_color="white")
        labelTelefono.pack(pady=(self.h*0.03,0), padx=(self.w*0.077,0), anchor="w")
        self.telefono = CTkEntry(form, width=(self.w*0.333), height=45, border_width=3, border_color="#BDBDE1", fg_color="white", font=self.normal, corner_radius=0, text_color="black")
        self.telefono.pack(padx=(self.w*0.077,0), pady=(self.h*0.004,0), anchor="w")
        # Terapia
        labelTerapia = CTkLabel(form, text="Terapia: ", text_color="black", font=self.bold, fg_color="white")
        labelTerapia.pack(pady=(self.h*0.03,0), padx=(self.w*0.077,0), anchor="w") 
        self.terapia = CTkTextbox(form, width=(self.w*0.333), height=86, border_width=3, border_color="#BDBDE1", fg_color="white", font=self.normal, corner_radius=0, text_color="black")
        self.terapia.pack(padx=(self.w*0.077,0), pady=(self.h*0.004,0), anchor="w")
         # Enfermedades
        labelEnfermedades = CTkLabel(form, text="Enfermedades: ", text_color="black", font=self.bold, fg_color="white")
        labelEnfermedades.pack(pady=(self.h*0.03,0), padx=(self.w*0.077,0), anchor="w") 
        self.enfermedades = CTkTextbox(form, width=(self.w*0.333), height=86, border_width=3, border_color="#BDBDE1", fg_color="white", font=self.normal, corner_radius=0, text_color="black")
        self.enfermedades.pack(padx=(self.w*0.077,0), pady=(self.h*0.004,0), anchor="w")
        # Monto
        labelMonto = CTkLabel(form, text="Monto: ", text_color="black", font=self.bold, fg_color="white")
        labelMonto.pack(pady=(self.h*0.03,0), padx=(self.w*0.077,0), anchor="w")
        self.monto = CTkEntry(form, width=(self.w*0.333), height=45, border_width=3, border_color="#BDBDE1", fg_color="white", font=self.normal, corner_radius=0, text_color="black")
        self.monto.pack(padx=(self.w*0.077,0), pady=(self.h*0.004,0), anchor="w")
        # Metodo
        labelMetodo = CTkLabel(form, text="Metodo de pago: ", text_color="black", font=self.bold, fg_color="white")
        labelMetodo.pack(pady=(self.h*0.03,0), padx=(self.w*0.077,0), anchor="w")
        self.metodo = CTkEntry(form, width=(self.w*0.333), height=45, border_width=3, border_color="#BDBDE1", fg_color="white", font=self.normal, corner_radius=0, text_color="black")
        self.metodo.pack(padx=(self.w*0.077,0), pady=(self.h*0.004,0), anchor="w")
        # Fecha
        labelFecha = CTkLabel(form, text="Fecha: ", text_color="black", font=self.bold, fg_color="white")
        labelFecha.pack(pady=(self.h*0.03,0), padx=(self.w*0.077,0), anchor="w")
        self.fecha = CTkEntry(form, width=(self.w*0.333), height=45, border_width=3, border_color="#BDBDE1", fg_color="white", font=self.normal, corner_radius=0, text_color="black")
        self.fecha.pack(padx=(self.w*0.077,0), pady=(self.h*0.004,0), anchor="w")
        date = datetime.now()
        format = date.strftime("%d/%m/%Y %I:%M %p")
        self.fecha.insert(0, format)
        # Boton
        self.btnCreate = CTkButton(form, width=(self.w*0.143), height=50, fg_color="#93A3DC", text_color="white", text="Registrar", font=self.bold, command=self.Add)
        self.btnCreate.pack(pady=(self.h*0.03, self.h*0.02))
        if (self.client):
            self.cedula.insert(0, self.client[1])
            self.nombre.insert(0, self.client[2])
            self.correo.insert(0, self.client[3])
            self.telefono.insert(0, self.client[4])
            self.enfermedades.insert('0.0', self.client[5])

    def Add(self):
        client = []
        terapy = []
        client.append(self.cedula.get())
        client.append(self.nombre.get())
        client.append(self.correo.get())
        client.append(self.telefono.get())
        client.append(self.enfermedades.get("0.0", 'end'))
        terapy.append(self.terapia.get("0.0", 'end'))
        terapy.append(self.monto.get())
        terapy.append(self.metodo.get())
        terapy.append(self.fecha.get())
        if (self.verify(client, terapy)):
            if self.client:
                client_e = self.client
            else:
                client_e = Client.clientExist(client[0])
            if (client_e):
                id_client = client_e[0]
                if (self.verify_edit(client, client_e)):
                    if (client[0] == client_e[1]):
                        Client.updateCliente(client, id_client)
                    else:
                        id_client = Client.addClient(client)
            else:
                id_client = Client.addClient(client)
            terapy.append(id_client)
            Terapy.addTerapy(terapy)
            Message(title="Cliente agregado", message="Cliente Agregado correctamente", icon="check", option_1="Aceptar")
            self.close()

    def verify(self, client, terapy):
        aux = False
        if (not client[0]):
            Message(title="Error", message="La cedula no puede estar vacia", icon="cancel")
        elif (not client[1]):
            Message(title="Error", message="El nombre no puede estar vacio", icon="cancel")
        elif (not terapy[0]):
            Message(title="Error", message="La terapia no puede estar vacia", icon="cancel")
        elif (not terapy[1]):
            Message(title="Error", message="El monto no puede estar vacio", icon="cancel")
        elif (not terapy[2]):
            Message(title="Error", message="El metodo de pago no puede estar vacio", icon="cancel")
        elif (not terapy[3]):
            Message(title="Error", message="La fecha no puede estar vacia", icon="cancel")
        else:
            date = self.validate(terapy[3])
            if (date):
                aux = True
            else :
                Message(title="Error", message="Formato de fecha no valido, debe tener el mismo formato de este ejemplo: 26/10/2026 12:30 PM", icon="cancel")
        return aux

    def validate(self, date):
        try :
            datetime.strptime(
                date,
                "%d/%m/%Y %I:%M %p"
            )
            return True
        except ValueError:
            return False

    def verify_edit(self, client, client_e):
        aux = False
        if ((client[0] != client_e[1]) or (client[1] != client_e[2]) or (client[2] != client_e[3]) or (client[3] != client_e[4]) or (client[4] != client_e[5])):
            aux = True
        return aux
        