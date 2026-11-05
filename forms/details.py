import util.globals as globals
from customtkinter import *
from CTkMessagebox import CTkMessagebox as Message
from datetime import datetime
from controllers.terapy import Terapy
from controllers.client import Client

class Details():
    def __init__(self, main, client, filtered, terapy=None):
        # Size
        self.main = main
        self.client = client
        if (terapy):
            self.terapy = terapy
        self.filtered = filtered
        size = globals.getSize()
        self.w = int(size[0]*0.8)
        self.h = int(size[1]*0.8)
        self.window = CTkToplevel(fg_color="#b7e9ed")
        self.window.title("Detalles")
        if terapy:
            self.window.state('zoomed') 
        globals.c_window(self.window, self.w, self.h)
        self.window.protocol("WM_DELETE_WINDOW", self.close)
        #Fuentes
        self.titulo = CTkFont(family="Inter", size=28, weight="normal")
        self.encabezados = CTkFont(family="Inter", size=16, weight="bold")
        self.texto = CTkFont(family="Inter", size=16, weight="normal")
        # Info
        if (terapy):
            self.info('terapia')
        else:
            self.info('cliente')

    def close(self):
        self.window.destroy()
        ClientList(self.main, self.filtered, self.client)

    def info(self, type):
        # Titulo
        if type == 'terapia':
            titulo_ventana = CTkLabel(self.window, text="Detalles de la terapia", text_color="black", font=self.titulo, fg_color="#b7e9ed")
        else:
            titulo_ventana = CTkLabel(self.window, text="Detalles del cliente", text_color="black", font=self.titulo, fg_color="#b7e9ed")
        titulo_ventana.pack(side=TOP, pady=(20,15))
        # Datos Cliente
        frame = CTkFrame(self.window, fg_color="#b7e9ed")
        frame.pack(side=TOP, fill='y')
        # Cedula
        label_cedula = CTkLabel(frame, text="Cedula", text_color="black", font=self.encabezados, fg_color="#b7e9ed")
        label_cedula.grid(row=0, column=0)
        self.cedula = CTkEntry(frame, width=275, height=28, text_color="black", font=self.texto, fg_color="white", border_width=3, border_color="#BDBDE1", justify='center')
        self.cedula.grid(row=1, column=0, pady=(6,10))
        self.cedula.insert(0,self.client[1])
        # Nombre
        label_nombre = CTkLabel(frame, text="Nombre", text_color="black", font=self.encabezados, fg_color="#b7e9ed")
        label_nombre.grid(row=0, column=1, padx=(125,0))
        self.nombre = CTkEntry(frame, width=275, height=28, text_color="black", font=self.texto, fg_color="white", border_width=3, border_color="#BDBDE1", justify='center')
        self.nombre.grid(row=1, column=1, pady=(6,10), padx=(125,0))
        self.nombre.insert(0,self.client[2])
        # Correo
        frame_1 = CTkFrame(self.window, fg_color="#b7e9ed")
        frame_1.pack(side=TOP, fill="y", pady=(10,0))
        label_correo = CTkLabel(frame_1, text="Correo", text_color="black", font=self.encabezados, fg_color="#b7e9ed")
        label_correo.grid(row=0, column=0)
        self.correo = CTkEntry(frame_1, width=275, height=28, text_color="black", font=self.texto, fg_color="white", border_width=3, border_color="#BDBDE1", justify='center')
        self.correo.grid(row=1, column=0, pady=(6,10))
        self.correo.insert(0,self.client[3])
        # Telefono
        label_tel = CTkLabel(frame_1, text="Telefono", text_color="black", font=self.encabezados, fg_color="#b7e9ed")
        label_tel.grid(row=0, column=1, padx=(125,0))
        self.tel = CTkEntry(frame_1, width=275, height=28, text_color="black", font=self.texto, fg_color="white", border_width=3, border_color="#BDBDE1", justify='center')
        self.tel.grid(row=1, column=1, pady=(6,10), padx=(125,0))
        self.tel.insert(0,self.client[4])
        # Enfermedades
        label_enfermedades = CTkLabel(self.window, text="Enfermedades", text_color="black", font=self.encabezados, fg_color="#b7e9ed")
        label_enfermedades.pack(side=TOP, pady=(10,10))
        frame_2 = CTkFrame(self.window, fg_color="#b7e9ed")
        frame_2.pack(side=TOP, fill='y')
        self.enfermedades = CTkTextbox(frame_2, width=(self.w*0.27), height=85, border_width=3, border_color="#BDBDE1", fg_color="white", font=self.texto, corner_radius=0, text_color="black")
        self.enfermedades.pack(side=TOP)
        self.enfermedades.insert('0.0',self.client[5])
        if (type == 'terapia'):
        # Monto
            frame_3 = CTkFrame(self.window, fg_color="#b7e9ed")
            frame_3.pack(side=TOP, fill="y", pady=(15,0))
            label_monto = CTkLabel(frame_3, text="Monto", text_color="black", font=self.encabezados, fg_color="#b7e9ed")
            label_monto.grid(row=0, column=0)
            self.monto = CTkEntry(frame_3, width=200, height=28, text_color="black", font=self.texto, fg_color="white", border_width=3, border_color="#BDBDE1", justify='center')
            self.monto.grid(row=1, column=0, pady=(6,10))
            self.monto.insert(0,self.terapy[3])
            # Metodo
            label_metodo = CTkLabel(frame_3, text="Metodo de pago", text_color="black", font=self.encabezados, fg_color="#b7e9ed")
            label_metodo.grid(row=0, column=1, padx=(50,0))
            self.metodo = CTkEntry(frame_3, width=200, height=28, text_color="black", font=self.texto, fg_color="white", border_width=3, border_color="#BDBDE1", justify='center')
            self.metodo.grid(row=1, column=1, pady=(6,10), padx=(50,0))
            self.metodo.insert(0,self.terapy[4])
            # Fecha
            label_fecha = CTkLabel(frame_3, text="Fecha", text_color="black", font=self.encabezados, fg_color="#b7e9ed")
            label_fecha.grid(row=0, column=2, padx=(50,0))
            self.fecha = CTkEntry(frame_3, width=200, height=28, text_color="black", font=self.texto, fg_color="white", border_width=3, border_color="#BDBDE1", justify='center')
            self.fecha.grid(row=1, column=2, pady=(6,10), padx=(50,0))
            self.fecha.insert(0,self.terapy[5])
            # Terapia
            label_terapia = CTkLabel(self.window, text="Terapia", text_color="black", font=self.encabezados, fg_color="#b7e9ed")
            label_terapia.pack(side=TOP, pady=(10,10))
            frame_4 = CTkFrame(self.window, fg_color="green")
            frame_4.pack(side=TOP, fill="y")
            self.terapia = CTkTextbox(frame_4, width=(self.w*0.27), height=85, border_width=3, border_color="#BDBDE1", fg_color="white", font=self.texto, corner_radius=0, text_color="black")
            self.terapia.pack(side=TOP)
            self.terapia.insert('insert',self.terapy[2])
            self.cedula.configure(state="readonly")
            self.nombre.configure(state="readonly")
            self.correo.configure(state="readonly")
            self.tel.configure(state="readonly")
            self.enfermedades.configure(state="disabled")
        # Buttons
        f_btns = CTkFrame(self.window, fg_color="#b7e9ed")
        f_btns.pack(side=TOP, fill='y')
        if (type == 'terapia'):
            btn_edit = CTkButton(f_btns, width=140, height=34, text="Editar", text_color="white", font=self.encabezados, fg_color="#3fa144", corner_radius=0, command=self.Edit)
            btn_eliminar = CTkButton(f_btns, width=140, height=34, text="Eliminar", text_color="white", font=self.encabezados, fg_color="#c24848", corner_radius=0, command=self.Eliminar)
        else:
            btn_eliminar = CTkButton(f_btns, width=140, height=34, text="Eliminar", text_color="white", font=self.encabezados, fg_color="#c24848", corner_radius=0, command=self.Eliminar_c)
            btn_edit = CTkButton(f_btns, width=140, height=34, text="Editar", text_color="white", font=self.encabezados, fg_color="#3fa144", corner_radius=0, command=self.Edit_C)
        btn_edit.pack(side=LEFT, pady=(15,0), padx=5)
        btn_eliminar.pack(side=LEFT, pady=(15,0), padx=5)
        btn_back = CTkButton(f_btns, width=140, height=34, text="Volver", text_color="white", font=self.encabezados, fg_color="#4763d6", corner_radius=0, command=self.close)
        btn_back.pack(side=LEFT, pady=(15,0), padx=5)


    def Edit(self):
        terapy = []
        terapy.append(self.terapy[0])
        terapy.append(self.terapy[1])
        terapy.append(self.terapia.get("0.0", 'end'))
        terapy.append(self.monto.get())
        terapy.append(self.metodo.get())
        terapy.append(self.fecha.get())
        if (self.verify(terapy[3], terapy[4], terapy[5], terapy[2])):
            msg = Message(title=("Editar"), message=("¿Seguro que quiere Editar la información"),icon="question",option_2="Si",option_1="No")
            res = msg.get()
            if res == 'Si':
                Terapy.updateTerapy(terapy)
                self.terapy = terapy
                self.monto.delete(0,'end')
                self.metodo.delete(0,'end')
                self.fecha.delete(0,'end')
                self.terapia.delete("0.0",'end')
                self.monto.insert(0,self.terapy[3])
                self.metodo.insert(0,self.terapy[4])
                self.fecha.insert(0,self.terapy[5])
                self.terapia.insert('insert',self.terapy[2])

    def verify(self, monto, metodo, fecha, terapia):
        aux = False
        if (not monto):
            Message(title="Error", message="El monto no puede estar vacio", icon="cancel")
        elif (not metodo):
            Message(title="Error", message="El metodo de pago no puede estar vacio", icon="cancel")
        elif (not fecha):
            Message(title="Error", message="La fecha no puede estar vacia", icon="cancel")
        elif (not terapia):
            Message(title="Error", message="La terapia no puede estar vacia", icon="cancel")
        else:
            date = self.validate(fecha)
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

    def Edit_C(self):
        client = []
        client.append(self.cedula.get())
        client.append(self.nombre.get())
        client.append(self.correo.get())
        client.append(self.tel.get())
        client.append(self.enfermedades.get("0.0", 'end'))
        if (self.verify_c(client)):
            msg = Message(title=("Editar"), message=("¿Seguro que quiere Editar la información"),icon="question",option_2="Si",option_1="No")
            res = msg.get()
            if res == 'Si':
                Client.updateCliente(client, self.client[0])
                self.cedula.delete(0,'end')
                self.nombre.delete(0,'end')
                self.correo.delete(0,'end')
                self.tel.delete(0,'end')
                self.enfermedades.delete("0.0",'end')
                self.cedula.insert(0,client[0])
                self.nombre.insert(0,client[1])
                self.correo.insert(0,client[2])
                self.tel.insert(0,client[3])
                self.enfermedades.insert('insert', client[4])

    def verify_c(self, client):
        aux = False
        if (not client[0]):
            Message(title="Error", message="La cedula no puede estar vacia", icon="cancel")
        elif (not client[1]):
            Message(title="Error", message="El nombre no puede estar vacio", icon="cancel")
        else:
            aux = True
        return aux

    def Eliminar(self):
        msg = Message(title=("Eliminar"), message=("¿Seguro que quiere Eliminar la terapia"),icon="question",option_2="Si",option_1="No")
        res = msg.get()
        if res == 'Si':
            Terapy.deleteTerapy(self.terapy[0])
            self.close()

    def Eliminar_c(self):
        msg = Message(title=("Eliminar"), message=("¿Seguro que quiere Eliminar al cliente"),icon="question",option_2="Si",option_1="No")
        res = msg.get()
        if res == 'Si':
            Client.deleteClient(self.client[0])
            self.filtered = False
            self.close()
    
from forms.clientList import ClientList
