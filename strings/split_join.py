lenguajes = "Python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++"

# El método split retorna una lista a partir de un texto
# El texto se divide por medio de un separador default es el espacio
# Entre parentesis se le puede poner el string con el que se quiere dividir

separador = "; "
resultado = lenguajes.split(separador) #resultado es lista
print(resultado)

# El metodo join genera un string a partir de una lista

nuevo_string = " ".join(resultado) #se separan por un espacio en blanco
print(nuevo_string)

texto = """Este es un texto
con
saltos
de

linea"""
resultado = texto.splitlines()
print(resultado)
