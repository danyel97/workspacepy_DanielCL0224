class Contacto:
    def __init__(self,nombre,numero):
        self.nombre=nombre
        self.numero=numero
    def __str__(self):
        return f"el contacto es {self.nombre} con numero {self.numero} "
    
class Phone:
    almacenamiento:None
    ram:None
    pixelesCam:None
    display:None
    marca:None
    os:None
    contactos:None
    apps:None
    status:None

    def __init__(self,almacenamiento,ram,pixeles,display):
        self.almacenamiento=almacenamiento
        self.ram=ram
        self.pixelesCam=pixeles
        self.display=display
        self.status=False
        self.contactos=[]

    def getAlmacenamiento(self):
        return (self.almacenamiento,self.ram)
    
    def getDisplay(self):
        return self.display

    def upPhone(self):
        if not self.status:
            self.status=True
            print("Celular encendiendo")    
        else :
            print("Celular prendido")

    def ShutdownPhone(self):
        if self.status:
            self.status=False
            print("Celular apagando")    
        else :
            print("Celular esta apagado")

    def addContacto(self):
        nombre=input("Ingrese el nombre:")
        numero=input("Ingrese el numero")
        contacto=Contacto(nombre,numero)
        self.contactos.append(contacto)
        print(self.contactos)

    def getListContacs(self):
        for item in self.contactos: 
            print(item)
            
    def __str__(self) -> str:
        return f"el celular con {self.almacenamiento}"
    
class Samsung(Phone):
    modelo:str
    def __init__(self,modelo,almacenamiento,ram,pixeles,display,marca="Samsung"):
        super().__init__(almacenamiento,ram,pixeles,display)
        self.marca=marca
        self.modelo=modelo
    def __str__(self) -> str:
        return f"el celular es de marca {self.marca}"

""" 
phone1=Phone(128,16,15,640)
samsungS20=Samsung('GalaxyS20',128,16,15,640)

print(phone1.getAlmacenamiento())
print(samsungS20.getDisplay())

print(phone1)
print(samsungS20)
 """
samsungS20=Samsung('GalaxyS20',128,16,15,640)    
while True:
    msg="""
        Bienvenidos al menu de celular
        1.agregar contacto
        2.ver contactos
        3.Salir
    """
    print(msg)
    try:
        opcion=int(input("Ingrese la opcion:"))
    except Exception as e :
        print(e)
        continue

    if opcion==1:
        samsungS20.addContacto()
    elif opcion==2:
        samsungS20.getListContacs()
    elif opcion==3:
        print("Gracias Hasta luego")
        break    
    else:
        print("Ingrese una opcion correcta")



""" 
class Iphone:
    pass """