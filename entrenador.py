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

"""En esta clase los metodos funcionan igual que en jugador, solo que con sus respectivos datos"""
class Entrenador(Persona):
    def __init__(self, nombre, apellido, edad, pais,equipo,titulos):
        super().__init__(nombre, apellido, edad, pais)
        self.equipo = equipo
        self.titulos = titulos

    def mostrarEntrenador(self):
        return f"{self.mostrarPersona()} entrena al {self.equipo} y ha ganado {self.titulos} titulos"

    @classmethod
    def añadirEntrenador(cls):
        logging.info("Intentando añadir entrenador")
        try:
            datos = input("Introduce un nuevo entrenador (Nombre,apellidos, edad, pais, equipo,nº de titulos) Separalo todo con , por favor: ")
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
            
            titulos = datos_lista[5]
            try:
                num_titulos = int(titulos)
            except ValueError:
                return "Error: el nº de titulos debe ser un numero entero."
            
            nombre = datos_lista[0].strip()
            apellidos = datos_lista[1].strip()
            nacionalidad = datos_lista[3].strip()
            equipo = datos_lista[4].strip()

            if(nombre !="" and apellidos !="" and edad>=18 and nacionalidad !="" and equipo != ""):
                nuevo_entrenador = cls(
                    nombre = nombre,
                    apellido = apellidos,
                    edad = edad,
                    pais = nacionalidad,
                    equipo = equipo,
                    titulos = num_titulos
                )

                lista = obtenerLista()
                lista["entrenadores"].append(nuevo_entrenador.__dict__)
                with open("jugadores.json","w",encoding="utf-8") as file:
                    json.dump(lista,file,indent=4,ensure_ascii=False)
                logging.info("Jugador añadido: "+ nombre + " " + apellidos)
                mensaje =(nombre + " " + apellidos + " ha sido añadido correctamente")
            else:
                logging.warning("Datos inválidos al añadir entrenador")
                mensaje = ("Error al añadir. Compruebe los datos")
            return mensaje

        
        except Exception as e:
                logging.error("Error inesperado al añadir entrenador")
                return "Error inesperado"
        

    @classmethod
    def buscarEntrenador(cls):
        logging.info("Buscando entrenador")
        try:
            nombre = input("Introduce el nombre del entrenador: ")
            nombreLimpio = nombre.strip()
            lista = obtenerLista()
            entrenadores = lista["entrenadores"]

            for entrenador in entrenadores:
                if(nombreLimpio.lower() == entrenador["nombre"].lower()):
                    logging.info("Entrenador encontrado")
                    return cls(
                        nombre = entrenador["nombre"],
                        apellido = entrenador["apellido"],
                        edad = entrenador["edad"],
                        pais = entrenador["pais"],
                        equipo = entrenador["equipo"],
                        titulos = entrenador["titulos"]   
                    )
            return None


        except Exception:
                logging.error("Error al buscar entrenador")
                return None
        
    @classmethod
    def modificarEntrenador(cls):
        logging.info("Intentando modificar el entrenador")
        try:
            nombre = input("Introduce el nombre del entrenador")
            nombreLimpio = nombre.strip()
            lista_json = obtenerLista()
            entrenadores = lista_json["entrenadores"]

            for i,entrenador in enumerate(entrenadores):
                if(nombreLimpio.lower() == entrenador["nombre"].lower()):
                    datos = input("Introduce los nuevos datos (Nombre,apellidos, edad, pais, equipo,nº de titulos) Separalo todo con , por favor: ")
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

                    titulos = datos_lista[5]
                    try:
                        num_titulos = int(titulos)
                    except ValueError:
                        return "Error: el nº de titulos debe ser un numero entero."
            
                    nombre = datos_lista[0].strip()
                    apellidos = datos_lista[1].strip()
                    nacionalidad = datos_lista[3].strip()
                    equipo = datos_lista[4].strip()

                    if(nombre !="" and apellidos !="" and edad>=18 and nacionalidad !="" and equipo != ""):
                        entrenador_modificado = cls(
                            nombre = nombre,
                            apellido = apellidos,
                            edad = edad,
                            pais = nacionalidad,
                            equipo = equipo,
                            titulos = num_titulos
                        )
                        entrenadores[i] = entrenador_modificado.__dict__
                        with open("jugadores.json","w",encoding="utf-8") as file:
                            json.dump(lista_json,file,indent=4,ensure_ascii=False)
                        logging.info("Entrenador modificado: " + nombre + " " + apellidos)
                        return (nombre + " " + apellidos + " ha sido modificado correctamente")
                    else:
                        logging.warning("Datos inválidos al modificar entrenador")
                        return ("Error al añadir. Compruebe los datos")    


        except Exception:
            logging.error("Error inesperado al modificar entrenador")
            return "Error inesperado"

    @classmethod
    def eliminarEntrenador(cls):
        logging.info("Intentando eliminar entrenador")

        try:
            nombre = input("Introduce el nombre del entrenador que quieras eliminar: ")
            nombreLimpio = nombre.strip()
            lista_json = obtenerLista()
            entrenadores = lista_json["entrenadores"]

            for i,entrenador in enumerate(entrenadores):
                if(nombreLimpio.lower() == entrenador["nombre"].strip().lower()):
                    nombreEntrenador = entrenador["nombre"]
                    apellidoEntrenador = entrenador["apellido"]
                    del entrenadores[i]
                    with open("jugadores.json","w",encoding="utf-8") as file:
                        json.dump(lista_json,file,indent=4,ensure_ascii=False)
                    logging.info("Entrenador eliminado " + nombreEntrenador + " " + apellidoEntrenador)
                    mensaje = nombreEntrenador + " " + apellidoEntrenador + " eliminado correctamente"
                    return mensaje
            mensaje ="Entrenador no encontrado"
            return mensaje
        
        except Exception:
            logging.error("Error al eliminar el entrenador")
            return "Error inesperado"   
        
    @classmethod
    def mostrarEntrenadores(cls):
        logging.info("Mostrando todos los entrenadores")

        try:
            lista_json = obtenerLista()
            entrenadores = lista_json["entrenadores"]
            total=""
            for entrenador in entrenadores:
                entrenador_obj = cls(
                    nombre = entrenador["nombre"],
                    apellido = entrenador["apellido"],
                    edad = entrenador["edad"],
                    pais = entrenador["pais"],
                    equipo = entrenador["equipo"],
                    titulos = entrenador["titulos"]   
                )
                total += entrenador_obj.mostrarEntrenador() + "\n"
            return total
        except Exception:
            logging.error("Error al mostrar entrenadores")
            return "Error al mostrar entrenadores"