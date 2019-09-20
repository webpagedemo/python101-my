# -*- coding: utf-8 -*-
"""
    Wydrukuj alfabet w porządku naturalnym, 
    a następnie odwróconym w formacie: “mała => duża litera”. 
    W jednym wierszu trzeba wydrukować po pięć takich grup.
"""

print("Alfabet w porządku naturalnym: ")
tmp = ""

for i in range(65, 91):

    litera = chr(i)

    tmp += litera + " => " + litera.lower() + " "
    if i > 65 and (i + 1) % 5 == 0:
        tmp += "\n"

print(tmp)
print("\nAlfabet w porządku odwróconym: ")
for i in range(122, 96, -1):

    litera = chr(i)

    tmp += litera.upper() + " => " + litera + " "
    if (i + 1) % 5 == 0:
        tmp += "\n"

print(tmp)

