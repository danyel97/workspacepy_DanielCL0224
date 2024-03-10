# 1.
print("Por favor, ingrese sus datos personales:")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
direccion = input("Dirección: ")

print("\nDatos Personales:")
print("Nombre:", nombre)
print("Apellido:", apellido)
print("Edad:", edad)
print("Dirección:", direccion)

#2.
pi=3.14
radio = float(input("Ingrese el radio del círculo: "))
area = pi* radio**2
perimetro = 2*pi *radio
#3.
ingreso_total = float(input("Ingrese el ingreso total del hogar: "))
egresos = 0
Luz=float(input("Ingresa el gasto de luz:"))
Agua=float(input("Ingresa el gasto de Agua:"))
Comida=float(input("Ingresa el gasto de Comida:"))
egresos=Luz+Agua+Comida
ahorro = ingreso_total - egresos    
print("\nResumen de Gastos:")
print("Egresos totales:", egresos)
print("Ahorro:", ahorro)
#4.
mayor_edad = input("¿Eres mayor de edad? (si/no): ").lower()
isMayorEdad=(mayor_edad== "si")
tiene_ruc = input("¿Tienes RUC? (si/no): ").lower() == "si"
nombre_comercial = input("¿Tienes un nombre comercial? (si/no): ").lower() == "si"

if isMayorEdad and tiene_ruc and nombre_comercial:
    print("Estás apto para abrir un negocio.")
else:
    print("No cumples con todas las condiciones para abrir un negocio.")