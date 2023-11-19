"""
En esta solución, se ha estructurado el código para que sea claro y fácil de seguir. Cada función tiene una responsabilidad específica, lo que hace que el código sea más legible y mantenible. Además, se han utilizado constantes para mejorar la comprensión del código y evitar el uso de "números mágicos" o cadenas de texto repetidas.

Notas Adicionales
La función revelar_celdas_vacias y verificar_victoria necesitan ser implementadas según las reglas del Buscaminas.
Este ejercicio es una excelente manera de evaluar y mejorar las habilidades de programación de tus alumnos, enfocándose en las estructuras de datos y el manejo de lógica básica en Python.

"""

import random

def mostrar_tablero(matriz_tablero_jugador: list) -> str:
    '''Muestra la situación del tablero con las celdas reveladas y/o marcadas

    Args:
        matriz_tablero_jugador (list): celdas reveladas y/o marcadas por el jugador

    Retunr:
        str: situación concreta de la partida
    '''
    tablero_posiciones = f'''
  1 2 3 4 5 6 7 8
1 {matriz_tablero_jugador[0][0]} {matriz_tablero_jugador[0][1]} {matriz_tablero_jugador[0][2]} {matriz_tablero_jugador[0][3]} {matriz_tablero_jugador[0][4]} {matriz_tablero_jugador[0][5]} {matriz_tablero_jugador[0][6]} {matriz_tablero_jugador[0][7]}
2 {matriz_tablero_jugador[1][0]} {matriz_tablero_jugador[1][1]} {matriz_tablero_jugador[1][2]} {matriz_tablero_jugador[1][3]} {matriz_tablero_jugador[1][4]} {matriz_tablero_jugador[1][5]} {matriz_tablero_jugador[1][6]} {matriz_tablero_jugador[1][7]}
3 {matriz_tablero_jugador[2][0]} {matriz_tablero_jugador[2][1]} {matriz_tablero_jugador[2][2]} {matriz_tablero_jugador[2][3]} {matriz_tablero_jugador[2][4]} {matriz_tablero_jugador[2][5]} {matriz_tablero_jugador[2][6]} {matriz_tablero_jugador[2][7]}
4 {matriz_tablero_jugador[3][0]} {matriz_tablero_jugador[3][1]} {matriz_tablero_jugador[3][2]} {matriz_tablero_jugador[3][3]} {matriz_tablero_jugador[3][4]} {matriz_tablero_jugador[3][5]} {matriz_tablero_jugador[3][6]} {matriz_tablero_jugador[3][7]}
5 {matriz_tablero_jugador[4][0]} {matriz_tablero_jugador[4][1]} {matriz_tablero_jugador[4][2]} {matriz_tablero_jugador[4][3]} {matriz_tablero_jugador[4][4]} {matriz_tablero_jugador[4][5]} {matriz_tablero_jugador[4][6]} {matriz_tablero_jugador[4][7]}
6 {matriz_tablero_jugador[5][0]} {matriz_tablero_jugador[5][1]} {matriz_tablero_jugador[5][2]} {matriz_tablero_jugador[5][3]} {matriz_tablero_jugador[5][4]} {matriz_tablero_jugador[5][5]} {matriz_tablero_jugador[5][6]} {matriz_tablero_jugador[5][7]}
7 {matriz_tablero_jugador[6][0]} {matriz_tablero_jugador[6][1]} {matriz_tablero_jugador[6][2]} {matriz_tablero_jugador[6][3]} {matriz_tablero_jugador[6][4]} {matriz_tablero_jugador[6][5]} {matriz_tablero_jugador[6][6]} {matriz_tablero_jugador[6][7]}
8 {matriz_tablero_jugador[7][0]} {matriz_tablero_jugador[7][1]} {matriz_tablero_jugador[7][2]} {matriz_tablero_jugador[7][3]} {matriz_tablero_jugador[7][4]} {matriz_tablero_jugador[7][5]} {matriz_tablero_jugador[7][6]} {matriz_tablero_jugador[7][7]}
'''

    return tablero_posiciones


