
import random

# =========================
# CONSTANTES DEL JUEGO
# =========================

FILAS = 10
COLUMNAS = 10

FLOTA = {
    "lancha_1": 1,
    "lancha_2": 1,
    "lancha_3": 1,
    "lancha_4": 1,
    "barco_1": 2,
    "barco_2": 2,
    "barco_3": 2,
    "fragata_1": 3,
    "fragata_2": 3,
    "acorazado": 4
}

AGUA = "~"
BARCO = "B"
IMPACTO = "X"
FALLO = "O"


# =========================
# CLASE TABLERO
# =========================

class Tablero:

    def __init__(self, id_jugador):
        self.id_jugador = id_jugador

        # Tablero propio
        self.tablero = [
            [AGUA for _ in range(COLUMNAS)]
            for _ in range(FILAS)
        ]

        # Tablero donde se registran los disparos realizados
        self.tablero_disparos = [
            [AGUA for _ in range(COLUMNAS)]
            for _ in range(FILAS)
        ]

        # Coordenadas de los barcos que quedan por hundir
        self.barcos = {}

        # Colocamos los barcos al crear el tablero
        self.colocar_barcos()

    def colocar_barcos(self):
        """Coloca todos los barcos aleatoriamente."""

        for nombre, eslora in FLOTA.items():
            colocado = False

            while not colocado:
                f
                ila = random.randint(0, FILAS - 1)
                columna = random.randint(0, COLUMNAS - 1)
                orientacion = random.choice(["H", "V"])

                coordenadas = []

                for i in range(eslora):
                    if orientacion == "H":
                        f = fila
                        c = columna + i
                    else:
                        f = fila + i
                        c = columna

                    coordenadas.append((f, c))

                # Comprobamos que el barco cabe en el tablero
                # y que no se superpone con otro barco
                if all(
                    0 <= f < FILAS
                    and 0 <= c < COLUMNAS
                    and self.tablero[f][c] == AGUA
                    for f, c in coordenadas
                ):
                    for f, c in coordenadas:
                        self.tablero[f][c] = BARCO

                    self.barcos[nombre] = coordenadas
                    colocado = True

    def disparar(self, fila, columna):
        """Registra un disparo recibido."""

        if self.tablero[fila][columna] == BARCO:
            self.tablero[fila][columna] = IMPACTO
            return "impacto"

        elif self.tablero[fila][columna] == AGUA:
            self.tablero[fila][columna] = FALLO
            return "agua"

        else:
            return "repetido"

    def quedan_barcos(self):
        """Comprueba si quedan posiciones de barcos sin impactar."""

        return any(
            celda == BARCO
            for fila in self.tablero
            for celda in fila
        )

    def mostrar_tablero(self, ocultar_barcos=False):
        """Imprime el tablero."""

        print("   " + " ".join(f"{i:2}" for i in range(COLUMNAS)))

        for i, fila in enumerate(self.tablero):
            if ocultar_barcos:
                fila_visible = [
                    AGUA if celda == BARCO else celda
                    for celda in fila
                ]
            else:
                fila_visible = fila

            print(f"{i:2} " + "  ".join(fila_visible))

    def mostrar_disparos(self):
        """Muestra los disparos realizados contra el adversario."""

        print("   " + " ".join(f"{i:2}" for i in range(COLUMNAS)))

        for i, fila in enumerate(self.tablero_disparos):
            print(f"{i:2} " + "  ".join(fila))

    def registrar_disparo(self, fila, columna, resultado):
        """Actualiza el tablero de disparos del jugador."""

        if resultado == "impacto":
            self.tablero_disparos[fila][columna] = IMPACTO
        else:
            self.tablero_disparos[fila][columna] = FALLO


# =========================
# FUNCIONES AUXILIARES
# =========================

def pedir_coordenadas(tablero_disparos):
    """Solicita coordenadas válidas al usuario."""

    while True:
        try:
            fila = int(input("Introduce la fila (0-9): "))
            columna = int(input("Introduce la columna (0-9): "))

            if not (0 <= fila < FILAS and 0 <= columna < COLUMNAS):
                print("Coordenadas fuera del tablero. Inténtalo de nuevo.")
                continue

            if tablero_disparos[fila][columna] != AGUA:
                print("Ya has disparado en esa posición. Prueba otra.")
                continue

            return fila, columna

        except ValueError:
            print("Debes introducir números enteros.")


def disparo_maquina(tablero_jugador):
    """La máquina dispara a una posición aleatoria no utilizada."""

    while True:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)

        if tablero_jugador.tablero[fila][columna] in (AGUA, BARCO):
            return fila, columna


def mostrar_estado(jugador, maquina):
    """Muestra el tablero propio y los disparos al adversario."""

    print("\nTU TABLERO")
    jugador.mostrar_tablero()

    print("\nTUS DISPAROS CONTRA LA MÁQUINA")
    maquina.tablero_disparos  # Tablero de disparos del jugador
    jugador.mostrar_disparos()


# =========================
# PROGRAMA PRINCIPAL
# =========================

def main():

    print("=" * 40)
    print("       HUNDIR LA FLOTA")
    print("=" * 40)
    print("Bienvenido al juego.")
    print("Introduce coordenadas de fila y columna entre 0 y 9.")
    print("X = impacto | O = agua | B = barco | ~ = sin disparar")
    print("Si aciertas, vuelves a disparar.")
    print()

    # Inicialización de los dos jugadores
    jugador = Tablero("Jugador")
    maquina = Tablero("Máquina")

    turno_jugador = True

    while jugador.quedan_barcos() and maquina.quedan_barcos():

        if turno_jugador:

            mostrar_estado(jugador, maquina)

            print("\nTU TURNO")

            fila, columna = pedir_coordenadas(
                jugador.tablero_disparos
            )

            resultado = maquina.disparar(fila, columna)

            jugador.registrar_disparo(fila, columna, resultado)

            if resultado == "impacto":
                print("¡Tocado! Has acertado. Puedes volver a disparar.")

                if not maquina.quedan_barcos():
                    break

                # El jugador conserva el turno
                turno_jugador = True

            else:
                print("Agua. Ahora dispara la máquina.")
                turno_jugador = False

        else:

            print("\nTURNO DE LA MÁQUINA")

            fila, columna = disparo_maquina(jugador)

            print(
                f"La máquina dispara a la fila {fila}, "
                f"columna {columna}."
            )

            resultado = jugador.disparar(fila, columna)

            if resultado == "impacto":
                print("¡La máquina te ha dado! Vuelve a disparar.")

                if not jugador.quedan_barcos():
                    break

                turno_jugador = False

            else:
                print("La máquina ha fallado. Te toca.")

                turno_jugador = True

    # Resultado final
    print("\n" + "=" * 40)
    print("FIN DE LA PARTIDA")

    if maquina.quedan_barcos():
        print("La máquina ha ganado. ¡Otra vez será!")
    else:
        print("¡ENHORABUENA! ¡HAS HUNDIDO TODA LA FLOTA!")

    print("\nTu tablero final:")
    jugador.mostrar_tablero()

    print("\nTablero final de la máquina:")
    maquina.mostrar_tablero()


if __name__ == "__main__":
    main()
