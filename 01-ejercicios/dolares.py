#Convertir la cantidad de dólares ingresados por un usuario a pesos colombianos y mostrar el resultado en pantalla.
print("**********CONVERSION DE USD A PESOS COLOMBIANOS**********")
TASA_CAMBIO = 3883.33
print("Ingrese una cantidad en USD:")
dolares = float(input())

total_pesos = dolares * TASA_CAMBIO
print("Conversión a pesos colombianos: ",total_pesos)