def iniciar_partida(matriz_tablero: list, mapear: dict) -> list:
    '''Genera coordenadas aleatorias hasta un total de 10 minas. Y coloca los números adyacentes las minas

    Args:
        matriz_tablero (list): valores de las celdas iniciales
        mapear (dict): diccionario con los caracteres que representan las celdas vacías y con minas

    Return:
        list: tablero con las minas y los números adyacentes a las minas
    ''' 
    minas = 0
    while minas <= 10:
        fila = int(random.randint(1, 6))
        columna = int(random.randint(1, 6))

        if matriz_tablero[fila][columna] != 'M':
            matriz_tablero[fila][columna] = mapear['mina']
            minas += 1

            # numeros adyacentes
            if matriz_tablero[fila - 1][columna - 1] != 'M':
                matriz_tablero[fila - 1][columna - 1] += 1
            
            if matriz_tablero[fila - 1][columna] != 'M':
                matriz_tablero[fila - 1][columna] += 1

            if matriz_tablero[fila - 1][columna + 1] != 'M':
                matriz_tablero[fila - 1][columna + 1] += 1

            if matriz_tablero[fila][columna - 1] != 'M':
                matriz_tablero[fila][columna - 1] += 1

            if matriz_tablero[fila][columna + 1] != 'M':
                matriz_tablero[fila][columna + 1] += 1

            if matriz_tablero[fila + 1][columna - 1] != 'M':
                matriz_tablero[fila + 1][columna - 1] += 1
            
            if matriz_tablero[fila + 1][columna] != 'M':
                matriz_tablero[fila + 1][columna] += 1

            if matriz_tablero[fila + 1][columna + 1] != 'M':
                matriz_tablero[fila + 1][columna + 1] += 1
    
    return matriz_tablero


def elegir_accion() -> int:
    '''Pregunta al usuario que acción quiere hacer en el juego

    Return:
        int: 1 si quiere revelar una celda, 2 si quiere marcar una celda y 3 si quiere dejar de jugar
    '''
    print('Elige una acción:\n1. Revelar celda\n2. Marcar celda\n3. Salir')
    accion = input('\nTu elección: ')

    while accion != '1' and accion != '2' and accion != '3':
        print('**ERROR** - ACCIÓN NO VÁLIDA')
        accion = input('Tu elección: ')

    return int(accion)


def revelar_celdas(matriz_tablero_jugador: list, matriz_tablero: list, mapear: dict, celdas_reveladas: set) -> list:
    '''Pregunta al usuario por las coordenadas de la celda que quiere revelar

    Args:
        matriz_tablero_jugador (list): tablero que ve el jugador
        matriz_tablero (list): tablero con las minas y los números adyacentes
        mapear (dict): diccionario con los caracteres que representan las celdas vacías y con minas
        celdas_reveladas (set): conjunto con las coordenadas de las celdas ya reveladas

    Return:
        list: con la matriz_tablero_jugador después de revelar una celda y celdas_reveladas a la que se ha añadido las coordenadas de la nueva celda revelada
    '''
    coordenadas = input('Ingresa coordenadas (fila, columna): ')

    while coordenadas.count(' ') >= 1:
        print('**ERROR** - INTRODUCE LAS COORDENADAS SIN ESPACIOS')
        coordenadas = input('Ingresa coordenadas (fila, columna): ')

    while coordenadas in celdas_reveladas:
        print('**ERROR** - ESA CELDA YA HA SIDO REVELADA')
        coordenadas = input('Ingresa coordenadas (fila, columna): ')
    
    celdas_reveladas.add(coordenadas)

    print(f'Revelando celda {coordenadas}...')

    fila = int(coordenadas[0]) - 1
    columna = int(coordenadas[-1]) - 1

    celda = matriz_tablero[fila][columna]

    if celda == 'M':
        return True
    else:
        if celda == 0:
            matriz_tablero_jugador[fila][columna] = mapear['vacia']
        else:
            matriz_tablero_jugador[fila][columna] = celda
        
        resultado = []
        resultado.append(matriz_tablero_jugador)
        resultado.append(celdas_reveladas)

        return resultado
    

def marcar_celdas(matriz_tablero_jugador: list, celdas_marcadas: set) -> list:
    '''Pide al usuario las coordenadas de la celda que quiere marcar

    Args:
        matriz_tablero_jugador (list): tablero que ve el jugador
        celdas_marcadas (set): conjunto con las coordenadas de las celdas marcadas

    Return:
        list: con la matriz_tablero_jugador después de marcar una celda y celdas_marcadas a la que se ha añadido las coordenadas de la nueva celda marcada
    '''
    coordenadas = input('Ingresa coordenadas (fila, columna): ')

    while coordenadas.count(' ') >= 1:
        print('**ERROR** - INTRODUCE LAS COORDENADAS SIN ESPACIOS')
        coordenadas = input('Ingresa coordenadas (fila, columna): ')

    while coordenadas in celdas_marcadas:
        print('**ERROR** - ESA CELDA YA HA SIDO MARCADA')
        coordenadas = input('Ingresa coordenadas (fila, columna): ')
    
    celdas_marcadas.add(coordenadas)

    print(f'Marcando celdas {coordenadas}...')

    fila = int(coordenadas[0]) - 1
    columna = int(coordenadas[-1]) - 1

    matriz_tablero_jugador[fila][columna] = 'F'

    resultado = []
    resultado.append(matriz_tablero_jugador)
    resultado.append(celdas_marcadas)

    return resultado


