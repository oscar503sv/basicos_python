animal = 'León' #toda variable declarada fuera de una funcion se conoce como variable global

def mostrar_animal():
    global animal
    animal = 'Ballena' # Variables locales
    print(animal)

#puede ser usada tanto dentro como fuera de la función
mostrar_animal()
print(animal)
