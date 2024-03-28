#flight_number = input('zadej cislo letu [napr: BA345]:')

flight_number = 'BA345'
prefix = flight_number[0] + flight_number[1]
prefix = flight_number[:2]

print(prefix)

#---------------------------------------------

guest_list = ['Jirka','Klara','Natalie']
jmeno = input('zadej jmeno: ')
if jmeno [0] == 'K':   #the same in other code: jmeno.startswith('K')
 guest_list.append(jmeno)

print(guest_list)


# sekvence - neboli "iterable"
# "procházenímožné" "dá se procházet"

guest_list = ["Jirka", "Klára", "Natálie"]

name = input('zadej jmeno na poslední chvíli: ')
if name[0] == 'K':
    # přidáme někoho s 'K' na začátku
    guest_list.append(name)

print(guest_list)

# kontorlujeme hosty
guest = input('Zadej příchozího: ')
if guest in guest_list:
    print("Buď vítán(a)!")
else:
    print("Bohužel nejsi na seznamu.")


#------------------------------------------
school_marks = [
    ["Jiří", 1, 4, 3, 2],
    ["Natálie", 2, 3, 4, 3],
    ["Tereza", 1, 1, 2, 1],
]

names_only = []
for row in school_marks:
    name = row[0]
    names_only.append(name)

print(names_only)

