from zamowienie import  Zamowienie
import threading
class Magazyn():
    lock = threading.Lock()

    def __init__(self,typy,pojemnosc):
        self.__pojemnosc = pojemnosc
        self.__ilosc_typow = typy
        self.__stan = []
        self.__zapelnienie = 0
        self.__threadLock = threading.Lock()
        self.__numer_akcji = 0
        for x in range(typy):
            self.__stan.append(0)


    def wolne_miejsce(self, typ):
        if (typ>0):
            return self.__pojemnosc-self.__zapelnienie
        else:
            return self.__zapelnienie

    def wykonywanie_zamowienia(self, z, nrZam):
        ilosc_prod_zamowienia = z.get_ilosc()
        po = ilosc_prod_zamowienia + self.__zapelnienie
        print("[{}] Zamowienie w toku".format(nrZam))
        if (ilosc_prod_zamowienia > 0 and po > self.__pojemnosc):  # producent
            ilosc_prod_zamowienia = self.__pojemnosc - self.__zapelnienie
            print("\tBrak Miejsca na {}  produktow typu {}\n".format(z.get_ilosc() - ilosc_prod_zamowienia, z.get_typ()));

        elif (ilosc_prod_zamowienia < 0 and self.__stan[z.getTyp()] + ilosc_prod_zamowienia < 0):  # konsument
            ilosc_prod_zamowienia = -self.__stan[z.getTyp()];
            print("Odeslanie reszty zamowienia klienta ({}} do konkurencji (sztuk: {} )\n".format(z.get_typ(),
                                                                                                    z.get_ilosc() - ilosc_prod_zamowienia))
        else:
            print("Zamowienie na {} ( {} ) zostalo w pelni wykonane".format(z.get_typ(), z.get_ilosc()))
            if (ilosc_prod_zamowienia<0):
                print("Klient pobral {} ({})".format(z.get_typ(),ilosc_prod_zamowienia))
            else:
                print("Producent przyniosl {} ({})".format(z.get_typ(), ilosc_prod_zamowienia))

        self.__stan[z.get_typ()] += ilosc_prod_zamowienia
        self.__zapelnienie += ilosc_prod_zamowienia
        threadlock2 = threading.Lock()
        threadlock2.acquire()
        self.print_magazyn()
        threadlock2.release()


    def przyjecie_akcji(self, z):
        nrZam=self.__numer_akcji
        print("[{}] Otrzymano zamowienie na produkt typu {}".format(self.__numer_akcji, z.get_typ()))
        self.__numer_akcji += 1

        self.__threadLock.acquire()
        self.wykonywanie_zamowienia(z, nrZam)
        self.__threadLock.release()



    def get_typy(self):
        return self.__ilosc_typow


    def print_magazyn(self):
        print("\t~~Stan magazynu~~")
        for element in range(self.__ilosc_typow):
           print("\tProdukt nr {} sztuk: {}".format(element, self.__stan[element]))


