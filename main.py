from jugador import Jugador 
from entrenador import Entrenador 
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

"""Mi idea principal de proyecto es hacer juegos de adivinar cosas relacionadas al futbol. Por ejemplo Un 3 en raya con 6 equipos diciendo en cada casilla un jugador que haya jugado en ambos equipos.
    O un woordle (o ahorcado como se dice aqui en españa para adivinar el nombre de un jugador). Mi proyecto estaria basado en la pagina de google: https://futbol-11.com/
    Mi idea seria hacer unos cuantos juegos parecidos a los de esa pagina y añadir algunos creados por mi"""


def menu():
    logging.info("Aplicación iniciada")
    while True:
        try:
            eleccion = int(input("¿Que campo deseas usar? 1-Jugadores, 2-Entrenadores, 3-Salir: "))
        except ValueError:
            logging.warning("Entrada no válida en el menú")
            print("Entrada no válida. Por favor, introduce un número.")
            continue

        if(eleccion==1):
            try:
                entrada = int(input("¿Que deseas hacer? 1-Añadir elemento, 2-Buscar elemento, 3-Modificar elemento, 4-Eliminar elemento, 5-Mostrar todos,6-Salir "))
            except ValueError:
                logging.warning("Entrada no válida en el menú")
                print("Entrada no válida. Por favor, introduce un número.")
                continue
            if(entrada ==1):
                respuesta = Jugador.añadirJugador()
                print(respuesta)
            elif(entrada ==2):
                respuesta = Jugador.buscarJugador()
                if respuesta:
                    print(respuesta.mostrarjugador())
            elif(entrada ==3):
                respuesta = Jugador.modificarJugador()
                print(respuesta)
            elif(entrada==4):
                respuesta = Jugador.eliminarJugador()
                print(respuesta)
            elif(entrada==5):
                respuesta = Jugador.mostrarJugadores()
                print("--TOTAL DE JUGADORES--")
                print(respuesta)
            else:
                logging.info("Aplicación cerrada por el usuario")
                print("Hasta pronto!")
                break

        elif(eleccion ==2):
            try:
                entrada = int(input("¿Que deseas hacer? 1-Añadir elemento, 2-Buscar elemento, 3-Modificar elemento, 4-Eliminar elemento, 5-Mostrar todos,6-Salir "))
            except ValueError:
                logging.warning("Entrada no válida en el menú")
                print("Entrada no válida. Por favor, introduce un número.")
                continue
            if(entrada ==1):
                respuesta = Entrenador.añadirEntrenador()
                print(respuesta)
            elif (entrada ==2):
                respuesta = Entrenador.buscarEntrenador()
                if(respuesta):
                    print(respuesta.mostrarEntrenador())
                else:
                    print("ERROR")
            elif (entrada ==3):
                respuesta = Entrenador.modificarEntrenador()
                print(respuesta)
            elif (entrada ==4):
                respuesta = Entrenador.eliminarEntrenador()
                print(respuesta)
            elif (entrada == 5):
                respuesta = Entrenador.mostrarEntrenadores()
                print("--TOTAL DE ENTRENADORES--")
                print(respuesta)
            else:
                logging.info("Aplicación cerrada por el usuario")
                print("Hasta pronto!")
                break
        else:
            logging.info("Aplicación cerrada por el usuario")
            print("Hasta pronto!")
            break

menu()
