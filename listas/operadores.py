lista = [12,14,5,3,12.5,7.2,6.1,4,8]
print(lista)

#ordenar la lista de forma ascendente
lista.sort()
print(lista)

#obteniendo el valor mas bajo
menor = lista[0]
print(menor)

#ordenar de forma descendente
lista.sort(reverse=True)
print(lista)


#obteniendo el valor mas grande
mayor = lista[0]
print(mayor)

#tambien se puede obtener el mayor y menor de esta forma
menor = min(lista)
print(menor)
mayor = max(lista)
print(mayor)

#saber el tamaño de la lista
longitud = len(lista)
print(longitud)

#buscar elementos en la lista
#retorna un valor booleano
resultado = 8 in lista
print(resultado)

#obtener el indice del elemento
indice = lista.index(8)
print(indice)

#cantidad de veces que se encuentra un elemento

contador = lista.count(8)
print(contador)