
#funciones
# parte
# defincion
def mifx():
    print("hola mundo")
# ejecucion o llamado , (callback)
mifx()
# PUEDO HACERLO MUCHAS VECES 
mifx()
mifx()
mifx()


## Funcion con parametros

def mifxv2(nombre):
    print("Hola {}".format(nombre))
# llamdo
    
mifxv2("GIAN")
mifxv2("CARLOS")
mifxv2("MARIA")

## Funcion devolver informacion
def mifxv3(number):
    flag=True
    if number>10:
        flag=False
    else:
        flag=True
    return flag
""" a=int(input('ingresa un valor '))
mifxv2(a) """
bandera=mifxv3(15)

print(bandera)
bandera2=mifxv3(8)
print(bandera2)
