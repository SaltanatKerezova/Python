vysvedceni = {
    'český jazyk': 1,
    'matematika': 2,
    'dějepis': 1
}

#---------------------------------

# Původní slovník prodejů
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

# Přidání nové knihy a aktualizace prodejů existující knihy
sales["Noc, která mě zabila"] = 0
sales["Vrah zavolá v deset"] += 100

# Vypsání upraveného slovníku prodejů
print("Upravený slovník prodejů:")
for kniha, prodeje in sales.items():
    print(f"{kniha}: {prodeje} kusů")
