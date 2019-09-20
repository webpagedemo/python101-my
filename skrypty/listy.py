liczby = [int(x) for x in input("podaj liczby po spacji: ").split(" ")]
print(liczby)

for i, v in enumerate(liczby):
    print("[", i, "]", v)

print()

for i in reversed(liczby):
    print(i, end=" ")

print()

for i in sorted(liczby):
    print(i, end=" ")

print()

e = int(input("którą liczbę usunąć? "))
liczby.remove(e)

print(liczby)
print()

a, i = eval(input("Podaj element i indeks oddzielone przecinkiem: "))
liczby.insert(i, a)

print(liczby)
print()

print("Wyszukiwanie i zliczanie elementu w liście")
e = int(input("Podaj liczbę: "))
print("Liczba wystąpień: ")
print(liczby.count(e))
print("Indeks pierwszego wystąpienia: ")
if liczby.count(e):
    print(liczby.index(e))
else:
    print("Brak elementu w liście")


print("Pobieramy ostatni element z listy: ")
print(liczby.pop())
print(liczby)

print("Część listy (notacja wycinkowa):")
i, j = eval(input("Podaj indeks początkowy i końcowy oddzielone przecinkiem: "))
print(liczby[i:j])

print()
print("Tupla to lista niemodyfikowalna.")
print("Próba zmiany tupli generuje błąd:")
tupla = tuple(liczby)
