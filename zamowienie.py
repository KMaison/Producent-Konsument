class Zamowienie:
    def __init__(self,typ,ile):
        self.__typ_produktu = typ
        self.__ilosc = ile

    def get_typ(self):
        return self.__typ_produktu

    def get_ilosc(self):
        return  self.__ilosc


