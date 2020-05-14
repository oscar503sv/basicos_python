def suma(*args):
    total = 0
    for valor in args:
        total+=valor
    return total

resultado = suma(10,20,30,40)
print(resultado)

def usuarios_autenticados(**kwargs):
    print(kwargs)

usuarios_autenticados(Codi=True,Facilito=False)

def combinacion(requerido,*args,**kwargs):
    print(requerido)
    print(args)
    print(kwargs)

combinacion("Valor requerido", 10, 20, valor_uno=True, valor_dos=False)