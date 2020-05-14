""" Las notaciones sirven para hacer más legible el código
    en el ejemplo se coloca la notacion que tipo de dato se espera recibir como parametro
    luego con la flecha -> se especifica el valor que retornara la funcion
    se puede poner: None, int, float, bool, str"""
def sumar(val1 : float, val2 : float) -> float:
    return val1 + val2

print(sumar(50,30))

def restar(val1 : int, val2 : int) -> int:
    return val1 - val2

print(restar(100,60))
