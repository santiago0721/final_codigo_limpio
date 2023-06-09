from jugador import *
from mapa import *
from monstruo import *


class juego:
    def __init__(self):
        self.jugador = jugador()
        self.monstruo = monstruo()
        self.iniciar_mapa()

    def iniciar_mapa(self):
        #cambiar aleatorio
        self.mapa = mapa(5)
        self.mapa.agregar_personaje(self.jugador)
        self.mapa.agregar_personaje(self.monstruo)
        self.mapa.print_mapa()
        self.turno_monstruo()
        self.turno_monstruo()
        self.turno_monstruo()
        self.turno_monstruo()


    def turno_monstruo(self):
        print(" ")
        while True:
            nueva_pos = self.monstruo.movimiento()
            if nueva_pos[0] >= 0 and nueva_pos[1] >= 0 and nueva_pos[0] < self.mapa.tamaño and nueva_pos[1] < self.mapa.tamaño:
                break

        if self.mapa.ubi_vacia(nueva_pos[0],nueva_pos[1]) or self.mapa.ubi_armas(nueva_pos[0],nueva_pos[1]):
            self.mapa.moverse_en_el_mapa(nueva_pos[0],nueva_pos[1],self.monstruo)

        elif self.mapa.ubi_comida(nueva_pos[0],nueva_pos[1]):
            self.monstruo.aumentar_vida()
            self.mapa.moverse_en_el_mapa(nueva_pos[0], nueva_pos[1], self.monstruo)

        else:
            self.jugador.disminuir_vida()
            self.mapa.moverse_en_el_mapa(nueva_pos[0], nueva_pos[1], self.monstruo,True)

        fila_actual,columna_actual = self.monstruo.posicion
        self.mapa.limpiar_casilla(fila_actual,columna_actual,self.monstruo)

        self.monstruo.cambiar_posicion(nueva_pos[0],nueva_pos[1])

        self.mapa.print_mapa()





