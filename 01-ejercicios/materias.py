#Mostrar en pantalla el promedio de un alumno que ha cursado 5 materias (Español, Matemáticas, Economía, Programación, Ingles).
print("**********PROMEDIO DE 5 MATERIAS CURSADAS**********")

print("Calificación de la materia Español:")
espanol = float(input())
print("Calificación de la materia Matemáticas:")
matematicas = float(input())
print("Calificación de la materia Economía:")
economia = float(input())
print("Calificación de la materia Programación:")
programacion = float(input())
print("Calificación de la materia Inglés:")
ingles = float(input())

promedio = (espanol+matematicas+economia+programacion+ingles)/5
print(f"El promedio del alumno es: {promedio}")