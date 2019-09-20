op = "t"

while op == "t":
    a, b, c = [
        int(x) for x in input("Podaj długości boków trójkąta po spacji: ").split(" ")
    ]

    zmienne = [a, b, c]
    zmienne.sort(reverse=True)

    if zmienne[0] > zmienne[1] + zmienne[2]:
        print("Nie można stworzyć trójkąta. Błędne długości boków.")
        exit()

    # Czy trójkąt równoboczny
    if zmienne[0] ** 2 == zmienne[1] ** 2 + zmienne[2] ** 2:
        print("\nTrójkąt jest prostokątny")

    # pole trójkąta
    poleTrojkata = (zmienne[0] + zmienne[1] + zmienne[2]) / 2
    print("\nPole trójkąta wynosi: ", poleTrojkata)

    # obwód trójkąta
    obwodTrojkata = zmienne[0] + zmienne[1] + zmienne[2]
    print("\nObwód trójkąta wynosi: ", obwodTrojkata)

    op = input("Spróbujesz jeszcze raz (t/n): ")
