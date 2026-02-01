from persona import Persona
import json
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)



class Arbitro(Persona):
    def __init__(self, nombre, apellido, edad, pais,partidos_arbitrados):
        super().__init__(nombre, apellido, edad, pais)
        self.partidos_arbitrados = partidos_arbitrados

    def mostrarArbitro(self):
        return f"{self.mostrarPersona()}, ha arbitrado {self.partidos_dirigidos} partidos"