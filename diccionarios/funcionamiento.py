diccionario = {}
diccionario['nombre'] = "Codi" #Para agregar una llave con su valor
print(diccionario)

valor = diccionario["nombre"] #Obtenemos un valor
print(valor)

diccionario['nombre'] = 90 #modificando el valor
print(diccionario)

diccionario_dos = {"a":1,"b":2,"c":3,"d":4}
print(diccionario_dos)

# Para obtener valores de los diccionarios sino existe la llave regresa el valor despues de la coma
resultado = diccionario_dos.get("z","La llave no existe")
print(resultado)


