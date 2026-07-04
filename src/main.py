from database.config import DB_CONFIG
from database.connection import obtener_conexion
from repositories.libro_repository import *
from repositories.autor_repository import *
from models.libro import Libro
from models.autor import Autor
from models.prestamo import Prestamo
from repositories.prestamo_repository import *
from datetime import datetime, date
from models.usuario import Usuario
from repositories.usuario_repository import *
from repositories.libro_repository import *
from menus.menu_principal import *
##autor = obtener_libros()

##for autor in autor:
    ##print(autor)
    

#libros = obtener_libros_detallados()

#for libro in libros:
 #   print(f"""
#ID: {libro[0]}
#ISBN: {libro[1]}
#Título: {libro[2]}
#Autor: {libro[3]} {libro[4]}
#Categoría: {libro[5]}
#Editorial: {libro[6]}
#Año: {libro[7]}
#Existencias: {libro[8]}
#""")

iniciar_menu()