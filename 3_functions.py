zvirata = [
    # druh, jmeno, potrava, pohlavi
    ["Slon", "Pepík", "Ovoce a zelenina", "Kluk"],
    ["Tygr", "Ferda", "Maso", "Kluk"],
    ["Medvěd", "Berta", "Ryby a ovoce", "Holka"],
    ["Žirafa", "Linda", "Listy a větvičky", "Holka"],
    ["Opice", "František", "Ovoce a ořechy", "Kluk"],
    ["Lva", "Šárka", "Maso", "Holka"],
    ["Panda", "Marek", "Bambus", "Kluk"],
    ["Krokodýl", "Bruno", "Maso a ryby", "Kluk"],
    ["Hroch", "Helena", "Tráva a vodní rostliny", "Holka"],
    ["Flamingo", "Anna", "Rakoplaz", "Holka"],
    ["Levhart", "Tomáš", "Maso", "Kluk"],
    ["Kočka", "Mia", "Krmivo pro kočky", "Holka"],
    ["Pes", "Buddy", "Krmivo pro psy", "Kluk"],
    ["Slípka", "Klára", "Zrní", "Holka"],
    ["Krtek", "Matěj", "Červi a hmyz", "Kluk"],
    ["Ježek", "Eliška", "Hmyz a bobule", "Holka"],
    ["Veverka", "Vilém", "Ořechy", "Kluk"],
    ["Krokodýl", "Karolína", "Maso a ryby", "Holka"],
    ["Nosorožec", "Vojtěch", "Tráva a listy", "Kluk"],
    ["Pštros", "Jana", "Plody a semena", "Holka"],
    ["Koala", "Max", "Eukalyptus", "Kluk"],
    ["Klokan", "Natálie", "Tráva a listy", "Holka"],
    ["Pavouk", "Adam", "Hmyz", "Kluk"],
    ["Krokodýl", "Gabriela", "Maso a ryby", "Holka"],
    ["Had", "Oliver", "Malé zvířata", "Kluk"],
    ["Vlčák", "Lucie", "Maso", "Holka"],
    ["Hroch", "Ondřej", "Tráva a vodní rostliny", "Kluk"],
    ["Delfín", "Klára", "Ryby", "Holka"],
    ["Slon", "Tomáš", "Ovoce a zelenina", "Kluk"],
    ["Medvěd", "Kristýna", "Ryby a ovoce", "Holka"]
]

navstevnici = [
    # jmeno, vek, nasi kartu mate?
    ["Jan", 25, True],
    ["Eva", 32, True],
    ["Petr", 45, True],
    ["Jana", 19, False],
    ["Michal", 55, True],
    ["Lucie", 28, True],
    ["Martin", 40, True],
    ["Kateřina", 14, False],
    ["Jakub", 30, True],
    ["Veronika", 22, False],
    ["Tomáš", 38, True],
    ["Barbora", 50, True],
    ["Lukáš", 10, False],
    ["Anna", 60, True],
    ["David", 26, True],
    ["Martina", 35, True],
    ["Pavel", 29, True],
    ["Tereza", 17, False],
    ["Ondřej", 42, True],
    ["Karolína", 20, False],
    ["Filip", 48, True],
    ["Simona", 23, True],
    ["Josef", 33, True],
    ["Alena", 70, True],
    ["Štěpán", 8, False],
    ["Natálie", 27, True],
    ["Roman", 52, True],
    ["Marie", 55, True],
    ["Jaroslav", 37, True],
    ["Zuzana", 24, False]
]

# POKLADNA
# úkoly:
# - nabidnout nasi karticku
# - s kartickou sleva dalších 10%
# - spočítat cenu všech lístků
# - zjistit, kolik navstevniku ma nasi karticku

# PAVILON
# úkoly:
# - nakrmit všechny zvířata
# - roztřídit podle pohlaví
# - vyrobit cedulky na výběhy

print(' Vitej v Zoo Czechitas 🐵🐈 '.center(80, '='))
print('POKLADNA')

def nabidni_karticku(zakaznik):
    """Pokud zakaznik nema karticku, tak mu ji nabidni, jinak nic.
    
    zakaznik: ["Zuzana", 24, False]
    """
    # kdyz dame "end=' '" print neudela novou radku
    # dalsi print pokracuje na stejne radce
    print('A nasi karticku mate?', end=' ')  
    karticka = zakaznik[-1]
    if not karticka:
        print('... a chcete ji?')
    else:
        print('To jsme rádi.')


def sleva(castka, procent=10):
    """Aplikuj slevu.
    
    Základní sleva je 10%
    """
    vysledek = castka * (100 - procent) / 100
    return vysledek


def vypocti_cenu_listku(vek):
    """Vypocti cenu listku na zaklade veku.
    
    deti do 6 let - zadarmo
    mladistvi do 18 - 100
    dospeli do 65 - 150
    seniori - 50
    """

    if vek <= 6:
        cena = 0

    elif vek <= 18:
        cena = 100

    elif vek <= 65:
        cena = 150

    else:
        cena = 50

    return cena


def pracuj_na_pokladne(navstevnici):
    """Zracuj vsechny navstevniky co prisli.
    
    kazdemu:
    - nabidni karticku
    - spoci cenu listku (pripdane dej slevu)
    
    vrat mi kolik navstevniku prislo, jaka byla trzba a kolik bylo karticek
    """
    pocet_navstevniku = 0
    celkova_trzba = 0
    pocet_karticek = 0

    # ["Zuzana", 24, False]
    for navstevnik in navstevnici:
        jmeno = navstevnik[0]
        vek = navstevnik[1]
        ma_karticku = navstevnik[2]

        print(f'Vítej {jmeno}')

        # pocitame vsechny navstevniky
        pocet_navstevniku += 1  # pocet_navstevniku = pocet_navstevniku + 1

        # nabizime karticky
        nabidni_karticku(navstevnik)

        # vypocitavame cenu
        cena_listku = vypocti_cenu_listku(vek)
        
        # pokud ma karticku
        if ma_karticku:
            pocet_karticek += 1              # pocitame karicky
            cena_listku = sleva(cena_listku) # davame slevy

        print(f'listek stoji: {cena_listku}')

        # pocitame celkovou trzbu
        celkova_trzba += cena_listku

    # list obsahujici tri polozky
    vysledek = [pocet_navstevniku, celkova_trzba, pocet_karticek]

    return vysledek  # list trech cisel


# dostaneme list tri cisel
vysledek_prace_na_pokladne = pracuj_na_pokladne(navstevnici)

print(f'celkem prislo: {vysledek_prace_na_pokladne[0]}')
print(f'celkova trzba byla: {vysledek_prace_na_pokladne[1]}')
print(f'lidi s karickou bylo: {vysledek_prace_na_pokladne[2]}')