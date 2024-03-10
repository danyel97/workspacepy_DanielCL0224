def call_inputs():
    base=int(input("ingrese la base: "))
    altura=int(input("ingrese la altura: "))
    return (base,altura)

def area_triangulo():
    (base,altura)=call_inputs()
    return base*altura/2

def area_rectangulo():
    (base,altura)=call_inputs()
    return base*altura/2

def calcular_poligono(poligono:str):
    poligono=poligono.upper()
    match poligono:
        case 'TRIANGULO':
            return area_triangulo()
        case 'RECTANGULO':
            return area_rectangulo()
        case _:
            return 'error'


print(calcular_poligono('TRIANGULO'))



