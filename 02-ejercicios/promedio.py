# Mostrar en pantalla el promedio del alumno.

calificaciones = {'calculo': 9, 'historia': 8, 'economia': 10, 'dibujo': 6}
cantidad_de_calificaciones = len(calificaciones)
suma = 0
# sumando los valores de cada materia.
for calificacion in calificaciones.values():
    suma += calificacion

promedio = (suma / cantidad_de_calificaciones)
print(f"el promedio del alumno es: {promedio}")