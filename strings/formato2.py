curso = "Python"
version = "3"

resultado = "Curso de %s %s" %(curso,version)
print(resultado)

#otra forma

resultado = "Curso de {} {}".format(curso,version)
print(resultado)

resultado = "Curso de {a} {b}".format(a=curso,b=version)
print(resultado)

resultado = "Curso de {b} {a}".format(b=curso,a=version)
print(resultado)