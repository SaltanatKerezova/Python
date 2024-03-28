tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
zvire = {
    'druh'   : 'Lenochod',
    'jmeno'  : 'Bronislavomir',
    'potrava': 'Ovoce a zelenina',
    'pohlavi': 'kluk',
    # 'karticka pojistence': 'VZP',
}

# to samé jako: slovnik.get(co, 'Neni to tam')

def vyndej_ze_slovniku(slovnik, co):
    if co in slovnik:
        return slovnik[co]
    else:
        return 'Neni to tam.'

cislo_listku = int(input('Zadej cislo listku: '))
vyhra = vyndej_ze_slovniku(tombola, cislo_listku)
print(vyhra)

vlastnost = input('Zadej vlastnost zvirete: ')
vysledek = vyndej_ze_slovniku(zvire, vlastnost)
print(f'Zvire {vlastnost} je {vysledek}.')

