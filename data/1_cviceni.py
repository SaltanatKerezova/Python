#CVICENI 1

cislo = 100
print(cislo)
cislo = cislo + 1  # Sem přidej kód, který proměnnou cislo zvýší o 1
print(cislo)  # Vypíše 101

#CVICENI 2 Varianta 1--------------------------

cislo = 150  # Ulož do proměnné cislo vstup od uživatele
print(cislo)  # Zopakuje zadanou hodnotu
cislo = cislo + 1  # Sem přidej kód, který proměnnou cislo zvýší o 1
print(cislo)  # Vypíše cislo zvětšené o 1

#CVICENI 2 Varianta 2--------------------------


cislo = input("Zadej cislo: ")  # Ulož do proměnné cislo vstup od uživatele
print(cislo)  # Zopakuje zadanou hodnotu
cislo = int(cislo) + 1  # Zvýší proměnnou cislo o 1
print(cislo)  # Vypíše cislo zvětšené o 1

#CVICENI 3------------------------


Fahrenheit_1 = float( input("Temperature value in degree Fahrenheit: " ))
# For Converting the temperature from degree Fahrenheit to degree Celsius.
# by using the above given formula.
celsius_1 = (Fahrenheit_1 - 32) * 5/9
# Print the result.
print(f'Temperature value in degree celsius: {round(celsius_1)}')