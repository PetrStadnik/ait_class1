
if __name__ == '__main__':
    vstup = input("Zadejte vstup: ")

    zl = ["(", "[", "{"]
    zp = [")", "]", "}"]
    zasobnik = []
    for c in vstup:
        if c in zl:
            zasobnik.append(c)
        elif c in zp:
            print(zasobnik)
            if len(zasobnik) == 0 or zl.index(str(zasobnik.pop())) != zp.index(c):
                print(f"CHYBA: {c} je špatná závorka")
                break

    if len(zasobnik) != 0:
        print("ŠPATNÉ UZÁVORKOVÁNÍ")
    else:
        print("Správně")
