#Mostrar en pantalla True o False si la edad ingresada por dos usuarios es la misma.
print("**********COMPARACIÓN DE EDADES**********")

print("Ingresa la edad del usuario 1:")
edad_uno = int(input())
print("Ingresa la edad del usuario 2:")
edad_dos = int(input())

print(f"¿Tienen la misma edad los usuarios? {edad_uno == edad_dos}")