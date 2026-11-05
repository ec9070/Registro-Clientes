import sqlite3
import util.connection as cnx
from CTkMessagebox import CTkMessagebox as Message

class Client():
    def clientExist(cedula):
        conn = cnx.connect()
        client = None
        entry = "SELECT * FROM clientes WHERE cedula = ?"
        try:
            cursor = conn.cursor()
            cursor.execute(entry,(cedula,))
            client = cursor.fetchone()
        except sqlite3.Error as err:
            Message(title="Error de base de datos", message=err, icon="cancel")
        conn.close()
        return client
    
    def addClient(client):
        conn = cnx.connect()
        entry = "INSERT INTO clientes (cedula, nombre, correo, telefono, enfermedades) VALUES(?,?,?,?,?)"
        data = (client[0],client[1],client[2],client[3],client[4])
        id_client = None
        try :
            cursor = conn.cursor()
            cursor.execute(entry,data)
            conn.commit()
            id_client = cursor.lastrowid
        except sqlite3.Error as err:
            Message(title="Error de base de datos", message=err, icon="cancel")
        conn.close()
        return id_client

    def updateCliente(client, id):
        conn = cnx.connect()
        entry = "UPDATE clientes SET cedula=?, nombre=?, correo=?, telefono=?, enfermedades=? WHERE id=?"
        data = (client[0],client[1],client[2],client[3],client[4],id) 
        try:
            cursor = conn.cursor()
            cursor.execute(entry,data)
            conn.commit()
        except sqlite3.Error as err:
            Message(title="Error de base de datos", message=err, icon="cancel")
        conn.close()

    def getClients():
        list = []
        conn = cnx.connect()
        entry = "SELECT * FROM clientes"
        try:
            cursor = conn.cursor()
            cursor.execute(entry)
            list = cursor.fetchall()
        except sqlite3.Error as err:
            Message(title="Error de base de datos", message=err, icon="cancel")
        conn.close()
        return list

    def deleteClient(id):
        conn = cnx.connect()
        entry = "DELETE FROM terapias where cliente=?"
        entry_2 = "DELETE FROM clientes where id=?"
        try:
            cursor = conn.cursor()
            cursor.execute(entry,(id,))
            cursor.execute(entry_2,(id,))
            conn.commit()
        except sqlite3.Error as err:
            Message(title="Error de base de datos", message=err, icon="cancel")
        conn.close()
            