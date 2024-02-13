##  v0 tienda  => clientes , productos 

clientes=[
        {'datos':{"nombre":["juan","cornejo rondoy","7776470"],"dni":"7776470"},"direccion":["mz xx cudara12",'localia1','distrito','lima'],"saldo":1500},
        {'datos':{"nombre":["juan","cornejo rondoy","7776444"],"dni":"7776444"},"direccion":["mz xx cudara12",'localia1','distrito','lima'],"saldo":1200},
        {'datos':{"nombre":["juan","cornejo rondoy","7776414"],"dni":"7776414"},"direccion":["mz xx cudara12",'localia1','distrito','lima'],"saldo":100},
        {'datos':{"nombre":["juan","cornejo rondoy","7776449"],"dni":"7776449"},"direccion":["mz xx cudara12",'localia1','distrito','lima'],"saldo":1400},
        {'datos':{"nombre":["juan","cornejo rondoy","7776420"],"dni":"7776420"},"direccion":["mz xx cudara12",'localia1','distrito','lima'],"saldo":200},
        {'datos':{"nombre":["juan","cornejo rondoy","7776431"],"dni":"7776431"},"direccion":["mz xx cudara12",'localia1','distrito','lima'],"saldo":1000}
        ]

productos=[
    {'nombre':"producto1","stock":50,"precio":150,"localia":["lima","aqp","ica"]},
    {'nombre':"producto2","stock":0,"precio":10,"localia":["lima"]},
    {'nombre':"producto3","stock":10,"precio":1500,"localia":[]},
    {'nombre':"producto4","stock":100,"precio":10,"localia":["lima"]},
    {'nombre':"producto5","stock":1000,"precio":40,"localia":["lima"]},
    {'nombre':"producto6","stock":20,"precio":20,"localia":["aqp"]},
    {'nombre':"producto7","stock":30,"precio":200,"localia":["lima"]}
]

"""productos.append({'nombre':inputProduct,'stock':inputStock})
 
    producto_tmp=productos[3]
    productos[3]=newInput
    productos.append(producto_tmp)
    productos.insert(3,newProduct)
"""

print("Bienvenidos a la Tienda datux")
dni=input("ingrese su dni")
print(len(clientes))

lista_compra=[]
lista_dni= [clientes[0]['datos']['nombre'][-1],clientes[1]['datos']['nombre'][-1],clientes[2]['datos']['nombre'][-1],clientes[3]['datos']['nombre'][-1],clientes[4]['datos']['nombre'][-1],clientes[5]['datos']['nombre'][-1]]
lista_producto=[productos[0]['nombre'],productos[1]['nombre'],productos[2]['nombre'],productos[3]['nombre'],productos[4]['nombre'],productos[5]['nombre'],productos[6]['nombre']]
if dni in lista_dni:
    index=lista_dni.index(dni)
    print("el cliente se encuentra en la bd de la tienda ",index)
    print("ejecute la accion a realizar en la tienda")
    print("1.ver saldo")
    print("2.ver mi localia ")
    print("3.comprar productos")
    print("4.salir")
    opcion=int(input("ingrese su opcion:"))
    saldo=clientes[index]["saldo"]
    if opcion==1:  
        msg=f'su saldo es {saldo}'
        print(msg)
    elif opcion==2:
        localia=clientes[index]['direccion'][-1]
        msg=f'su localia es {localia}'
        flag_updated=input('desea actualizarla ? (Si/No)')
        if flag_updated.upper()=='SI':
            new_localia=input('ingrese su nueva localia')
            clientes[index]['direccion'][-1]=new_localia
        else:
            print('gracias !')
    elif opcion==3:
        print(f'lista de productos :{lista_producto}')
        product=input('ingrese el producto a comprar para ver el detalle ').lower()
        if product in lista_producto:
            index_product=lista_producto.index(product)
            print(f'el producto {productos[index]["nombre"]} tiene un costo de {productos[index]["precio"]}')
            flag_carrito=input('desea agregarlo al carrito(si/no )')
            if flag_carrito.upper() =='SI':
                lista_compra.append(productos[index])
                if lista_compra[0]['stock']>0:
                    print('el producto tiene stock')
                    if lista_compra[0]['precio']<saldo:
                        clientes[index]['saldo']=clientes[index]['saldo']-lista_compra[0]['precio']
                        print("gracias por la compra ")
                else:
                    print("el producto no tiene stock")
            else:
                print("gracias")  
        else:
            print("el producto no existe en la lista")
    elif opcion==4:
        print("gracias hasta luego")
    else:
        print("esta opcion no es valida")
else: 
    print("el cliente no se encuentra en la tienda")