import random

# 1. FELADAT: Hozz létre egy listát, benne 3 számot.
szamok = [3 , 5 , 7]
print(szamok)

# 2. FELADAT: FOR ciklus 10-szer fut
for i in range(10):
# 3. FELADAT: random generálaás
    szamok2 = random.randint(1,10)
    print(szamok2)
# 4. FELADAT: számok hozzáadása listához
    szamok.append(szamok2)
print(szamok)

# 5. FELADAT: kérjünk be egy tetszőleges számot
a = int(input("Adj meg egy tetszőleges számot:")) 
print(a)

# 6. FELADAT: ha nincs a listában, adjuk hozzá az első helyre
if a in szamok:
    print("Benne van a listában a szám")
else: 
    szamok.insert(0, a)  
print(szamok)

# 7. FELADAT: Az első elemet szorozzuk 2-vel.
print("Ell.:",szamok[0])
for i in range (len(szamok)):
    szamok[0] = szamok[0] * 2
    print(szamok)

# 8. FELADAT: A második elemet távolítsuk el
szamok.pop(1)
print(szamok)

#9. FELADAT: rendezzük növekvőbe a listát
szamok.sort()
print(szamok)

# 10. FELADAT: rendezzük csökkenőbe a listát
szamok.sort(reverse=True)
print(szamok)

# 11. FELADAT: adjuk össze a lista elemeit
ba = 0
for i in range(len(szamok)):
      ba = ba + szamok[i]
print("A számok összege:", ba)