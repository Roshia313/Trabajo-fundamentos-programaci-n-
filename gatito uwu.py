import random #sirve para generar valores aleatorios 

def imprimir_tablero(tablero):
    # Imprime el tablero de juego en su estado actual.
    # Itera sobre cada fila del tablero y las une con "|" para formatear el tablero como una cuadrícula.
    for fila in tablero:
        print("|".join(fila))
    print("\n")

def chequear_victoria(tablero, jugador):
    # Verifica si el jugador ha ganado el juego.
    # Chequea cada fila para ver si todas las casillas son iguales al símbolo del jugador.
    for fila in tablero:
        if all([casilla == jugador for casilla in fila]):
            return True
    # Chequea cada columna para ver si todas las casillas son iguales al símbolo del jugador.
    for columna in range(3):
        if all([tablero[fila][columna] == jugador for fila in range(3)]):
            return True
    # Chequea la diagonal principal y la diagonal inversa para ver si todas las casillas son iguales al símbolo del jugador.
    if all([tablero[i][i] == jugador for i in range(3)]) or all([tablero[i][2-i] == jugador for i in range(3)]):
        return True
    return False

def movimiento_computadora(tablero, jugador):
    # Determina un movimiento aleatorio para la computadora.
    # Genera una lista de todas las posiciones vacías en el tablero.
    movimientos_disponibles = [(fila, columna) for fila in range(3) for columna in range(3) if tablero[fila][columna] == " "]
    # Selecciona y retorna una posición vacía aleatoria de la lista de movimientos disponibles.
    return random.choice(movimientos_disponibles)

def jugar_gato_vs_com():
    # Lógica del juego de Gato donde el jugador 1 juega contra la computadora.
    tablero = [[" " for _ in range(3)] for _ in range(3)]  # Inicializa el tablero vacío de 3x3.
    jugador_actual = "X"  # Define al jugador 1 como "X".
    print("¡Bienvenido al juego de Gato (Jugador 1 vs COM)!")
    while True:
        imprimir_tablero(tablero)  # Imprime el tablero en cada turno.
        if chequear_victoria(tablero, "X"):  # Verifica si el jugador 1 ha ganado.
            print("¡Felicidades J1 ha ganado!")
            break
        elif chequear_victoria(tablero, "O"):  # Verifica si la computadora ha ganado.
            print("¡La computadora ha ganado!")
            break
        elif all([casilla != " " for fila in tablero for casilla in fila]):  # Verifica si el tablero está lleno y el juego es un empate.
            print("¡El juego ha terminado en empate!")
            break
        if jugador_actual == "X":  # Turno del jugador 1.
            fila,columna=3,3
            while fila<0 or fila>2:
                fila = int(input("Jugador 1 (X), ingrese el número de fila (1-3): ")) - 1
                columna = int(input("Jugador 1 (X), ingrese el número de columna (1-3): ")) - 1
                if fila<0 or fila>2:
                    print("Seleccion de fila fuera de regla, reintente.")
                if columna<0 or columna>2:
                    print("Seleccion de columna fuera de regla, reintente.")
        else:  # Turno de la computadora.
            fila, columna = movimiento_computadora(tablero, jugador_actual)
        if tablero[fila][columna] == " ":  # Verifica si la casilla está vacía antes de hacer el movimiento.
            tablero[fila][columna] = jugador_actual  # Actualiza el tablero con el símbolo del jugador actual.
            jugador_actual = "O" if jugador_actual == "X" else "X"  # Alterna entre los jugadores.
        else:
            print("¡Esa casilla ya está ocupada! Intente nuevamente.")  # Mensaje de error si la casilla está ocupada.

def jugar_gato_vs_jugador():
    # Lógica del juego de Gato donde dos jugadores se enfrentan.
    tablero = [[" " for _ in range(3)] for _ in range(3)]  # Inicializa el tablero vacío de 3x3.
    jugador_actual = "X"  # Define al jugador 1 como "X".
    print("¡Bienvenido al juego de Gato (Jugador 1 vs Jugador 2)!")
    while True:
        imprimir_tablero(tablero)  # Imprime el tablero en cada turno.
        if chequear_victoria(tablero, "X"):  # Verifica si el jugador 1 ha ganado.
            print("¡Felicidades J1 (X) ha ganado!")
            break
        elif chequear_victoria(tablero, "O"):  # Verifica si el jugador 2 ha ganado.
            print("¡Felicidades J2 (O) ha ganado!")
            break
        elif all([casilla != " " for fila in tablero for casilla in fila]):  # Verifica si el tablero está lleno y el juego es un empate.
            print("¡El juego ha terminado en empate!")
            break
        fila = int(input(f"Jugador {jugador_actual} ({jugador_actual}), ingrese el número de fila (1-3): ")) - 1
        columna = int(input(f"Jugador {jugador_actual} ({jugador_actual}), ingrese el número de columna (1-3): ")) - 1
        if tablero[fila][columna] == " ":  # Verifica si la casilla está vacía antes de hacer el movimiento.
            tablero[fila][columna] = jugador_actual  # Actualiza el tablero con el símbolo del jugador actual.
            jugador_actual = "O" if jugador_actual == "X" else "X"  # Alterna entre los jugadores.
        else:
            print("¡Esa casilla ya está ocupada! Intente nuevamente.")  # Mensaje de error si la casilla está ocupada.

def menu():
    # Menú principal para seleccionar el modo de juego.
    print("Bienvenido al juego de Gato")
    print("Menú:")
    print("1. Nueva partida (Jugador 1 vs COM)")
    print("2. Versus (J1 vs J2)")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")  # Solicita al usuario que seleccione una opción del menú.

    if opcion == "1":
        jugar_gato_vs_com()  # Inicia el juego de Jugador 1 vs computadora.
    elif opcion == "2":
        jugar_gato_vs_jugador()  # Inicia el juego de Jugador 1 vs Jugador 2.
    elif opcion == "3":
        print("¡Gracias por jugar!")  # Salida del programa.
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")  # Mensaje de error para opciones inválidas.
        menu()  # Vuelve a mostrar el menú para seleccionar una opción válida.
menu()  # Llama a la función del menú.
    
    #estudiar su fuinsion y su significado:

    #all siesque todo esta funcionando funsiona y sino no funciona 

    #if all([tablero[fila][columna] == jugador for fila in range(3)]):
    #revisa las files para ver si todos los sinvolos son del jugador 

   