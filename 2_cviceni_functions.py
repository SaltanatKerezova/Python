# Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.

def two_numbers(a, b):
    return a * b

returned_value = two_numbers(5, 3)
print(returned_value)    

""" Převod kilometrů na míle a zpět

Napište dvě funkce: kilometry_na_mile(kilometry) a mily_na_kilometry(mile), 
které provedou převod mezi kilometry a mílemi."""

def kilometry_na_mile(kilometry):
    """Převede kilometry na míle."""
    mile = kilometry * 0.621371
    return mile

def mile_na_kilometry(mile):
    """Převede míle na kilometry."""
    kilometry = mile / 0.621371
    return kilometry

# Příklad použití funkcí:
kilometry = 10
mile = kilometry_na_mile(kilometry)
print(f"{kilometry} kilometrů je {mile} mil.")

mile = 6.21
kilometry = mile_na_kilometry(mile)
print(f"{mile} mil je {kilometry} kilometrů.")


#Převod metrů na stopy a zpět které umožňují převod mezi metry a stopami.

def metry_na_stopy(metry):
    stopy = metry * 3.280839895
    return stopy


def stopy_na_metry(stopy):
    metry = stopy / 3.280839895
    return metry

metry = 15
stopy = metry_na_stopy(metry)
print(f"{metry} metru je {stopy} stopy")

stopy = 6.21
metry = stopy_na_metry(stopy)
print(f"{stopy} stopy je {metry} metrů.")



# Převod centimetrů na palce a zpět

Vytvořte dvě funkce: centimetry_na_palec(centimetry) a palce_na_centimetry(palce), 
které umožní převod mezi centimetry a palci.


def centimetry_na_palec(centimetry):
    palce = centimetry * 2.54
    return palce

def palce_na_centimetry(palce):
    centimetry = palce / 2.54
    return centimetry

centimetry = 67
palce = centimetry_na_palec(centimetry)
print (f"{centimetry} centimetry je {palce} palce.")


palce = 80
centimetry = palce_na_centimetry(palce)
print (f"{palce} palce je {centimetry} centimetry.")


"""Převod hmotnosti kilogramů na libry a zpět

Napište funkce: kilogramy_na_libry(kilogramy) a libry_na_kilogramy(libry), 
které provedou převod mezi kilogramy a librami.

Převod objemu litrů na galony a zpět

Vytvořte dvě funkce: litry_na_galony(litry) a galony_na_litry(galony), 
které umožní převod mezi litry a galony.

Převod rychlosti kilometrů za hodinu na míle za hodinu a zpět

Napište funkce: kmh_na_mph(kmh) a mph_na_kmh(mph), které umožní převod 
rychlosti mezi kilometry za hodinu a míli za hodinu.

Převod teploty ze stupňů Celsia na Fahrenheit a zpět

Vytvořte dvě funkce: celsia_na_fahrenheit(teplota) a fahrenheit_na_celsia(teplota), 
které umožňují převod teploty mezi stupni Celsia a stupni Fahrenheit 



Napiš funkci month_of_birth, která bude mít jeden parametr - rodné číslo.
Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup.
Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.


#------------------

Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.
"""

def month_of_birth(rodne_cislo):
    if len(rodne_cislo) < 10:
        return 'Nespravne zadani'
    mesic_text = rodne_cislo[2:4]
    mesic = int(mesic_text)
    if mesic > 50:
        mesic = mesic - 50
    return mesic

print(month_of_birth('1234'))
print(month_of_birth('9207054439'))
print(month_of_birth('9555125899'))

# vnitrni print zobrazi "ahoj" a "vratí" None
# vnejsi print zobrazi to, co vratil vnitrni - "None"

print(print('ahoj'))