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
                nuevo_jugador =cls (
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


    @classmethod
    def buscarJugador(cls):
        logging.info("Buscando jugador")
        try:
            nombre = input("Introduce el nombre del jugador: ")
            nombreLimpio = nombre.strip()
            lista = obtenerLista()
            jugadores = lista["jugadores"]

            for jugador in jugadores:
                if(nombreLimpio.lower() == jugador["nombre"].lower()):
                    logging.info("Jugador encontrado")
                    return cls(
                        nombre = jugador["nombre"],
                        apellido = jugador["apellido"],
                        edad = jugador["edad"],
                        pais = jugador["pais"],
                        equipo = jugador["equipo"],
                        posicion = jugador["posicion"]
                    )
        
            return None
    
        except Exception:
            logging.error("Error al buscar jugador")
            return None
        
    @classmethod
    def modificarJugador(cls):
        logging.info("Intentando modificar jugador")
        try:
            nombre = input("Introduce el nombre del jugador: ")
            nombreLimpio = nombre.strip()
            lista_json = obtenerLista()
            jugadores = lista_json["jugadores"]

            for i,jugador in enumerate(jugadores):
                if(nombreLimpio.lower() == jugador["nombre"].lower()):
                    """Pedir nuevos datos"""
                    datos = input("Introduce los nuevos datos del jugador (Nombre, apellidos, edad, pais, equipo,posicion) Separalo todo con , por favor ")
                    datos_lista = datos.split(",")

                    if len(datos_lista) !=6:
                        print("Error debes introducir exacatamente 6 valores")
                        return
                    edad_str = datos_lista[2].strip()
                    """Comprueba que la edad es un int"""
                    try:
                        edad = int(edad_str)
                    except ValueError:        
                        return "Error: La edad debe ser un número entero."
            
                    nombre = datos_lista[0].strip()
                    apellidos = datos_lista[1].strip()
                    nacionalidad = datos_lista[3].strip()
                    equipo = datos_lista[4].strip()
                    posicion= datos_lista[5].strip()
                    if(nombre != "" and apellidos !="" and edad>=15 and nacionalidad !="" and equipo !="" and posicion!=""):
                        jugador_modificado= cls(
                            nombre = nombre,
                            apellido = apellidos,
                            edad = edad,
                            pais = nacionalidad,
                            equipo = equipo,
                            posicion= posicion
                        )
                        jugadores[i] = jugador_modificado.__dict__
                        with open("jugadores.json","w",encoding="utf-8") as file:
                            json.dump(lista_json,file,indent=4,ensure_ascii=False)
                        logging.info("Jugador modificado: " + nombre + " " + apellidos)
                        return (nombre + " " + apellidos + " ha sido modificado correctamente")
                    else:
                        logging.warning("Datos inválidos al modificar jugador")
                        return ("Error al añadir. Compruebe los datos")

        except Exception:
            logging.error("Error inesperado al modificar jugador")
            return "Error inesperado"
        
    @classmethod
    def eliminarJugador(cls):
        logging.info("Intentando eliminar jugador")

        try:
            nombre = input("Introduce el nombre del jugador que quieras eliminar: ")
            nombreLimpio = nombre.strip()
            lista_json = obtenerLista()
            jugadores = lista_json["jugadores"]
            for i,jugador in enumerate(jugadores):
                if(nombreLimpio.lower() == jugador["nombre"].lower()):
                    nombreJugador = jugador["nombre"]
                    apellidoJugador = jugador["apellido"]
                    del jugadores[i]
                    with open("jugadores.json", "w", encoding="utf-8") as file:
                        json.dump(lista_json, file, indent=4, ensure_ascii=False)
                    logging.info("Jugador eliminado: " + nombreJugador + " " + apellidoJugador)
                    mensaje = nombreJugador + " " + apellidoJugador + " eliminado correctamente"
                    return mensaje
            mensaje= "Jugador no encontrado"
            return mensaje
    
        except Exception:
            logging.error("Error al eliminar el jugador")
            return "Error inesperado"     


    @classmethod
    def mostrarJugadores(cls):
        logging.info("Mostrando todos los jugadores")

        try:    
            lista_json = obtenerLista()
            jugadores = lista_json["jugadores"]
            total = ""
            for jugador in jugadores:
                jugador_obj = cls(
                    nombre = jugador["nombre"],
                    apellido = jugador["apellido"],
                    edad = jugador["edad"],
                    pais = jugador["pais"],
                    equipo = jugador["equipo"],
                    posicion = jugador["posicion"]
                )
                total += jugador_obj.mostrarjugador() + "\n"
            return total
    
        except Exception:
            logging.error("Error al mostrar jugadores")
            return "Error al mostrar jugadores"

