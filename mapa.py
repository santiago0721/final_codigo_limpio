import random
from random import *

from jugador import jugador
from monstruo import monstruo


class mapa:
    def __init__(self,tamaño:int):
        self.tamaño = tamaño
        self.tablero = []
        self.crear_mapa(tamaño)
        self.agregar_beneficios()

    def crear_mapa(self,tamaño):
        for filas in range(tamaño):
            self.tablero.append([])
            for columnas in range(tamaño):
                self.tablero[filas].append([" "])

    def print_mapa(self):
        for i in self.tablero:
            print(i)

    def agregar_beneficios(self):
        self.armas = [["🔫"],["🗡️"],["🛠️"]]
        self.comidas = [["🍔"],["🍟"],["🌮"]]
        self.agregar_al_mapa(self.armas)
        self.agregar_al_mapa(self.comidas)


    def agregar_al_mapa(self,data:list):

        cantidad = randrange(1,self.tamaño)
        contador = 0

        while True:
            if contador == cantidad:
                break
            dato_agregar = choice(data)
            fila = randrange(self.tamaño)
            columna = randrange(self.tamaño)

            if self.tablero[fila][columna] == [" "]:
                self.tablero[fila][columna] = dato_agregar
                contador +=1

    def agregar_personaje(self,personaje):
        while True:
            fila = randrange(self.tamaño)
            columna = randrange(self.tamaño)

            if self.tablero[fila][columna] == [" "]:
                self.tablero[fila][columna] = [personaje.personaje]
                personaje.posicion = (fila,columna)
                break

    def ubi_comida(self,fila,columna):
        if self.tablero[fila][columna] in self.comidas:
            return True
        return False

    def ubi_armas(self,fila,columna):
        if self.tablero[fila][columna] in self.armas:
            return True
        return False

    def ubi_vacia(self,fila,columna):
        if self.tablero[fila][columna] == [" "]:
            return True
        return False

    def moverse_en_el_mapa(self,fila,columna,personaje,ambos=False):
        if ambos:
            self.tablero[fila][columna] += [personaje.personaje]
        else:
            self.tablero[fila][columna] = [personaje.personaje]

    def limpiar_casilla(self,fila,columna,personaje):
        if len(self.tablero[fila][columna]) >1:
            self.tablero[fila][columna].remove(personaje.personaje)
        else:
            self.tablero[fila][columna] = [" "]


