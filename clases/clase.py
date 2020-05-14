class Usuario:
    def __init__(self, username='', correo='', nombre=''):
        self.username = username
        self.correo = correo
        self.nombre = nombre
    
    def saluda(self):
        print(f"hola, soy el usuario {self.nombre}")

codi = Usuario("codi","codi@gmail.com","Código") # instancia de clase
facilito = Usuario("facilito","facilito@python.com","Facilito")

codi.saluda()
facilito.saluda()
