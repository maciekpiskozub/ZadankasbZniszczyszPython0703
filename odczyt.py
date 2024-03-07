with open('nazwa pliku') as plik:
    dane = plik.read()
    dane = plik.readline()

dane = dane.splitlines()
print(dane)