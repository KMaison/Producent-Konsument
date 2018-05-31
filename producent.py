from postac import Postac
from magazyn import Magazyn

class Producent(Postac):
    def __init__(self, magazyn, id):
        super().__init__(id, 1, magazyn)
