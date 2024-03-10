
flagProgram=True

def saludar():
    name=input("Ingrese su nombre completo: ")
    correo=input("Ingrese su correo: ")
    msg=f'Hola ,{name} con usuario {correo}'
    return msg

def fxMath():
    numberOne=input('ingrese primer numero')
    numberTwo=input('ingrese segundo numero')
    

while flagProgram:

    opcionInput=input('Ingrese una opcion')
    opcion=int(opcionInput)

    if opcion==1:
        saludo=saludar()
        print(saludo)

    elif opcion == 2:
        pass