# Funciones lambda en Python
#el valor por default 0 es opcional, si se desean poner mas de un parametro
#se separan por comas
#todas las funciones lambda retornan un valor
mi_funcion = lambda grados=0 : (grados*1.8) + 32

resultado = mi_funcion(32)
print(resultado)
