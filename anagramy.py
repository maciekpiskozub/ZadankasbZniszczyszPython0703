wyr1 = input("Wprowadz wyrazenie 1:  ").lower()
wyr2 = input("Wprowadz wyrazenie 2:  ").lower()
a = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'r':0, 's':0, 't':0, 'u':0, 'w':0, 'x':0, 'y':0, 'z':0}
b = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'r':0, 's':0, 't':0, 'u':0, 'w':0, 'x':0, 'y':0, 'z':0}

if wyr1==" " and wyr2 == " ":
    print("Wprowadz wartosci!!")
else:
    for i in range(len(wyr1)):
        for klucz, wartosc in a.items():
            if wyr1[i] == klucz:
                a[wyr1[i]] += 1

    for i in range(len(wyr2)):

        for klucz, wartosc in a.items():
             if wyr2[i] == klucz:
                b[wyr2[i]] += 1

    if a == b:
        print("ANAGRAMKI AUUUU")
    else:
        print("NIE MA ANAGRAMKOW")
