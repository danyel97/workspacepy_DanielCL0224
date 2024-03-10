
try:
    lista=[1,2,3,4,12,2]
    index=int(input("ingrese un index"))
    a=lista[index]
except Exception as errorMensaje:
    print("this error: ",errorMensaje)
else:
    print(a)
finally:
    print("llamando a otra funcion")