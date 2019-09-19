""" 
 Pobierz od użytkownika imię, wiek
 i powitaj go komunikatem: “Mów mi Python, mam x lat. 
 Witaj w moim świecie imie. Jesteś starszy(młodszy) ode mnie.”
"""
import datetime

# bierzacyRok = datetime.datetime.now().strftime("%Y")
bierzacyRok = input("Podaj bierzący rok: ")

dataPowstaniaPythona = 1989

wiekPythona = int(bierzacyRok) - int(dataPowstaniaPythona)

imie = input("Podaj imię: ")
wiek = input("Podaj wiek: ")


roznicaTxt = "młodszy"
if int(wiek) > wiekPythona:
    roznicaTxt = "starszy"

print(
    "Mów mi Python, mam "
    + str(wiekPythona)
    + " lat. Witaj w moim świecie "
    + imie
    + ". Jesteś "
    + roznicaTxt
    + " ode mnie."
)
