print("****Calculadora financiera****")
ingr = float(input("Digite el monto de su ingreso mensual: "))
gastos = int(input("Digite la cantidad de gastos a realizar: "))

if gastos <=5:
    print("Indique los gastos a realizar: ")
    
    pag1 = float(input(""))
    pag2 = float(input(""))
    gast = pag1+pag2
    pag3 = float(input(""))
    gast = pag1+pag2+pag3
    pag4 = float(input(""))
    gast = pag1+pag2+pag3+pag4
    pag5 = float(input(""))
    gast = pag1+pag2+pag3+pag4+pag5
    print("Su egreso es de: ",gast)
    rest = ingr-gast
    if gast >ingr:
        print("Su ahorro es de: ",rest)
    else:
        negrest = -rest
        print("Sus gastos excede en: ",negrest)
else:
    print("Supera los gastos basicos de su hogar")
