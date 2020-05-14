cursos = ["python","django","flask","C++","golang","java","php","C#"]

curso = cursos[0]
print(curso)

curso = cursos[-1]
print(curso)

#Generacion de sublista a partir de una lista padre
sublista = cursos[0:3]
print(sublista)

#Desde indice 0 a 5
sublista = cursos[:5]
print(sublista)

#Desde indice 3 en adelante
sublista = cursos[3:]
print(sublista)

#Sublista con saltos
#Sublista desde 1 hasta 7 con saltos de 2 en 2
sublista = cursos[1:7:2]
print(sublista)

#inverso de lista
sublista = cursos[::-1]
print(sublista)