class Animal:
    def comer(self):
        print("Comiendo")
    
    def dormir(self):
        print("Durmiendo")

class Mascota:
    def fecha_adopcion(self,fecha):
        self.fecha_de_adopcion = fecha

class Perro(Animal,Mascota): # Entre parentesis la clase padre, Python soporta herencia multiple separando clases padre por comas
    def __init__(self,nombre):
        self.nombre = nombre
    
    def ladrar(self):
        print("Ladrando")

    def dormir(self): # Sobreescribiendo el metodo de la clase padre (override)
        print(self.nombre, "está durmiendo")

firulais = Perro("Firulais")

firulais.ladrar()
firulais.comer()
firulais.dormir()
firulais.fecha_adopcion("Hoy")
print(firulais.fecha_de_adopcion)