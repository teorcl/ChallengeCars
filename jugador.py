class Jugador():
    def __init__(self):
        self.num_players = 0

    def inicio(self):
        self.num_players = int(input('Ingrese el numero de jugadores: '))


jugador1 = Jugador()
jugador1.inicio()
