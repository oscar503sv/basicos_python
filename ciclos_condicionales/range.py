"""# Crea una secuencia de numeros desde 0
for valor in range(10):
    print(valor)

# Obteniendo un rango del 10 al 20
for valor in range(10,21):
    print(valor)

# Imprimiendo todos los impares del 1 al 100
for valor in range(1,101,2):
    print(valor)
"""
# Iterando una lista

lista = [1,2,3,4,5,6]

for valor in range(len(lista)):
    print(f"indice: {valor}, valor: {lista[valor]}")

for indice, valor in enumerate(lista):
    print(f"indice: {indice}, valor: {valor}")
