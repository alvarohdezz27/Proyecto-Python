class Persona:
    def __init__(self,nombre,apellido,edad,pais):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.pais = pais
    
    def mostrarPersona(self):
        return f"{self.nombre} {self.apellido}, {self.edad} años, de {self.pais}"
    
