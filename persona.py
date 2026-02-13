import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)


class Persona:
    def __init__(self,nombre,apellido,edad,pais):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.pais = pais
    
    def mostrarPersona(self):
        return f"{self.nombre} {self.apellido}, {self.edad} años, de {self.pais}"
    
    """"""
    
    """Devuelvo el numero de lo que quiere añadir, Jugador, Arbitro o Entrenador y los hijos cogeran ese valor ya para añadir el elemento"""
    @classmethod
    def insertar_elemento(cls):
        logging.info("Intentando añadir una persona")
        try:
            eleccion = int(input("¿Que quieres introducir? 1-Jugador, 2-Arbitro, 3-Entrenador: "))
        except ValueError:
            logging.warning("Entrada no válida en el menú")
            return "Entrada no válida. Por favor, introduce un número."
        
        return eleccion
    
    @classmethod
    def buscar_elemento(cls):
        logging.info("Intentando buscar una persona")
        try:
            eleccion = int(input("¿Que quieres buscar? 1-Jugador, 2-Arbitro, 3-Entrenador: "))
        except ValueError:
            logging.warning("Entrada no válida en el menú")
            return "Entrada no válida. Por favor, introduce un número."
        
        return eleccion

    @classmethod
    def modificar_elemento(cls):
        logging.info("Intentando modificar a una persona")
        try:
            eleccion = int(input("¿Que quieres modifcar? 1-Jugador, 2-Arbitro, 3-Entrenador: "))

        except:
            logging.warning("Entrada no válida en el menú")
            return "Entrada no válida. Por favor, introduce un número."
        
        return eleccion
    
    @classmethod
    def eliminar_elemento(cls):
        logging.info("Intentando eliminar a una persona")
        try:
            eleccion = int(input("¿Que quieres eliminar? 1-Jugador, 2-Arbitro, 3-Entrenador: "))

        except:
            logging.warning("Entrada no válida en el menú")
            return "Entrada no válida. Por favor, introduce un número."
        return eleccion
    
    @classmethod
    def mostrar_elementos(cls):
        logging.info("Intentando mostrar un grupo especifico de personas")
        try:
            eleccion = int(input("¿Que quieres mostrar? 1-Jugador, 2-Arbitro, 3-Entrenador: "))

        except:
            logging.warning("Entrada no válida en el menú")
            return "Entrada no válida. Por favor, introduce un número."
        
        return eleccion

            

        