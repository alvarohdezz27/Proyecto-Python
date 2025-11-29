"""Mi idea principal de proyecto es hacer juegos de adivinar cosas relacionadas al futbol. Por ejemplo Un 3 en raya con 6 equipos diciendo en cada casilla un jugador que haya jugado en ambos equipos.
    O un woordle (o ahorcado como se dice aqui en españa para adivinar el nombre de un jugador). Mi proyecto estaria basado en la pagina de google: https://futbol-11.com/
    Mi idea seria hacer unos cuantos juegos parecidos a los de esa pagina y añadir algunos creados por mi"""


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
    except ValueError:
        return "Error: La edad debe ser un número entero."
    

    nombre = datos_lista[0]
    apellidos = datos_lista[1]
    nacionalidad = datos_lista[3]
    equipo = datos_lista[4]
    nuevo_jugador = [nombre,apellidos,edad,nacionalidad,equipo]
    if(nombre != "" and apellidos !="" and edad>=15 and nacionalidad !="" and equipo !=""):
        jugadores.append(nuevo_jugador)
        mensaje =(nombre + " " + apellidos + " ha sido añadido correctamente")
    else:
         mensaje = ("Error al añadir. Compruebe los datos")
    return mensaje

# En esta funcion busco los datos completos con el nombre del jugador, recorriendo el array de jugadires y comprobando que el nombre introducido es igual al  primer valor del array
def buscarElemento():
    nombre = input("Introduce le nombre del jugador: ")
    nombreLimpio = nombre.strip()

    for jugador in jugadores:
        nombreJugador = jugador[0].strip()

        if(nombreLimpio == nombreJugador):
            return jugador
        
    return None

# Para poder modificarlo he utilizado el metodo enumerate, para poder enumerar cada array y poder llevar la cuenta de cuantas veces se ha iterado y asi con el indicie i poder modificarlo
def modificarElemento():
    nombre = input("Introduce le nombre del jugador: ")
    nombreLimpio = nombre.strip()
    for i,jugador in enumerate(jugadores):
        nombreJugador = jugador[0].strip()
        if(nombreLimpio == nombreJugador):
            datos = input("Introduce los nuevos valores del jugador (Nombre, apellidos, edad, pais, equipo) Separalo todo con , por favor ")
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
            nombre = datos_lista[0]
            apellidos = datos_lista[1]
            
            nacionalidad = datos_lista[3]
            equipo = datos_lista[4]
            nuevo_jugador = [nombre,apellidos,edad,nacionalidad,equipo]
            if(nombre != "" and apellidos !="" and edad>=15 and nacionalidad !="" and equipo !=""):
                jugadores[i] = nuevo_jugador
                mensaje =(nombre + " " + apellidos + " ha sido modificado correctamente")
            else:
                mensaje = ("Error al añadir. Compruebe los datos")
            return mensaje

# Y para esta funcion he hecho la misma jugada que modificar, solo que esta vez en vez de modificar, elimino el array
def eliminarElemento():
    nombre = input("Introduce le nombre del jugador que quieras eliminar: ")
    nombreLimpio = nombre.strip()
    for i,jugador in enumerate(jugadores):
        nombreJugador = jugador[0].strip()
        apellidoJugador = jugador[1].strip()
        if(nombreLimpio == nombreJugador):
            del jugadores[i]
            mensaje = nombreJugador + " " + apellidoJugador + " eliminado correctamente"
        else:
            mensaje= "Jugador no encontrado"
    return mensaje

# Ene sta funcion recorro el array y lo almaceno en una variable para poder mostrar todos los datos
def mostrarTodos():
    total = ""
    for jugador in jugadores:
        total += jugador[0] + " " + jugador[1] + " ,edad:" + str(jugador[2]) + " ,nacionalidad:" + jugador[3] + " ,equipo actual:" + jugador[4] + "\n"
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
                nombre = resultado[0]
                apellidos = resultado[1]
                edad = resultado[2]
                nacionalidad = resultado[3]
                equipo = resultado[4]
                print(nombre + " " + apellidos + " " + str(edad) + " "+ " " + nacionalidad + " " + equipo)
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