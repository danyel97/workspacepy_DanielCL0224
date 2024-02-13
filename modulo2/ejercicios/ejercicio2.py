print("rango de 0 al 9")
for i in range(0,10):
    print(i)

print("rango de 1 al 10")
for i in range(0,10):
    print(i)

print("con saltos o steps")

for i in range(0,20,2):
    print(i)

## para convertirlo en una lista se agrega corchetes y un *

# como sumar numeros consecutivos : ejemplo de eficiencia
suma=0
for i in range(0,1001):
    suma+=i

print(suma)

## n => n(n+1)/2
n=1000
sumav2=1000*1001/2
print(sumav2)
    
