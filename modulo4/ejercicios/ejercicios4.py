import re

def validarCorreo(email):
    
    patron="^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$"
    resultado=re.match(patron,email.lower())

    if resultado:
        print("Es un correo")
    else :
        print("No es un correo")


correo="gmggmail.com"
validarCorreo(correo)

def validarTelefono(telefono):
    patron="^[789]\d{9}"
    resultado=re.match(patron,telefono)
    if resultado:
        print("Es un telefono valido")
    else:
        print("No es un telefono")

telefono="6587454281"
validarTelefono(telefono)