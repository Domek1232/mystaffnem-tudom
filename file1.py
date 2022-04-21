#sorok nevű lista deklarálás
sorok = []

# file nevű, fájl tipusú változó létrehozása olvasásra
#with open('forras.txt','r',encoding='utf-8') as file:
file = open('forras.txt','r',encoding='utf-8')

#for ciklussal végigmegy a sorokon
# a ciklusban minden sort hozzáfűzök a listához
for e in file:
    sorok.append(e.strip())
    
print(sorok)

#írj egy forrás file-t a txt-ben ahol 3-om ember teljes neve található 1feladat olvasukk be 3db változóba
f1 = open('nevek.txt','r',encoding='utf-8')
nev1 = f1.readline().strip()
print(nev1)
nev2 = f1.readline().strip()
print(nev2)
nev3 = f1.readline().strip()
print(nev3)
#hozzunk létre egy txt-t aminek az a neve szamok és legyen egymás allat számok olvassuk be egy szamok nevű listába
szamok = []
f2 = open('szamok.txt','r',encoding='utf-8')
for sz in f2:
    szamok.append (int (sz.strip()))
    
print(szamok)