konicky = ["Python", "kung-fu", "Python", "Python", "SQL", "Netflix"]
konicky = set(konicky)
print(konicky)

#---------------------------------

konicky_pavel = {"Python", "kung-fu", "Python"}
konicky_alena = {"Python", "běhání"}
zajmy_obou = konicky_pavel | konicky_alena
spolecne_zajmy = konicky_pavel & konicky_alena
print(zajmy_obou)
print(spolecne_zajmy)