print ('hello world')
pocet_jablek = 10  #int
teplota = 37.8  #float, decimal
jmeno = 'Kuba'  #string

pravda = True #boolean
lez = False #boolean

zbozi = ['hrnek',     #list, array- seznam
         'sklenicka',
         300,
         'konvice',
         'talir',
         ]

#VARIANTA 1___________________

PRICE_PER_TICKET = 250 #definuj si konstatu

number_of_tickets = int(input('zadej pocet listku: '))
total_price = number_of_tickets * PRICE_PER_TICKET

if total_price >= 500:
    total_price = total_price * 0.9

if 1==1:
    print ('pravda')    

print(f'Tady mas {number_of_tickets}, bude te to stat {total_price}Kc')
#print (total_price)

#prevod z dvojkove soustavy
#text = '35455'
#cislo = int(text, 2)
#print (text,cislo)

#VARIANTA 2___________________

PRICE_PER_TICKET = 250  # definuji si "konstantu"
DISCOUNT_AMT = 0.1
DISCOUNT_THRESH = 500

number_of_tickets = int(input('Zadej počet lístků: '))
total_price = number_of_tickets * PRICE_PER_TICKET

if total_price >= DISCOUNT_THRESH:
    total_price = total_price * (1 - DISCOUNT_AMT)

print(f'Tady máš {number_of_tickets} lístků, bude tě to stát {total_price}Kč')

#__________________
age = int(input("Jaký je Váš věk? "))

if age < 13:
    print("Představení je bohužel přístupné až od 13 let.")
    exit()

number_of_tickets = int(input("Kolik si přejete lístků? "))
price_per_ticket = 190
total_price = number_of_tickets * price_per_ticket
if total_price >= 1500:
    discount = 0.2
    total_price = total_price * (1 - discount)
    print(f"Získáváte slevu {discount * 100}.")
elif total_price >= 500:
    discount = 0.1
    total_price = total_price * (1 - discount)
    print(f"Získáváte slevu {discount * 100}.")
else:
    to_discount = total_price - 500
    print(f"Nakupjte ještě za {to_discount} Kč a získáte slevu 10 %!")

print(f"Celková cena nákupu je {total_price} Kč.")