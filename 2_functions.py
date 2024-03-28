def greet_teacher():
 print("Ahoj!")

def greet_user(name, title):                    # greet_user = f"Ahoj{title} {name}!"
    print(f"Ahoj {title} {name}!")              # return greet_user


greet_user("Jirko","Dr. ")

def sum_two_numbers (a,b): 
   vysledek = a+b
   return vysledek

c = sum_two_numbers (2,5)
print(c) 


# -------------------------------

def get_mark(points):
    if points <= 60:
        mark = 5
    elif points <= 70:
        mark = 4
    elif points <= 80:
        mark = 3
    elif points <= 90:
        mark = 2
    else:
        mark = 1
    return mark

points = int(input("Zadej počet bodů v testu: "))
mark = get_mark(points)
if mark == 5:
    points = int(input("Zadej počet bodů v opravném pokusu: "))
    mark = get_mark(points)
print(f"Výsledná známka je {mark}.")


# -------------------------------

def compose_greeting_dr(jmeno, titul='Dr.'):
    """Vytvoří pozdrav
    
    pokud není zadaný titul, použije se "Dr."
    """
    pozdrav = f'ahoj {titul} {jmeno}'
    return pozdrav


print(compose_greeting_dr('Kuba'))
print(compose_greeting_dr('Markéta', 'CSc.'))

# -------------------------------

def compose_greeting_dr(jmeno, titul=None):
    """Vytvoří pozdrav
    
    pokud není zadaný titul, použije se "Dr."
    """
    if titul == None:
        pozdrav = f'ahoj {jmeno}'
    else:
        pozdrav = f'ahoj {titul} {jmeno}'
    return pozdrav


print(compose_greeting_dr('Kuba'))
print(compose_greeting_dr('Markéta', 'CSc.'))


