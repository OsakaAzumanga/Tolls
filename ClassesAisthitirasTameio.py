import random

class Aisthitiras:
    def __init__(self, tameio):
        self.tameio = tameio

    def anixneyei(self, ePassList):
        return random.choice(ePassList)

class Tameio:
    def __init__(self):
        self.arDieleysewn = 0
        self.esodaDieleysewn = 0

    def addAxiaDieleysis(self, axia):
        self.arDieleysewn += 1
        self.esodaDieleysewn += axia
