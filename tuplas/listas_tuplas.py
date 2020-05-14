lista = ["Curso","Python","CodigoFacilito"]
tupla = ("Introducción","Básico","Listas","Tuplas")

mensaje = "Este es el curso de Python"
# Conversion de listas y tuplas
nueva_lista = list(tupla)
print(nueva_lista)

nueva_tupla = tuple(lista)
print(nueva_tupla)

nueva_lista_dos = list(mensaje)
nueva_tupla_dos = tuple(mensaje)
print(nueva_lista_dos)
print(nueva_tupla_dos)