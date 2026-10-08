cenik = {
    "maslo": (55, 0),
    "chleba": (20, 5),
    "vajcka6": (30, 10),
    "rohlík": (2, 0),
    "vanocka": (25, 25),
    "parek": (13, 0),
    "tvahor": (32, 1)
}

def pridej(kosik:dict[str, int], produkt:str) -> dict[str, int]:
    if produkt not in cenik.keys():
        raise NameError("Produkt neexistuje v ceníku")
    else:
        if produkt in kosik.keys():
            kosik[produkt] += 1
        else:
            kosik[produkt] = 1
    return kosik

def odeber(kosik:dict, produkt:str):
    if produkt not in kosik.keys():
        return kosik
    else:
        if kosik[produkt] > 1:
            kosik[produkt] -= 1
        else:
            kosik.pop(produkt)
        return kosik

def celkem_bez_slevy(kosik:dict, cenik:dict) -> float:
    celkem = 0.
    for produkt in kosik.keys():
        celkem += kosik[produkt] * cenik[produkt][0]
    return celkem

def celkem_se_slevou(kosik:dict, cenik:dict) -> float:
    celkem = 0.
    for produkt in kosik.keys():
        celkem += kosik[produkt] * cenik[produkt][0] * (1 - cenik[produkt][1]/100)
    return celkem