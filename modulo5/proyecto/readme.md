# Proyecto Datux
0. solo se puede trabajar desde local quiere decir que no de github
1. cambiar la ruta de la imagen
2. Cambiar el texto del boton de la linea 36 del archivo view.py
3. instalar pandas ( pip install pandas, pip install seaborn)
4. cambiar la funcion generate_graph : los labels y las columnas del grafico
    4.1 en la linea  53 del archivo view determina el tipo de grafico.
    ejemplo de diversas formas de graficar 
    ax.plot(data['Age'], data['mean'], label='Promedio de Ventas')
    ax.hist(data['Age'], bins=20, color='blue', alpha=0.7, label='Edad')
    ax.bar(data['Age'], data['mean'], color='green', alpha=0.7, label='Promedio de Ventas')
    ax.scatter(data['Age'], data['mean'], alpha=0.7)
    ax.scatter(data['Age'], data['mean'], alpha=0.7, marker='o')
    ax.scatter(data['Age'], data['mean'], alpha=0.7, label='Puntos de Datos')
    ax.scatter(data['Age'], data['mean'], alpha=0.7, c=data['tercera_variable'], cmap='viridis')
    ax.pie(data['Sales'], labels=data['Category'], autopct='%1.1f%%', startangle=90)
    ax.fill_between(data['DatAgee'], data['mean'], data['tercera_variable'], color='skyblue', alpha=0.4)
    ax.boxplot(data['Values'], vert=False)
    ax.imshow(data, cmap='viridis', interpolation='nearest') " este mapa de calor mayormente funciona con datos sin agrupar quiere decir que no es necesario filtar"

    es cambiar la linea 53

5. en el archivo proyecto => servicios => transformation la linea 29

# lista de preguntas propuestas
Cantidad/Monto de compras por genero
Cantidad/Monto de compra para familias de mas 1 persona
Cantidad/Monto de compras solteros /casados ( diagrama torta)
Monto maximo que gasta personas mayores/menores de 30 años
Monto minimo que gasta personas mayores/menores de 30 años
Relacion de gasto mensual con ingreso mensual 
Cantidad de pedidos por rating de restaurante


# specch para linkedIn

📚¡Saludos, comunidad de LinkedIn! Quiero compartir con ustedes los avances que he logrado en mi curso de Python, enfocándome en desarrollar habilidades para realizar un análisis básico de datos. Recientemente, he trabajado en parametrizar un dataset y aplicar ese conocimiento para crear diversos gráficos representativos. Un ejemplo concreto sería el "respuesta a la pregunta seleccionada*", logrando visualizar estos insights de manera efectiva 📊.
@datuxperu @gianmarcogutierrez

#Datux #Datos #Dataset #Python #Data

*Ejemplo de respuesta: análisis de la relación entre la edad de los consumidores y sus patrones de consumo