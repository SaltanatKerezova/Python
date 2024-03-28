zvire_list = ["Lenochod", "Bronislavomír", "Ovoce a zelenina", "Kluk"]
navstevnik_list =  ["Jana", 19, False]

# slovnik !!!
zvire = {
    'druh'   : 'Lenochod',
    'jmeno'  : 'Bronislavomir',
    'potrava': 'Ovoce a zelenina',
    'pohlavi': 'kluk',
}
navstevnik = {
    'jmeno'   : 'Jana',
    'vek'     : 19,
    'karticka': True,
    'deti'    : ['Pepik', 'Anicka'],
}
cisla = {
    1: 'jedna',
    2: 'dva',
    3: 'tri',
}

if navstevnik['karticka']:
    sleva = 'ma slevu'
else:
    sleva = 'nema slevu'

print(f'Prislel navstevnik {navstevnik["jmeno"]}, a {sleva}.')

#---------------------------------

zvire = {
    'druh'   : 'Lenochod',
    'jmeno'  : 'Bronislavomir',
    'potrava': 'Ovoce a zelenina',
    'pohlavi': 'kluk',
}

# vypis hodnoty
jmeno = zvire['jmeno']
print(jmeno)

# pridavam (proste zalozim novy klic)
zvire['barva'] = 'hnedo-sediva'
print(zvire)

# takhle prepisuji (prirazuji ke klici, ktery uz ve slovniku je)
zvire['pohlavi'] = 'holka'
print(zvire)

# mazani (dva druhy)
# pop
barva = zvire.pop('barva')  # pop nam hodnotu jeste vrati
print(barva)  # tady jsme ji mohli jeste vypsat
print(zvire)  # lenochod barvu uz nema

# del
del zvire['pohlavi']  # vypari se primo ze slovniku
print(zvire)  # lenochod uz neni kluk


#---------------------------------


zvire = {
    'druh'   : 'Lenochod',
    'jmeno'  : 'Bronislavomir',
    'potrava': 'Ovoce a zelenina',
    'pohlavi': 'kluk',
    # 'karticka pojistence': 'VZP',
}

print('a' in 'ahoj')
print(1 in [1, 2, 3])
print('pohlavi' in zvire)

# Tohle nepujde, protoze tento klic ve slovniku neni.
# print(zvire['karticka pojistence'])

# get - ochrana proti KeyError
karticka = zvire.get('karticka pojistence', 'nenalezena')
print(karticka)

if 'potrava' in zvire:
    print(f'Zvire je najedene. Snedlo {zvire["potrava"]}')
else:
    print('Toto zvire nemusi jist. Poznamka: poridit jich vic')