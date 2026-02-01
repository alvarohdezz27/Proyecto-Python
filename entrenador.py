from persona import Persona
import json
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

class Entrenador(Persona):
    def __init__(self, nombre, apellido, edad, pais,equipo,titulos):
        super().__init__(nombre, apellido, edad, pais)
        self.equipo = equipo
        self.titulos = titulos

    def mostrarEntrenador(self):
        return f"{self.mostrarPersona()} entrena al {self.equipo} y ha ganado {self.titulos} titulos"
