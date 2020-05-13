#Convertir los grados centígrados ingresados por un usuario a grados Fahrenheit y mostrar el resultado en pantalla.

print("**********CONVERSIÓN DE GRADOS CELCIUS A FAHRENHEIT**********")
print("Ingrese los grados CELCIUS:")
celcius = float(input())

grados_fahrenheit = (celcius * 9/5) + 32
print("Conversión a grados Fahrenheit es:",grados_fahrenheit)