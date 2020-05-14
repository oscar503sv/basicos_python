import pprint # pretty printing


mensaje = input("Ingresa tu mensaje: ")

contador = {}

# Buscando las vocales en el mensaje
for vocal in mensaje:
    if vocal in "AEIOUaeiou":
        # Si la vocal esta en el mensaje
        # la agregamos al dictionario
        contador.setdefault(vocal, 0)
        contador[vocal] += 1 
print("")
print("cantidad de vocales".title().center(50,'-'))
print(f"\t{pprint.pformat(contador)}")
print("")