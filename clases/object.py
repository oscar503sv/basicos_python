class Gato:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def __str__(self):
        return self.nombre

class Pato(object):
    def __init__(self,nombre):
        self.nombre = nombre
    
    def __str__(self):
        return self.nombre

gato = Gato("Bigotes")
pato = Pato("Lucas")
gato.edad = 6
# Con __dict__ se muestran todos los atributos del objeto
print(gato.__dict__)
print(pato.__dict__)
