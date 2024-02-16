while True:
    print("Ingrese una opcion")
    opciones="""
        1. Ingrese sus datos personales
        2. Calculadora basica
        3. Lista de estudiantes
        4. Promedio de notas
        5. Lista de almunos aprobados
        6. Lista de alumnos desaprobados
        7. Numeros multiplo de 2 ,  5 y de 7
        8. ¿que numero es mayor?
        9. salir
    """
    print(opciones)
    opc=int(input("Ingrese su opción: "))
    if opc==1:
        print("Bienvenido!!!")
        nomb=input("Nombre(s)")
        apell=input("Apellidos")
        edad=int(input("Edad"))
        DNI=input("DNI")
    elif opc==2:
        while True:
            print("Ingrese la operacion a realizar")
            opciones="""
                1. Suma
                2. Resta
                3. Multiplicacion
                4. Division
            """
            print(opciones)
            opc=int(input("Ingrese su opción: "))
            numa=int(input("Ingrese el primer numero: "))
            numb=int(input("Ingrese el segundo numero: "))
            if opc==1:
               reslt1=numa+numb
               print(reslt1)
            elif opc==2:
                reslt2=numa-numb
                print(reslt2)
            elif opc==3:
                reslt3=numa*numb
                print(reslt3)
            elif opc==4:
                reslt4=numa/numb
                print(reslt4)
            else:
                print("ingrese un valor correcto")
    elif opc==3:
        personas = []
        persona1 = {
            "nombre": "Juan",
            "edad": 25,
            "correo": "juan@example.com",
            "cursos": [
                {"curso": "Excel basico", "notas": [14,17,16]}
            ]
        }

        persona2 = {
            "nombre": "María",
            "edad": 30,
            "correo": "maria@example.com",
            "cursos": [
                {"curso": "Pyhton basico", "notas": [15,15,17]},
            ]
        }

        personas.append(persona1)
        personas.append(persona2)
        print(personas)
    elif opc==4:
        print("q")
    elif opc==5:
        print("x")
    elif opc==6:
        print("y")
    elif opc==7:
        print("e")
    elif opc==8:
        num_1=int(input("Ingrese un numero: "))
        num_2=int(input("Ingrese un numero: "))
        x = max(num_1,num_2)
        print("el numero mayor es: ", x)
    else:
        print("ingrese un valor correcto")