import threading
import random
from magazyn import *
from zamowienie import *
import time

class Postac(threading.Thread):


    def __init__(self, id, typ, magazyn):
       self.__id = id
       self.__magazyn = magazyn
       self.__typ = typ
       threading.Thread.__init__(self)

    def run(self):
        while True:
            time.sleep(1)
            ilemozna = self.__magazyn.wolne_miejsce(self.__typ)
            zamowienie = Zamowienie(self.losowanie(self.__magazyn.get_typy()+1),self.losowanie(ilemozna)+1)
            """dodatnie jak prod, ujemne jak klient"""
            self.__magazyn.przyjecie_akcji(zamowienie)


    def losowanie(self,typ):
        if typ<2:
           return 0
        r = random.randrange(typ-1)
        return r