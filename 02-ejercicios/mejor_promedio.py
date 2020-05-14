# Mostrar en pantalla el mejor promedio.

calificaciones = {'calculo': 9, 'historia': 10, 'economia': 9, 'dibujo': 6}
# variables que mas tarde se utlizaran
calificacion = 0
materia = ''
# buscando el promedio mas alto
for k, v in calificaciones.items():
    if calificacion < v:
    # asignando el valor mas alto para 
    # posteriormente desplegarlo en pantalla.    
        materia = k
        calificacion = v

print(f"El mejor promedio es: {materia.title()} - {calificacion}")