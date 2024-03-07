data = input("Podaj date urodzenia (FORMAT: rrrr/mm/dd): ")
liczba = 0
liczba2 = 0

while liczba >= 0 and liczba<=9:
    for i in range(len(data)):
        liczba = liczba + int(data[i])
    print(liczba)

    wynik = str(liczba)
    for i in range(len(wynik)):
        liczba2 = liczba2 + int(wynik[i])
    print(liczba2)








