# létrehozok egy szákom nevú listát
# legyen benne 3 szám
szamok = [3 , 5 , 7]
print(szamok)

#adj hozzá két új számot
szamok.append(2)
szamok.append(8)
print(szamok)

#lista végig futása
for i in range(len(szamok)):
      print(szamok[i])

#hány darab páros szám van
db = 0
for i in range(len(szamok)):
    if szamok[i] %2 == 0: 
        db = db + 1 
print("A listában", db, "darab páros szám van.")

#ha a szám kisebb 5-nél, akkor szorozza 2-vel
#egyébként ossza 3-mal
for i in range(len(szamok)):
    if szamok[i] < 5:
        szamok[i] = szamok[i] * 2
    else: szamok[i] = szamok[i] / 3

print(szamok) 