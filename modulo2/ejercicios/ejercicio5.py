
usuarios=[]

def saludar(name):
    return 'Bienvenido {}'.format(name)

def agregar_usuario():
        name=input("ingrese su nombre")
        #saludo=saludar(name)
        #print(saludo)
        print(saludar(name))
        dni=input("ingrese su dni")
        correo=input("ingrese su correo")
        datos={
            'name':name,
            'dni':dni,
            'correo':correo
        }
        usuarios.append(datos)


while True:

    print("Bienvenido a la tienda datux")
    print("Ingrese una opcion")
    opciones="""
        1. Agregar usuario
        2. Verificar lista
        3. salir
    """
    print(opciones)
    opc=int(input("ingrese sus opciones"))
    if opc==1:
        agregar_usuario()
    elif opc==2:
        for i,item in enumerate(usuarios):
            print(i,".",item)
           # for j in item.items():
           #     print(i,".",j)
    elif opc==3:
        print("Hasta luego")
        break
    else:
        print("ingrese un valor correcto")