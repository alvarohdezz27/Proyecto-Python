from persona import Persona
import logging
import json

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

class Arbitro(Persona):
    def __init__(self, nombre, apellido, edad, pais,partidosArbitrados):
        super().__init__(nombre, apellido, edad, pais)
        self.partidosArbitrados = partidosArbitrados

    def mostrarPersona(self):
        return super().mostrarPersona() + ". Numero de partidos Arbitrados: " + str(self.partidosArbitrados)
    
    @classmethod
    def insertar_elemento(cls):
            logging.info("Intentando añadir un arbitro")
            try:
                datos = input("Introduce un nuevo arbitro (Nombre, apellidos, edad, pais, nº de partidos arbitrados) Separalo todo con , por favor ")
                datos_lista = datos.split(",")

                if len(datos_lista) !=5:
                    print("Error debes introducir exacatamente 5 valores")
                    return
                
                edad_str = datos_lista[2]
                """Comprueba que la edad es un int"""
                try:
                    edad = int(edad_str)
                except ValueError:        
                    return "Error: La edad debe ser un número entero."
                
                try:
                    partidosArbitrados = int(datos_lista[4].strip())
                except ValueError:        
                    return "Error: La edad debe ser un número entero."
            
                nombre = datos_lista[0].strip()
                apellidos = datos_lista[1].strip()
                nacionalidad = datos_lista[3].strip()

    
                if(nombre != "" and apellidos !="" and edad>=18 and nacionalidad !="" and partidosArbitrados !=""):
                    nuevo_arbitro =cls(
                        nombre = nombre,
                        apellido = apellidos,
                        edad = edad,
                        pais = nacionalidad,
                        partidosArbitrados = partidosArbitrados
                    )
 
                    lista = obtenerLista()
                    lista["arbitros"].append(nuevo_arbitro.__dict__)
                    with open("jugadores.json","w",encoding="utf-8") as file:
                        json.dump(lista,file,indent=4,ensure_ascii=False)
                    logging.info("Arbitro añadido: "+ nombre + " " + apellidos)
                    mensaje =(nombre + " " + apellidos + " ha sido añadido correctamente")
                else:
                    logging.warning("Datos inválidos al añadir arbitro")
                    mensaje = ("Error al añadir. Compruebe los datos")
                return mensaje
        

            except Exception as e:
                logging.error("Error inesperado al añadir arbitro")
                return "Error inesperado"
        
    @classmethod
    def buscar_elemento(cls):
            logging.info("Buscando arbitro")
            try:
                nombre = input("Introduce el nombre del arbitro")
                nombreLimpio = nombre.strip()
                lista = obtenerLista()
                arbitros = lista["arbitros"]

                for arbitro in arbitros:
                    if(nombreLimpio.lower() == arbitro["nombre"].lower()):
                        logging.info("Arbitro encontrado")
                        arbitro["nombre"].find
                        return cls(
                            nombre = arbitro["nombre"],
                            apellido = arbitro["apellido"],
                            edad = arbitro["edad"],
                            pais = arbitro["pais"],
                            partidosArbitrados = arbitro["partidosArbitrados"]
                        )
                    
                return None
            except Exception:
                logging.error("Error al buscar jugador")
                return None

    @classmethod
    def modificar_elemento(cls):
        logging.info("Intentando modificar un arbitro")
        nombre = input("Introduce el nombre del arbitro: ")
        nombreLimpio = nombre.strip()
        lista_json = obtenerLista()
        arbitros = lista_json["arbitros"]

        for i,arbitro in enumerate(arbitros):
            if(nombreLimpio.lower() == arbitro["nombre"].lower()):
                try:
                    datos = input("Introduce sus nuevos datos (Nombre, apellidos, edad, pais, nº de partidos arbitrados) Separalo todo con , por favor ")
                    datos_lista = datos.split(",")

                    if len(datos_lista) !=5:
                        print("Error debes introducir exacatamente 5 valores")
                        return
            
                    edad_str = datos_lista[2]
                    """Comprueba que la edad es un int"""
                    try:
                        edad = int(edad_str)
                    except ValueError:        
                        return "Error: La edad debe ser un número entero."
            
                    try:
                        partidosArbitrados = int(datos_lista[4].strip())
                    except ValueError:        
                        return "Error: La edad debe ser un número entero."
            
                    nombre = datos_lista[0].strip()
                    apellidos = datos_lista[1].strip()
                    nacionalidad = datos_lista[3].strip()

    
                    if(nombre != "" and apellidos !="" and edad>=18 and nacionalidad !="" and partidosArbitrados !=""):
                        arbitro_modifcado = cls(
                            nombre = nombre,
                            apellido = apellidos,
                            edad = edad,
                            pais = nacionalidad,
                            partidosArbitrados = partidosArbitrados
                        )
                        arbitros[i] = arbitro_modifcado.__dict__
                        with open("jugadores.json","w",encoding="utf-8") as file:
                            json.dump(lista_json,file,indent=4,ensure_ascii=False)
                            logging.info("Arbitro modificado: " + nombre + " " + apellidos)
                            return (nombre + " " + apellidos + " ha sido modificado correctamente")
                    else:
                        logging.warning("Datos inválidos al modificar el arbitro")
                        return ("Error al añadir. Compruebe los datos")
                    
                except Exception as e:
                    logging.error("Error inesperado al modificar arbitro")
                    return "Error inesperado"
        
    @classmethod
    def eliminar_elemento(cls):
            logging.info("Intentando eliminar arbitro")
            try:
                nombre = input("Introduce el nombre del arbitro: ")
                nombreLimpio = nombre.strip()
                lista_json = obtenerLista()
                arbitros = lista_json["arbitros"]
                for i,arbitro in enumerate(arbitros):
                    if(nombreLimpio.lower() == arbitro["nombre"].lower()):
                        nombreArbitro = arbitro["nombre"]
                        apellidoArbitro = arbitro["apellido"]
                        del arbitros[i]
                        with open("jugadores.json", "w", encoding="utf-8") as file:
                            json.dump(lista_json, file, indent=4, ensure_ascii=False)
                        logging.info("Arbitro eliminado: " + nombreArbitro + " " + apellidoArbitro)
                        mensaje = nombreArbitro + " " + apellidoArbitro + " eliminado correctamente"
                        return mensaje
                    
                mensaje= "Jugador no encontrado"
                return mensaje
            except Exception:
                logging.error("Error al eliminar el arbitro")
                return "Error inesperado"

    @classmethod
    def mostrar_elementos(cls):
            logging.info("Mostrando todos los arbitros")
            try:
                lista_json = obtenerLista()
                arbitros  = lista_json["arbitros"]
                total =""
                for arbitro in arbitros:
                    arbitro_obj = cls(
                        nombre = arbitro["nombre"],
                        apellido = arbitro["apellido"],    
                        edad = arbitro["edad"],
                        pais = arbitro["pais"],
                        partidosArbitrados = arbitro["partidosArbitrados"]
                    )
                    total += arbitro_obj.mostrarPersona() + "\n"
                return total
            except Exception:
                logging.error("Error al mostrar jugadores")
                return "Error al mostrar jugadores"