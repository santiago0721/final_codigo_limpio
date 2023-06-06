class jugador:
    def __init__(self):
        self.posicion = (None,None)
        self.personaje = "🧑🏻"
        self.vida: int = 50

    def aumentar_vida(self):
        self.vida += 10
    def disminuir_vida(self):
        self.vida -= 25

    def cambiar_posicion(self,fila,columa):
        self.posicion = (fila,columa)



