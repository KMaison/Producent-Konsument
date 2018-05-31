from magazyn import *
from zamowienie import *

import producent
import konsument
pojemnosc = 10
typy = 4

magazyn = Magazyn(typy,pojemnosc)

producent1 = producent.Producent(magazyn,1)
producent2 = producent.Producent(magazyn,2)
producent3 = producent.Producent(magazyn,3)

konsument1= konsument.Konsument(magazyn,-1)
konsument2= konsument.Konsument(magazyn,-2)
konsument3= konsument.Konsument(magazyn,-3)


producent1.start()
producent2.start()
producent3.start()

konsument1.start()
konsument2.start()
konsument3.start()

