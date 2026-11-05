import sqlite3

def initialize():
    conn = sqlite3.connect("Clientes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cedula TEXT NOT NULL,
            nombre TEXT NOT NULL,
            correo TEX NULL,
            telefono TEXT NULL,
            enfermedades TEXT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS terapias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente INTEGER NOT NULL,
            terapia TEXT NOT NULL,
            monto TEXT NOT NULL,
            metodo TEXT NOT NULL,
            fecha TEXT NOT NULL,
            FOREIGN KEY (cliente) REFERENCES clientes(id)
        )
    """)
    conn.commit()
    conn.close()

def connect():
 conn = sqlite3.connect("Clientes.db")
 return conn