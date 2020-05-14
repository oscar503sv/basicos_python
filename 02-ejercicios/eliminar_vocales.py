# Eliminar las vocales de la 
# frase ingresada.

frase = input("Ingrasa una frase o palabra: ")
nueva_frase = ''
for letra in frase:
    if letra not in "AEIOUaeiou":
        nueva_frase += letra

print("frase sin vocales".title().center(50,'-'))
print(f"{nueva_frase.rjust(25)}")
