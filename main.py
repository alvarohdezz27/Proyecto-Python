from jugador import Jugador 
from entrenador import Entrenador 
from persona import Persona
from arbitro import Arbitro
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

"""Mi idea principal de proyecto es hacer juegos de adivinar cosas relacionadas al futbol. Por ejemplo Un 3 en raya con 6 equipos diciendo en cada casilla un jugador que haya jugado en ambos equipos.
    O un woordle (o ahorcado como se dice aqui en españa para adivinar el nombre de un jugador). Mi proyecto estaria basado en la pagina de google: https://futbol-11.com/
    Mi idea seria hacer unos cuantos juegos parecidos a los de esa pagina y añadir algunos creados por mi"""

#Menu
def menu():
    logging.info("Aplicación iniciada")
    while True:
        try:
            entrada = int(input("¿Que deseas hacer? " \
            "1-Añadir elemento, " \
            "2-Buscar elemento, " \
            "3-Modificar elemento, " \
            "4-Eliminar elemento, " \
            "5-Mostrar todos, " \
            "6-Generar un reporte, " \
            "7-Salir "))
        except ValueError:
            logging.warning("Entrada no válida en el menú")
            print("Entrada no válida. Por favor, introduce un número.")
            continue
        if(entrada ==1):
            eleccion = Persona.insertar_elemento()
            if(eleccion ==1):
                resultado = Jugador.insertar_elemento()
                print(resultado)
            elif(eleccion ==2):
                resultado = Arbitro.insertar_elemento()
                print(resultado)
            elif(eleccion ==3):
                resultado = Entrenador.insertar_elemento()
                print(resultado)
        elif(entrada == 2):
            eleccion = Persona.buscar_elemento()
            if(eleccion ==1):
                resultado = Jugador.buscar_elemento()
                if resultado:
                    print(resultado.mostrarPersona())
            elif(eleccion ==2):
                resultado = Arbitro.buscar_elemento()
                if resultado:
                    print(resultado.mostrarPersona())
            elif(eleccion ==3):
                resultado = Entrenador.buscar_elemento()
                if resultado:
                    print(resultado.mostrarPersona())
        elif(entrada ==3):
            eleccion = Persona.modificar_elemento()
            if(eleccion ==1):
                resultado = Jugador.modificar_elemento()
                print(resultado)
            elif(eleccion ==2):
                resultado = Arbitro.modificar_elemento()
                print(resultado)
            elif(eleccion ==3):
                resultado = Entrenador.modificar_elemento()
                print(resultado)
        elif(entrada ==4):
            eleccion = Persona.eliminar_elemento()
            if(eleccion ==1):
                resultado = Jugador.eliminar_elemento()
                print(resultado)
            elif(eleccion ==2):
                resultado = Arbitro.eliminar_elemento()
                print(resultado)
            elif(eleccion ==3):
                resultado = Entrenador.eliminar_elemento()
                print(resultado)
        elif(entrada==5):
            eleccion = Persona.mostrar_elementos()
            if(eleccion==1):
                resultado = Jugador.mostrar_elementos()
                print("--TOTAL DE JUGADORES--")
                print(resultado)
            elif(eleccion==2):
                resultado = Arbitro.mostrar_elementos()
                print("--TOTAL DE ARBITROS--")
                print(resultado)
            if(eleccion==3):
                resultado = Entrenador.mostrar_elementos()
                print("--TOTAL DE ENTRENADORES--")
                print(resultado)
        elif(entrada ==6):
            resultado = generar_reporte()
            print(resultado)
        else:
            logging.info("Aplicación cerrada por el usuario")
            print("Hasta pronto!")
            break



#Funcion para obtener el json
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


#Ejercicio 3 del examen, segun la entrada que tenga recorre el array de jugadores,entrenadores y arbitros y ya segun ellos ùes vuestro la suma de una cantidad, los nombres y la longitud
def generar_reporte():
    try:
        valor=""
        entrada = int(input("¿Que reporte quieres generar? 1-Jugadores, 2-Entrenadores, 3-Arbitros: "))
    except ValueError:
        logging.warning("Entrada no válida")
        return "Entrada no válida. Por favor, introduce un número."
    if(entrada ==1):
        valor="jugadores"
    elif(entrada ==2):
        valor="entrenadores"
    elif(entrada==3):
        valor="arbitros"
    else:
        return "error"
    
    listas = obtenerLista()
    list = listas[valor]
    nombres = []
    totalGoles = 0
    totalTitulos =0
    totalPartidos = 0

    for linea in list:
        if(entrada ==1):
            numGoles = int(linea["goles"])
            totalGoles += numGoles
        elif(entrada ==2):
            titulos = int(linea["titulos"])
            totalTitulos += titulos
        elif(entrada ==3):
            partidos = int(linea["partidosArbitrados"])
            totalPartidos +=partidos

        nombre = linea["nombre"]
        nombres.append(nombre)
     

    nombres.sort()
    print("Nombres ordenados: ")
    for i in nombres:
        print(i)
    print("Total de nombres: " +  str(len(nombres)))

    if(entrada ==1):
        print("Total de goles entre todos los jugadores: " + str(totalGoles))
    elif(entrada ==2):
        print("Total de titulos entre todos los entrenadores: " + str(totalTitulos))
    elif(entrada ==3):
        print("Total de partidos arbitrados entre todos los arbitros: " + str(totalPartidos))
    else:
        print("ERROR")




menu()
