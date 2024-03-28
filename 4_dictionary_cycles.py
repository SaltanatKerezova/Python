sales = {
    "Zkus mě chytit"     : 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh"      : 2565,
}

# funguje, ale neni idealni
for key in sales:
    print(f'Knihy {key} se prodalo {sales[key]}')

# tohle je mnohem lepsi, rychlejsi, pouziva se nejcasteji
for name, amount in sales.items():
    print(f'Knihy {name} se prodalo {amount}')

# prochazi jen hodnoty
for amount in sales.values():
    print(amount)

# prochazi jen klice
for key in sales:
    print(key)

# prochazi jen klice   
for key in sales.keys(): 
    print(key)    
   

# shrnuti
# slovnik          -> jen klice
# slovnik.keys()   -> jen klice (ale rikam to naprimo)
# slovnik.values() -> jen hodnoty
# slovnik.items()  -> klic i hodnota - super, pozivat


# chceme celkovy prodej
total_sales = 0
for name, amount in sales.items():
    total_sales += amount
print(total_sales)

# nebo :-)

print(sum(sales.values()))


#---------------------------------

books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

# celkem kusu
total_sales = 0
for book in books:
    total_sales += book['sold']

print(total_sales)

# prvni pismena nazvu
for book in books:
    title = book['title']
    first_letter = title[0]
    print(first_letter)

# celkem vydelek v roce 2019
cash = 0
for book in books:
    if book['year'] == 2019:
        amount = book['price'] * book['sold']
        cash += amount
print(cash)