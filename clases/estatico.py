class Triangulo:

    @staticmethod
    def area(base, altura): # Metodo estático, no le pertenece a la instancia
        return (base * altura)/2

resultado = Triangulo.area(10,20)
print(resultado)
