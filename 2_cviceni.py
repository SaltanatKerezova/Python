import statistics
"""Mějme seznam pohybů na nějakém bankovním účtu:

pohyby = [1200, -250, -800, 540, 721, -613, -222]
Vypište v pořadí třetí pohyb z uvedeného seznamu.
Vypište všechny pohyby kromě prvních dvou.
Vypište kolik je všech pohybů dohromady.
Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný."""

pohyby = [1200, -250, -800, 540, 721, -613, -222]
print(pohyby[2:]) #Vypište všechny pohyby kromě prvních dvou.
print(sum(pohyby))  #Vypište kolik je všech pohybů dohromady.
print(min(pohyby))   #Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb
print(max(pohyby))   #Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
print(sum(pohyby))   #Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný. """


"""Mějme proměnnou s, ve které předpokládáme uložený nějaký seznam. 
Sestavte v výraz (vzoreček), který spočítá průměrnou hodnotu v takovém 
seznamu. Otestujte jej na seznamech různých délek."""

s = [1,2,3,4,20]
print (statistics.mean(s))

#Postupujte obdobně jako v úložce Průměr, ale tentokrát 
#sestavte výraz pro výpočet rozpětí, tedy rozdílu mezi minimální a maximální hodnotou.


#Uložte si do proměnné jmeno svoje jméno. Pomocí volání vhodných metod jej převeďte 
#nejdříve na malá písmena a poté na velká písmena.

jmeno = 'Salta'
print(jmeno.upper())
print(jmeno.lower())

