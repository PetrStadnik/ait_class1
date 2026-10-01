
if __name__ == "__main__":
    tajne_cislo = 33
    """
    Nastavíte proměnou na nějaké číslo
    potom necháte uživatele hádat to číslo, pokud se trefí,
    tak mu to řeknete, pokud ne, tak mu napište, 
    jestli je větší nebo menší.
    Bude na to mít 5 pokusů. 
    """
    """
    uhodnuto = False
    for i in range(5):
        c = int(input("Hádej: "))
        if c == tajne_cislo:
            uhodnuto = True
            print("Gratuluju máš to!")
            break
        elif c > tajne_cislo:
            print("zkus menší")
        else:
            print("zkus větší")

    if not uhodnuto:
        print("Smůla došly ti pokusy!!")

    """

    end = False
    i = 0
    while not end:
        i += 1
        print(f"Pokus {i}")
        if i == 5:
            end = True
        c = input("Hádej: ")
        try:
            c = int(c)
        except ValueError:
            print("Zadej číslo")
            continue
        finally:
            print("Zadal si", c)

        if c == tajne_cislo:
            uhodnuto = True
            print("Gratuluju máš to!")
            end = True
        elif c > tajne_cislo:
            print("zkus menší")
        else:
            print("zkus větší")

