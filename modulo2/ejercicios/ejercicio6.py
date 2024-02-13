
def sumar(n):
    if n!=1:
        return n+ sumar(n-1)
    else:
        return 1

##numero=int(input("ingrese un valor a sumar"))
##print(sumar(numero))
## n +n-1 + (n-1)-1 + 

#declaracion
def evalue_tax(monto,tasa=0.18):
    if monto>2000:
        return monto*tasa
    else:
        return monto*tasa-100

impuesto_carlos=evalue_tax(2500)
impuesto_juan=evalue_tax(2200)
print(impuesto_carlos,impuesto_juan)


