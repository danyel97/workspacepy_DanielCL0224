print("**** Bienvenido al registro de negocios ****")
print("Para aperturar un negocio es necesario que cumpla las siguientes condiciones:")

edad = input("¿Eres mayor de edad?: ")
ruc = input("¿Tiene RUC?: ")
nom_comer = input("¿Tiene nombre comercial?: ")

if edad=="si" and ruc=="si" and nom_comer=="si":
    print("Felicidades!!! Esta apto para para emprender un negocio :D ")
else:
    print("No es apto para abrir un negocio. Vuelva luego.")
