import json
to_json = {}

with open('alice.txt', encoding='utf-8') as file:  # Napiš skript v Pythonu, který otevře soubor alice.txt
    text = file.read()

#print(text)

for character in text.lower():  #velká písmena převeď za malá
    if not character.isspace(): #ignoruj mezery a znaky nového řádku (ostatní znaky jako čárky nebo závorky zařaď do výsledku)
        if character in to_json:
            to_json[character] +=1  #spočítá četnost (počet výskytů) všech znaků
        else:
            to_json[character]=1

with open('ukol1_output.json', mode = "w", encoding='utf-8') as  output_file:  #obsahuje slovník, kde klíče jsou znaky a hodnoty jejich četnost
    json.dump(to_json, output_file, ensure_ascii=False, indent = 4, sort_keys=True)  #volitelně: slovník je seřazen podle klíčů, sort_keys zapisuje alphabeticky.
