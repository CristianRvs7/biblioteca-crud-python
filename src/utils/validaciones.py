from datetime import datetime

## ================================================================================ ##
##                                 LECTURA DE DATOS                                 ##
## ================================================================================ ##
def leer_isbn(mensaje):
    while True:
        isbn = input(mensaje)

        if len(isbn) == 13 and isbn.isdigit():
            return isbn

        print("El ISBN debe tener 13 dígitos y contener solo números.")

## ================================================================================ ##

def leer_int(mensaje):
    while True:
        try:
            valor = int(input(mensaje))

            if valor <= 0:
                raise ValueError

            return valor

        except ValueError:
            print("Debe ingresar un número entero positivo.")
    
## ================================================================================ ##

def leer_anio(mensaje):
    while True:
        try:
            anio = int(input(mensaje))

            if anio < 1450 or anio > datetime.now().year:
                raise ValueError

            return anio

        except ValueError:
            print(f"El año debe estar entre 1450 y {datetime.now().year}.")

## ================================================================================ ##

def leer_correo(mensaje):
    while True:
        correo = input(mensaje)

        if "@" in correo and "." in correo:
            return correo

        print("Ingrese un correo válido.")

## ================================================================================ ##

def confirmar_accion(mensaje):
    while True:
        respuesta = input(f"{mensaje} (S/N): ").strip().upper()

        if respuesta in ("S", "N"):
            return respuesta == "S"

        print("Ingrese S o N.")

## ================================================================================ ##

def leer_int_no_negativo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))

            if valor < 0:
                raise ValueError

            return valor

        except ValueError:
            print("Debe ingresar un número entero mayor o igual a cero.")

### ================================================================================ ##

def leer_texto(mensaje, longitud_maxima=None):
    while True:
        texto = input(mensaje).strip()

        if not texto:
            print("Este campo no puede estar vacío.")
            continue

        if longitud_maxima and len(texto) > longitud_maxima:
            print(f"El texto no puede superar los {longitud_maxima} caracteres.")
            continue

        return texto
## ================================================================================ ##
def leer_fecha(mensaje, allow_empty=False):
    while True:
        fecha = input(mensaje).strip()

        if allow_empty and fecha == "":
            return None

        try:
            return datetime.strptime(fecha, "%Y-%m-%d").date()
        except ValueError:
            print("Fecha inválida. Use el formato YYYY-MM-DD.")