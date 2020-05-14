texto = "curso de Python 3, Python básico"

resultado = texto.capitalize()
print(resultado)

resultado = texto.swapcase()
print(resultado)

resultado = texto.upper()
print(resultado)

resultado = texto.lower()
print(resultado)

print(resultado.isupper())
print(resultado.islower())

resultado = texto.title()
print(resultado)

#Remplaza parte del texto por otro con el numero 
#Se le indica el número de veces que lo debe reemplazar 
#Por si el texto está más de una vez en el string.
resultado = texto.replace("Python","Ruby",1)
print(resultado)

#El metodo strip le quita los espacios al inicio y final al string
texto_dos = "     curso de Python 3, Python básico    "
resultado = texto.strip()
print(resultado)
