print("Ingrese sus datos correctamente")
nomre = input("Ingrese sus nombres completos: ")
apell = input("Ingrese sus apellidos: ")
edad = input("Ingrese su edad: ")
dni = input("Ingrese el numero de su dni: ")
cel = input("Ingrese el numero de sus celular: ")
msg = "Hola {} {} tus datos son: ".format(nomre,apell)
msg2 = "Tienes " + edad+ " años"
msg3 = ", tu DNI es {} y tu numero de celular es {} .".format(dni, cel)

print(msg+"\n"+msg2+msg3)
