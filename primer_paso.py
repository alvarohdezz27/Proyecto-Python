"""Mi idea principal de proyecto es hacer juegos de adivinar cosas relacionadas al futbol. Por ejemplo Un 3 en raya con 6 equipos diciendo en cada casilla un jugador que haya jugado en ambos equipos.
    O un woordle (o ahorcado como se dice aqui en españa para adivinar el nombre de un jugador). Mi proyecto estaria basado en la pagina de google: https://futbol-11.com/
    Mi idea seria hacer unos cuantos juegos parecidos a los de esa pagina y añadir algunos creados por mi"""
import json

def obtenerLista():
    with open("jugadores.json","r",encoding="utf-8") as file:
        datos = json.load(file)
    return datos


# En esta funcion lo que hago es pedir al usuario que introduzca los datos dividos por comas para luego con split crear un array y añadirlo al array de jugadores
def añadirElementos():
    datos = input("Introduce un nuevo jugador (Nombre, apellidos, edad, pais, equipo) Separalo todo con , por favor ")
    datos_lista = datos.split(",")
    if len(datos_lista) !=5:
        print("Error debes introducir exacatamente 5 valores")
        return
    
    edad_str = datos_lista[2]
    """Comprueba que la edad es un int"""
    try:
        edad = int(edad_str)
    except ValueError:        return "Error: La edad debe ser un número entero."
    

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
        mensaje =(nombre + " " + apellidos + " ha sido añadido correctamente")
    else:
         mensaje = ("Error al añadir. Compruebe los datos")
    return mensaje

# En esta funcion busco los datos completos con el nombre del jugador, recorriendo el array de jugadires y comprobando que el nombre introducido es igual al  primer valor del array
def buscarElemento():
    nombre = input("Introduce el nombre del jugador: ")
    nombreLimpio = nombre.strip()
    lista = obtenerLista()
    jugadores = lista["jugadores"]

    for jugador in jugadores:
        if(nombreLimpio.lower() == jugador["nombre"].lower()):
            return jugador["nombre"] + " " + jugador["apellido"] + " ,edad:" + str(jugador["edad"]) + " ,nacionalidad:" + jugador["pais"] + " ,equipo actual:" + jugador["equipo"] + "\n"
        
    return None

# Para poder modificarlo he utilizado el metodo enumerate, para poder enumerar cada array y poder llevar la cuenta de cuantas veces se ha iterado y asi con el indicie i poder modificarlo
def modificarElemento():
    nombre = input("Introduce el nombre del jugador: ")
    nombreLimpio = nombre.strip()
    lista_json = obtenerLista()
    jugadores = lista_json["jugadores"]

    for i,jugador in enumerate(jugadores):
        if(nombreLimpio.lower() == jugador["nombre"].lower()):
            """Pedir nuevos datos"""
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
                return (nombre + " " + apellidos + " ha sido modificado correctamente")
            else:
                return ("Error al añadir. Compruebe los datos")
    return "Jugador no encontrado"

# Y para esta funcion he hecho la misma jugada que modificar, solo que esta vez en vez de modificar, elimino el array
def eliminarElemento():
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
            mensaje = nombreJugador + " " + apellidoJugador + " eliminado correctamente"
            return mensaje
    mensaje= "Jugador no encontrado"
    return mensaje

# En esta funcion recorro el array y lo almaceno en una variable para poder mostrar todos los datos
def mostrarTodos():
    lista_json = obtenerLista()
    jugadores = lista_json["jugadores"]
    total = ""
    for jugador in jugadores:
        total += jugador["nombre"] + " " + jugador["apellido"] + " ,edad:" + str(jugador["edad"]) + " ,nacionalidad:" + jugador["pais"] + " ,equipo actual:" + jugador["equipo"] + "\n"
    return total


# El menu para poder utilizar todas las funciones, comprobando si el valor añadido es un numero
def menu():
     while True:
        try:
            entrada = int(input("¿Que deseas hacer? 1-Añadir elemento, 2-Buscar elemento, 3-Modificar elemento, 4-Eliminar elemento, 5-Mostrar todos,6-Salir "))
        except:
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
            print("Hasta pronto!")
            break



jugadores = [
    ["Lionel Andres","Messi Cuccitini",38,"Argentina","Inter Miami"],
    ["Cristiano Ronaldo", "dos Santos Aveiro",40,"Portugal","Al-Nassr"],
    ["Kylian", "Mbappé Lottin",26,"Francia","Real Madrid"],
    ["Lamine","Yamal Nasraoui",18, "España","FC Barcelona"],
    ["Nicholas", "Williams Arthuer",23, "España","Athletic Club de Bilbao"]
]

menu()