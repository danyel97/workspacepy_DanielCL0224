
#scope 
x=10

def myUx(x):
    print(x)

myUx(20)
print(x)

## 
## paso por valor a una funcion
def myUxv2(x):
    x+=20
    if x<30:
        print('este es un ',x)
    else:
        x+=20
        print(x)

myUxv2(x)
x+=5
print(x)

