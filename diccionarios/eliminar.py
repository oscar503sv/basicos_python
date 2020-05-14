diccionario = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

print(diccionario)
del diccionario["a"]
print(diccionario)

#otra forma
diccionario.pop("b")
print(len(diccionario))
print(diccionario)
# eliminar todos los elementos

diccionario = {}
print(diccionario)
# otra forma usando el metodo clear

diccionario.clear()
print(diccionario)
