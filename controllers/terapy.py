import sqlite3
import util.connection as cnx
from CTkMessagebox import CTkMessagebox as Message
from datetime import datetime

class Terapy():
    def addTerapy(terapy):
        conn = cnx.connect()
        entry = "INSERT INTO terapias (cliente, terapia, monto, metodo, fecha) VALUES(?,?,?,?,?)"
        data = (terapy[4],terapy[0],terapy[1],terapy[2],terapy[3])
        try:
            cursor = conn.cursor()
            cursor.execute(entry,data)
            conn.commit()
        except sqlite3.Error as err:
            Message(title="Error de base de datos", message=err, icon="cancel")
        conn.close()

    def getAll():
        list = []
        conn = cnx.connect()
        entry = "SELECT * FROM terapias"
        try:
            cursor = conn.cursor()
            cursor.execute(entry)
            list = cursor.fetchall()
        except sqlite3.Error as err:
            Message(title="Error de base de datos", message=err, icon="cancel")
        conn.close()
        if len(list)>0:
            list.sort(
                key=lambda terapia: datetime.strptime(
                    terapia[5],
                    "%d/%m/%Y %I:%M %p"
                ),
                reverse=True
            )
        return list
    
    def updateTerapy(terapy):
        conn = cnx.connect()
        entry = "UPDATE terapias set terapia=?, monto=?, metodo=?, fecha=? WHERE id=?"
        data = (terapy[2], terapy[3], terapy[4], terapy[5], terapy[0])
        try:
            cursor = conn.cursor()
            cursor.execute(entry,data)
            conn.commit()
        except sqlite3.Error as err:
            Message(title="Error de base de datos", message=err, icon="cancel")
        conn.close()

    def deleteTerapy(id):
        conn = cnx.connect()
        entry = "DELETE FROM terapias where id=?"
        try:
            cursor = conn.cursor()
            cursor.execute(entry,(id,))
            conn.commit()
        except sqlite3.Error as err:
            Message(title="Error de base de datos", message=err, icon="cancel")
        conn.close()
