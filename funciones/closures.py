def mostrar_mensaje(mensaje):
    mensaje = mensaje.title() #local

    def mostrar():
        print(mensaje)
    return mostrar

nueva_funcion = mostrar_mensaje("Oscar Hernandez")
nueva_funcion()
