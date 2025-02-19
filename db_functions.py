import sqlite3
import pyrebase
import os
from dotenv import load_dotenv

load_dotenv()

firebase_config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID")
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()


FIREBASE_ERRORS = {
    "EMAIL_NOT_FOUND": "Este correo no está registrado.",
    "INVALID_PASSWORD": "La contraseña ingresada es incorrecta.",
    "MISSING_PASSWORD": "Contraseña requerida.",
    "USER_DISABLED": "Esta cuenta ha sido deshabilitada.",
    "INVALID_EMAIL": "El correo ingresado no es válido.",
    "INVALID_LOGIN_CREDENTIALS": "Credenciales incorrectas.",
    "TOO_MANY_ATTEMPTS_TRY_LATER": "Has intentado demasiadas veces. Intenta más tarde.",
    "WEAK_PASSWORD": "Contraseña demasiado débil.",
    "EMAIL_EXISTS": "El correo ingresado ya está registrado.",
}



def get_db_connection():
    try:
        conn = sqlite3.connect("database.db")  
        cursor = conn.cursor() 
        return conn, cursor 
    except sqlite3.Error as e:
        print(f"Error de conexión con la base de datos: {e}")
        return None, None


def close_db_connection(conn):
    try:
        if conn:
            conn.close() 
    except sqlite3.Error as e:
        print(f"Error al cerrar la conexión: {e}")

