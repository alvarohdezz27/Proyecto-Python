from persona import Persona
import json
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

def obtenerLista():
    try:
        logging.info("Cargando jugadores.json")
        with open("jugadores.json","r",encoding="utf-8") as file:
            datos = json.load(file)
        logging.info("jugadores.json cargado")
        return datos
    except Exception as e:
        logging.error("Error al leer jugadores.json")
        raise



class Jugador(Persona):
    def __init__(self, nombre, apellido, edad, pais,equipo,posicion):
        super().__init__(nombre, apellido, edad, pais)
        self.equipo = equipo
        self.posicion = posicion
        self.goles = 0

    def mostrarjugador(self):
        return f"{self.mostrarPersona()}, juega en {self.equipo} como {self.posicion}. Goles: {self.goles}"
    
    @classmethod
    def añadirJugador(cls):
        logging.info("Intentando añadir jugador")
        try:
            datos = input("Introduce un nuevo jugador (Nombre, apellidos, edad, pais, equipo,posicion) Separalo todo con , por favor ")
            datos_lista = datos.split(",")

            if len(datos_lista) !=6:
                print("Error debes introducir exacatamente 6 valores")
                return
            edad_str = datos_lista[2]
            """Comprueba que la edad es un int"""
            try:
                edad = int(edad_str)
            except ValueError:        
                return "Error: La edad debe ser un número entero."
            
            nombre = datos_lista[0].strip()
            apellidos = datos_lista[1].strip()
            edad = int(edad_str)
            nacionalidad = datos_lista[3].strip()
            equipo = datos_lista[4].strip()
            posicion= datos_lista[5].strip()

    
            if(nombre != "" and apellidos !="" and edad>=15 and nacionalidad !="" and equipo !="" and posicion!=""):
                nuevo_jugador = Jugador (
                    nombre = nombre,
                    apellido = apellidos,
                    edad = edad,
                    pais = nacionalidad,
                    equipo = equipo,
                    posicion= posicion
                )
 
                lista = obtenerLista()
                lista["jugadores"].append(nuevo_jugador.__dict__)
                with open("jugadores.json","w",encoding="utf-8") as file:
                    json.dump(lista,file,indent=4,ensure_ascii=False)
                logging.info("Jugador añadido: "+ nombre + " " + apellidos)
                mensaje =(nombre + " " + apellidos + " ha sido añadido correctamente")
            else:
                logging.warning("Datos inválidos al añadir jugador")
                mensaje = ("Error al añadir. Compruebe los datos")
            return mensaje
        

        except Exception as e:
            logging.error("Error inesperado al añadir jugador")
            return "Error inesperado"

