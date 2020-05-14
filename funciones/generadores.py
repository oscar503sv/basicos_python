def tabla_multiplicar(numero, maximo=10):
    for posicion in range(1,maximo+1):
        yield numero * posicion

for resultado in tabla_multiplicar(9):
    print(resultado)

