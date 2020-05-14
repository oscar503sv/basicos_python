# creando la primera funcion

def saluda():
    print("Hola mundo")

saluda()

def crear_mensaje(nombre):
    mensaje = "Hola {}, bienvenido al curso de python 3".format(nombre)
    return mensaje

print("Ingresa tu nombre")
argumento = str(input())
print(crear_mensaje(argumento))
