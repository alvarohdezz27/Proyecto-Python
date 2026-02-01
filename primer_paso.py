"""Mi idea principal de proyecto es hacer juegos de adivinar cosas relacionadas al futbol. Por ejemplo Un 3 en raya con 6 equipos diciendo en cada casilla un jugador que haya jugado en ambos equipos.
    O un woordle (o ahorcado como se dice aqui en españa para adivinar el nombre de un jugador). Mi proyecto estaria basado en la pagina de google: https://futbol-11.com/
    Mi idea seria hacer unos cuantos juegos parecidos a los de esa pagina y añadir algunos creados por mi"""
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


# En esta funcion lo que hago es pedir al usuario que introduzca los datos dividos por comas para luego con split crear un array, luego con jugadores.json creo un array y añado el ultimo array de jugador para que se añada al json
def añadirElementos():
    logging.info("Intentando añadir jugador")
    try:
        datos = input("Introduce un nuevo jugador (Nombre, apellidos, edad, pais, equipo) Separalo todo con , por favor ")
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
    

        nombre = datos_lista[0].strip()
        apellidos = datos_lista[1].strip()
        nacionalidad = datos_lista[3].strip()
        equipo = datos_lista[4].strip()
    
        if(nombre != "" and apellidos !="" and edad>=15 and nacionalidad !="" and equipo !=""):
            nuevo_jugador = {
                "nombre" : nombre,
                "apellido": apellidos,
                "edad" :edad,
                "pais": nacionalidad,
                "equipo" : equipo
            }

            lista = obtenerLista()
            lista["jugadores"].append(nuevo_jugador)
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

# En esta funcion busco los datos completos con el nombre del jugador, creando un array de jugadores para comprobar uno por uno hasta que coincida el nombre
def buscarElemento():
    logging.info("Buscando jugador")
    try:
        nombre = input("Introduce el nombre del jugador: ")
        nombreLimpio = nombre.strip()
        lista = obtenerLista()
        jugadores = lista["jugadores"]

        for jugador in jugadores:
            if(nombreLimpio.lower() == jugador["nombre"].lower()):
                logging.info("Jugador encontrado")
                return jugador["nombre"] + " " + jugador["apellido"] + " ,edad:" + str(jugador["edad"]) + " ,nacionalidad:" + jugador["pais"] + " ,equipo actual:" + jugador["equipo"] + "\n"
        
        return None
    
    except Exception:
        logging.error("Error al buscar jugador")
        return None

# Para poder modificarlo he utilizado el metodo enumerate, para poder enumerar cada array y poder llevar la cuenta de cuantas veces se ha iterado y asi con el indicie i poder modificarlo
# Hago  lo mismo que en buscarElemento(), creo un array con los jugadores y ya lo recorro, modificandolo gracias a la i.
def modificarElemento():
    logging.info("Intentando modificar jugador")
    try:
        nombre = input("Introduce el nombre del jugador: ")
        nombreLimpio = nombre.strip()
        lista_json = obtenerLista()
        jugadores = lista_json["jugadores"]

        for i,jugador in enumerate(jugadores):
            if(nombreLimpio.lower() == jugador["nombre"].lower()):
                """Pedir nuevos datos"""
                logging.info("Jugador encontrado para modificar")
                datos = input("Introduce los nuevos valores del jugador (Nombre, apellidos, edad, pais, equipo) Separalo todo con , por favor ")
                datos_lista = datos.split(",")

                if len(datos_lista) !=5:
                    print("Error debes introducir exacatamente 5 valores")
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
            
                if(nombre != "" and apellidos !="" and edad>=15 and nacionalidad !="" and equipo !=""):
                    jugadores[i] ={
                        "nombre": nombre,
                        "apellido": apellidos,
                        "edad": edad,
                        "pais": nacionalidad,
                        "equipo": equipo
                    }
                    with open("jugadores.json","w",encoding="utf-8") as file:
                        json.dump(lista_json,file,indent=4,ensure_ascii=False)
                    logging.info("Jugador modificado: " + nombre + " " + apellidos)
                    return (nombre + " " + apellidos + " ha sido modificado correctamente")
                else:
                    logging.warning("Datos inválidos al modificar jugador")
                    return ("Error al añadir. Compruebe los datos")
        logging.info("Jugador no encontrado para modificar")
        return "Jugador no encontrado"
    except Exception:
        logging.error("Error inesperado al modificar jugador")
        return "Error inesperado"

# Y para esta funcion he hecho la misma jugada que modificar, solo que esta vez en vez de modificar, elimino el array
def eliminarElemento():
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
        logging.error("Error al eliminar jugador")
        return "Error inesperado"

# En esta funcion recorro el array y lo almaceno en una variable para poder mostrar todos los datos
def mostrarTodos():
    logging.info("Mostrando todos los jugadores")

    try:    
        lista_json = obtenerLista()
        jugadores = lista_json["jugadores"]
        total = ""
        for jugador in jugadores:
            total += jugador["nombre"] + " " + jugador["apellido"] + " ,edad:" + str(jugador["edad"]) + " ,nacionalidad:" + jugador["pais"] + " ,equipo actual:" + jugador["equipo"] + "\n"
        return total
    
    except Exception:
        logging.error("Error al mostrar jugadores")
        return ""


# El menu para poder utilizar todas las funciones, comprobando si el valor añadido es un numero
def menu():
     logging.info("Aplicación iniciada")
     while True:
        try:
            entrada = int(input("¿Que deseas hacer? 1-Añadir elemento, 2-Buscar elemento, 3-Modificar elemento, 4-Eliminar elemento, 5-Mostrar todos,6-Salir "))
        except ValueError:
            logging.warning("Entrada no válida en el menú")
            print("Entrada no válida. Por favor, introduce un número.")
            continue


        if(entrada == 1):
            resultado =añadirElementos()
            print(resultado)
        elif(entrada == 2):
            resultado = buscarElemento()
            if resultado:
                print(resultado)
            else:
                print("No hemos podido encontrar al jugador")
        elif (entrada ==3):
             resultado =modificarElemento()
             print(resultado)
        elif (entrada == 4):
            resultado = eliminarElemento()
            print(resultado)
        elif (entrada == 5):
            resultado = mostrarTodos()
            print("--TOTAL DE JUGADORES--")
            print(resultado)
        elif(entrada == 6):
            logging.info("Aplicación cerrada por el usuario")
            print("Hasta pronto!")
            break

        else:
            logging.warning("Opción fuera de rango en el menú")

menu()