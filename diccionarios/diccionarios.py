diccionario = {}
#creacion del diccionario
diccionario = dict()

# {llave: valor}

diccionario = {"total": 55 }
diccionario = {"total": 55, "descuento": True, "subtotal": 15}

# Agregar nueva llave valor
diccionario['usuario']='Oscar'

#Actualizar valor mediante una llave

diccionario['usuario']='oscar_gpg'

# Obtener valor mediante una llave
print(diccionario['usuario'])

diccionario_dos = {'Oscar': 1, 'Fernando': 2, 'Uriel': 3, 'Daniela': 4}

diccionario_dos.keys()
diccionario_dos.values()

for key, value in diccionario_dos.items():
    print(key,value)

#metodo get se puede extraer en dado caso la llave no exista