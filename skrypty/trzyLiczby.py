op = "t"

while op == "t":
    a, b, c = input("Podaj trzy liczby oddzielone spacjami: ").split(" ")

    liczby = [a, b, c]

    print("Wprowadzono liczby:", a, b, c)
    print("\nNajmnijsza: ")

    liczby.sort()

    print(liczby[0])

