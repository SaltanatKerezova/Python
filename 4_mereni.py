with open ("data/mereni.txt", encoding="utf-8") as file:
    text = file.read()
print('Text')
print(text)

lines = []

with open('data/mereni.txt', encoding='utf-8') as file:
    for line in file:
        lines.append(line)

print('lines')
print(lines)


hours = []
with open("data/vykaz.txt", encoding="utf-8") as file:
    for line in file:
        hour = int(line)
        hours.append(hour)

hour_rate = int(input("Zadej hodinovou mzdu: "))
total_salary = hour_rate * sum(hours)
print(total_salary)
print(total_salary/len(hours))



rows_words = []
with open("data/praha.txt", encoding="utf-8") as file:
    for line in file:
        words = line.split()
        words_count = len(words)
        print(words_count)
        rows_words.append(words_count)
print(sum(rows_words))

#---------------------------------

total_distance = 0
with open("data/auta.txt", encoding="utf-8") as file:
    for line in file:
        if len(line.strip()) > 0:
            _, km = line.split()
            km = km.replace(",", ".")
            km = float(km)
            total_distance += km
print(total_distance)


