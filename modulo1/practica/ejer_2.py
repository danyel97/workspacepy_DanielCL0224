print("****Calculadora de Areas****")
fig = input("Ingrese la figura deseada: ")

if fig == "circulo" or "cuadrado" or "triangulo":
    import math
    if fig == "cuadrado":
        lado = float(input("Ingrese el lado del cuadrado: "))
        area2 = math.pow(lado,2)
        print(area2)
    elif fig == "triangulo":
        base = float(input("Ingrese la base del triangulo: "))
        alt = float(input("Ingrese la altura del triangulo: "))
        area3 = (base*alt)/2
        print(area3)
    elif fig == "circulo":
         PI = math.pi # float
         rad = float(input("Ingrese el radio del circulo: "))
         area=PI*math.pow(rad,2)
         print(area)
else:
    msg = "no es la figura"
    print(msg)
