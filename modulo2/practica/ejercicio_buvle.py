def agregar_alumno(lista_alumnos, nombre, edad, correo, cursos):
  alumno = {
    "nombre": nombre,
    "edad": edad,
    "correo": correo,
    "cursos": cursos
  }
  lista_alumnos.append(alumno)
lista_alumnos = []

agregar_alumno(lista_alumnos, "Juan Pérez", 20, "juan.perez@correo.com", [
  {
    "nombre_curso": "Python basico",
    "notas": [9, 10, 14]
  },
  {
    "nombre_curso": "Excel intermedio",
    "notas": [16, 12, 10]
  }
])

agregar_alumno(lista_alumnos, "Ana García", 21, "ana.garcia@correo.com", [
  {
    "nombre_curso": "Python bsaico",
    "notas": [18, 12, 14]
  },
  {
    "nombre_curso": "Excel intermedio",
    "notas": [17, 20, 10]
  }
])
def calcular_promedio(notas):
  suma_notas = sum(notas)
  promedio = suma_notas / len(notas)
  return promedio
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
        print(lista_alumnos)
    elif opc==4:
        def mostrar_alumnos_aprobados(lista_alumnos):
            print("Alumnos aprobados:")
            for alumno in lista_alumnos:
                promedio_total = 0
                numero_cursos = 0
                for curso in alumno["cursos"]:
                    promedio_curso = calcular_promedio(curso["notas"])
                    promedio_total += promedio_curso
                    numero_cursos += 1
                    promedio_final = promedio_total / numero_cursos
                if promedio_final >= 13:
                    print(f"- {alumno['nombre']}: {promedio_final:.2f}")

        mostrar_alumnos_aprobados(lista_alumnos)
    elif opc==5:
        def mostrar_alumnos_desaprobados(lista_alumnos):
            print("Alumnos desprobados:")
            for alumno in lista_alumnos:
                promedio_total = 0
                numero_cursos = 0
                for curso in alumno["cursos"]:
                    promedio_curso = calcular_promedio(curso["notas"])
                    promedio_total += promedio_curso
                    numero_cursos += 1
                    promedio_final = promedio_total / numero_cursos
                if promedio_final <= 13:
                    print(f"- {alumno['nombre']}: {promedio_final:.2f}")

        mostrar_alumnos_desaprobados(lista_alumnos)
    elif opc==6:
        print("y")
    elif opc==7:
        def generar_lista_multiplos():
            lista_multiplos = []
            for num in range(0, 10**10, 10000):#step=10000 para que se obtenga resultado de manera inmediata
                if num % 2 == 0 and num % 5 == 0 and num % 7 == 0:
                    lista_multiplos.append(num)
            return lista_multiplos
        lista_resultado = generar_lista_multiplos()
        print("Tamaño de la lista de múltiplos:", len(lista_resultado))
    elif opc==8:
        num_1=int(input("Ingrese un numero: "))
        num_2=int(input("Ingrese un numero: "))
        x = max(num_1,num_2)
        print("el numero mayor es: ", x)
    else:
        print("ingrese un valor correcto")
