from postac import Postac
from magazyn import Magazyn

class Konsument(Postac):
    def __init__(self, magazyn, id):
        super().__init__(id, -1, magazyn)