def verificar_victoria(celdas_reveladas: set) -> bool:
    '''Comprueba si el número de celdas reveladas es igual que 54 (número de celdas vacías)

    Args:
        celdas_reveladas (set): conjunto con las coordenas reveladas en la partida

    Return:
        bool: True si ha revelado todas las celdas vacías / False si todavía le faltan celdas por revelar
    '''
    if len(celdas_reveladas) == 54:
        return True
    else:
        return False


def jugar():
    """
    Esta función ejecuta el juego.

    """
    # Tablero interno donde estarán marcadas las minas
    matriz_tablero = [
        [0, 0, 0, 0, 0, 0, 0, 0], # fila 1
        [0, 0, 0, 0, 0, 0, 0, 0], # fila 2
        [0, 0, 0, 0, 0, 0, 0, 0], # fila 3
        [0, 0, 0, 0, 0, 0, 0, 0], # fila 4
        [0, 0, 0, 0, 0, 0, 0, 0], # fila 5
        [0, 0, 0, 0, 0, 0, 0, 0], # fila 6
        [0, 0, 0, 0, 0, 0, 0, 0], # fila 7
        [0, 0, 0, 0, 0, 0, 0, 0], # fila 8
        [0, 0, 0, 0, 0, 0, 0, 0]  # fila 9
        ]
    
    # Tablero que verá el jugador
    matriz_tablero_jugador = [
        ['.', '.', '.', '.', '.', '.', '.', '.'], # fila 1
        ['.', '.', '.', '.', '.', '.', '.', '.'], # fila 2
        ['.', '.', '.', '.', '.', '.', '.', '.'], # fila 3
        ['.', '.', '.', '.', '.', '.', '.', '.'], # fila 4
        ['.', '.', '.', '.', '.', '.', '.', '.'], # fila 5
        ['.', '.', '.', '.', '.', '.', '.', '.'], # fila 6
        ['.', '.', '.', '.', '.', '.', '.', '.'], # fila 7
        ['.', '.', '.', '.', '.', '.', '.', '.'], # fila 8
        ['.', '.', '.', '.', '.', '.', '.', '.']  # fila 9
        ]
    
    mapear = {'mina': 'M', 'vacia': '_'}

    celdas_marcadas = set()
    celdas_reveladas = set()

    # Empezar la partida
    matriz_tablero = iniciar_partida(matriz_tablero, mapear)

    fin_partida = False

    while fin_partida == False:
        print(f'Celdas marcadas: {len(celdas_marcadas)}') # Número de celdas marcadas en ese momento de la partida
        print(mostrar_tablero(matriz_tablero_jugador))
        accion = elegir_accion()

        # Acción revelar una celda
        if accion == 1:
            lista_resultado = revelar_celdas(matriz_tablero_jugador, matriz_tablero, mapear, celdas_reveladas)
            
            # Comprobar si la celda revelada contenía una mina
            if lista_resultado == True:
                print('\n¡HABÍA UNA MINA EN ESA COORDENADA!. HAS PERDIDO')
                fin_partida = True
            else:
                matriz_tablero_jugador = lista_resultado[0]
                celdas_reveladas = lista_resultado[-1]

            # Comprobar si todas las celdas vacías han sido descubiertas
            if verificar_victoria(celdas_reveladas) == True:
                print('FIN DE LA PARTIDA. ¡HAS GANADO!')
                fin_partida = True

        # Acción marcar una celda
        elif accion == 2:
            lista_resultado = marcar_celdas(matriz_tablero_jugador, celdas_marcadas)
            matriz_tablero_jugador = lista_resultado[0]
            celdas_marcadas = lista_resultado[-1]

            # Comprobar si todas las celdas vacías han sido descubiertas
            if verificar_victoria(celdas_reveladas) == True:
                print('FIN DE LA PARTIDA. ¡HAS GANADO!')
                fin_partida = True

        # Acción salir del juego
        elif accion == 3:
            print('Saliendo del juego...')
            fin_partida = True


if __name__ == "__main__":
    """
    Esta sección del código se ejecuta solo si ejecutamos este archivo directamente.
    """
    jugar()
