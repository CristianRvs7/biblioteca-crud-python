import psycopg
from database.config import DB_CONFIG

def obtener_conexion():
    return psycopg.connect(**DB_CONFIG)
    