# Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña. 

class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

    def __str__(self):
        return f'Usuario: {self.nombre_usuario} \nContraseña: {self.contraseña}'



# Crea un objeto usando la clase:

usuario1 = Usuario('ibon93', 'contraseñaSegura')

# Impresión de prueba:

print(usuario1)