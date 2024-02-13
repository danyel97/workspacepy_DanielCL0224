import sys 
print(sys.argv)
dataYear=int(sys.argv[1])
dataCurrent=int(input("Ingrese el año actual"))


if  dataYear<=2012 and (type(dataCurrent)==int):
    print("los datos para mostrar el reporte ....")

else:
    print("los años son incorrectos")


print("comming")