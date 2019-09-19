# -*- coding: utf-8 -*-

import random

from totomodul import ustawienia, losujliczby, pobierztypy, wyniki
from totomodul import czytaj_json, zapisz_json
from totomodul import zapisz_str, czytaj_str
import time

# program główny

# ustalamy trudność gry
nick, ileliczb, maksliczba, ilerazy = ustawienia()

nazwapliku = nick + ".json"
losowania = czytaj_json(nazwapliku)

# losujemy liczby
liczby = losujliczby(ileliczb, maksliczba)

# pobieramy typy użytkownika i sprawdzamy, ile liczb trafił
for i in range(ilerazy):
    typy = pobierztypy(ileliczb, maksliczba)
    trafione = wyniki(set(liczby), typy)

losowania.append(
    {
        "czas": time.time(),
        "dane": (ileliczb, maksliczba),
        "wylosowane": liczby,
        "ile": trafione,
    }
)

zapisz_json(nazwapliku, losowania)

nazwapliku = nick + "2.txt"
zapisz_str(nazwapliku, losowania)
czytaj_str(nazwapliku)


print("Wylosowane liczby:", liczby)
print("\n", losowania)

