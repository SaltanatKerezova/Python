venecky = [1, 2, 4, 1, 6, 0, 1]
jmeno = 'Marketa Vaneckova'

print (venecky[1:4:2])
print (jmeno[5:])

print (len(jmeno[5:]))
print (len(jmeno))

print (min(venecky))
print (max(venecky))

serazene = sorted (venecky)
print (serazene)

serazene = sorted (venecky, reverse=True)
print (serazene)

serazene_jmeno = sorted (jmeno)
print(serazene_jmeno)

serazene_jmeno = sorted (jmeno, reverse=True)
print(serazene_jmeno)

tri_nej = serazene_jmeno [:3]
print (tri_nej)

'''----------------------------------'''
venecky = [1, 2, 4, 1, 6, 0, 1]
jmeno = 'Markéta Vašek'

print(min(venecky))
print(max(venecky))

serazene_venecky = sorted(venecky, reverse=True)
print(serazene_venecky)

serazene_jmeno = sorted(jmeno)
print(serazene_jmeno)

# tri nejvetsi cisla ze seznamu
tri_nejvetsi = serazene_venecky[:3]
tri_nejmensi = serazene_venecky[-3:]
print(tri_nejvetsi)
print(tri_nejmensi)

'''----------------------------------'''

email = 'marketa.vasek@seynam.cz'
if 'vasek' in email:
  print('je tam vasek')


