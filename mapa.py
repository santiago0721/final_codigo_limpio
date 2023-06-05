import random
from random import *
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
        armas = ["🔫","🗡️","🛠️"]
        comidas = ["🍔","🍟","🌮"]
        self.agregar_al_mapa(armas)
        self.agregar_al_mapa(comidas)


    def agregar_al_mapa(self,data:list):

        cantidad = randrange(self.tamaño)
        contador = 0

        while True:
            if contador == cantidad:
                break
            dato_agregar = choice(data)
            fila = randrange(self.tamaño)
            columna = randrange(self.tamaño)

            if self.tablero[fila][columna] == [" "]:
                self.tablero[fila][columna] = [dato_agregar]
                contador +=1

a = mapa(4)
a.print_mapa()