# Mostrar en pantalla la cantidad de meses transcurridos desde la fecha de nacimiento de un usuario.
from datetime import date, datetime
print("**********CANTIDAD DE MESES TRANSCURRIDOS DESDE FECHA DE NACIMIENTO**********")

today = date.today()
anio_actual = today.year
anio = int(input("Ingresa tu año de nacimiento?\n"))
mes = int(input("Ingresa tu mes de nacimiento?\n"))
dia = int(input("Ingresa tu dia de nacimiento\n"))

fecha_nacimiento = date(anio, mes, dia)

if today.month < mes:
    if today.day < dia:
        resta_anios = ((anio_actual  - anio - 1) * 12) + today.month - 1 
    else:
        resta_anios = ((anio_actual  - anio - 1) * 12) + today.month  
elif today.day < dia:
    resta_anios = ((anio_actual - anio) * 12) + (today.month - mes) - 1
else:
    resta_anios = ((anio_actual - anio) * 12) + (today.month - mes) 

print("El dia de hoy es",today)
print("Tu fecha de nacimiento es",fecha_nacimiento)
print("Han pasado", resta_anios, "meses hasta ahora")