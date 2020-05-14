mensaje = "Este es un texto un poco grande en cuanto a longitud de caracteres se refiere"

resultado = mensaje.count("texto")
print(resultado)

resultado = "texto" in mensaje
print(resultado)

resultado = "texto" not in mensaje
print(resultado)

#find regresa el entero en la posicion que se encuentra

resultado = mensaje.find("texto")
print(resultado)

resultado = mensaje.startswith("Este")
print(resultado)

resultado = mensaje.endswith("refiere")
print(resultado)
