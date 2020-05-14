# Almacenar 10 numeros enteros
# positivos.

numeros = []
count = 1
suma = 0
print("Almacena 10 numeros positivos".center(30, '-'))
while count <= 10:
    numero = int(input(f"{count}- "))
    if numero >= 0:
        numeros.append(numero)
        suma += numero
        count += 1
    else:
        print("No es un numero valido...")
promedio = suma / count
print('')
print("Tus numeros son los siguientes".center(50,'-'))
print(f"\t{numeros}")
print(f"\nLa suma de los numeros es: {suma}")
print(f"\nEl promedio es: {promedio}")
print(f"\nEl numero mayor es: {max(numeros)}")
print(f"\nEl numero menor es: {min(numeros)}")