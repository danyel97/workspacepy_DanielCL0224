from sqlite3 import Connection
import requests
from clases.db import init_db
from clases.producto import Product
def get_cambio():
    url="https://api.apis.net.pe/v1/tipo-cambio-sunat"
    response=requests.get(url)

    # 2. Recupero la informacion como json
    data = response.json()

    # 3. Recupero valor tipo cambio - compra - venta
    dolar_compra = data['compra']
    dolar_venta = data['venta']
    return (dolar_compra,dolar_venta)

def initTable(conexion:Connection):
    try:
        sentencia = """
            CREATE TABLE IF NOT EXISTS PRODUCT(
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100), 
                precio_pen REAL,
                precio_usd REAL 
            );
        """
        cursor=conexion.cursor()
        cursor.execute(sentencia)
        conexion.commit()
    except Exception as e:
        print("ERROR EN INITABLE",e)

def addProduct(conexcion:Connection):
    name=input("Ingrese el nombre")
    precio=float(input("Ingrese el precio"))
    tasa_cambio=get_cambio()
    precio_usd=precio/tasa_cambio[1]
    p1=Product(name,precio_usd,precio)
    try:
        insert_data=(p1.name,p1.precio_pen,p1.precio_usd)
        query="INSERT INTO PRODUCT(nombre,precio_pen,precio_usd) values(?,?,?)"
        cursor=conexcion.cursor()
        cursor.execute(query,insert_data)
        conexcion.commit()
    except Exception as e:
        print("Error al insertar",e)

def getAll(conexion:Connection):
     cursor = conexion.cursor()
     cursor.execute("SELECT * FROM PRODUCT")
     products = cursor.fetchall()
     print(products)

while True:
    conexion=init_db()
    initTable(conexion)
    print("Bienenvido a la Tienda")
    print("Ingrese su opcion")
    print("1.Agregar Producto")
    print("2.Listar Productos")
    print("3.Salir")
    opcion=int(input("Ingrese su opcion:"))
    if opcion==1:
        addProduct(conexion)
    elif opcion==2:
        getAll(conexion)
    elif opcion==3:
        break
    else:
        print("Opcion no valida")