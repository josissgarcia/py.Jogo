from monstro import Monstro

class Goblin(Monstro):
    def __init__(self, inteligencia):
        super().__init__("Goblin")
        self.inteligencia = inteligencia
    

