# lista = []
#
#for x in range(0,100):
#   lista.append(x)
#
#print(lista)

estructura = [ x for x in range(0,100)] # esta linea de codigo hace lo mismo que lo comentado
print(estructura)

# creando un diccionario con comprehension

diccionario = {indice:valor 
                for indice, valor in enumerate(estructura)}

print(diccionario)
