if __name__ == "__main__":
    """
    uživatel zadá vstup, ošetříte, že je to číslo.
    převecete ho do 16 a 2 soustavy
    vytisknete výsledek.
    """

    mapovani16 = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }
    vstup = input("Vlož číslo ")
    try:
        vstup = int(vstup)
    except ValueError:
        print("ERROR: toto není číslo" )
        exit(1)

    end = False
    mocnina = 10
    vysledek = 11*[0]
    while not end:
        kolik = 0
        while vstup >= (16**mocnina):
            kolik += 1
            vstup -= (16**mocnina)
        if kolik >= 10:
            kolik = mapovani16[kolik]
        vysledek[mocnina] = kolik
        mocnina -= 1
        if mocnina < 0:
            end = True

    print(str(vysledek[::-1]))






