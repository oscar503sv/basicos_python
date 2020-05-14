tupla = (1, 2, 3, 4, 5, 6)
uno, *dos, tres, cuatro = tupla

print(uno)
print(dos)
print(tres)
print(cuatro)

lista = [10,20,30,40]
tupla_dos = (100,200,300,400)
#generando nuevas tuplas
#funcion zip regresa un objeto de tipo zip

resultado = zip(tupla,lista,tupla_dos)
resultado = tuple(resultado)
print(resultado)
resultado = list(resultado)
print(resultado)
