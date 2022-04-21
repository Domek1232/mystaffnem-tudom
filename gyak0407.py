from posixpath import split


class Eredmeny:
    nev: str
    rajtszam: int
    kategoria: str
    ido: str
    tavSzazalek: int
    
    def __init__(self, sor: str) -> None:
        adatok = sor.split(';')
        self.nev = adatok[0]
        self.rajtszam = int(adatok[1])
        self.kategoria = adatok[2]
        self.ido = adatok[3]
        self.tavSzazalek = int(adatok[4])
    def a():
        pass

        
file = open('ub2017egyeni.txt', 'r',encoding='utf-8')

# első sort beolvasom hogy a 2.-ra ugorjon a mutató (az első sor csak fejléc)
file.readline()

osszeseredmeny: list[Eredmeny] = []

for sor in file:
    egyeredmeny = Eredmeny(sor.strip())
    # a létrehozott egyeredmeny hozzáfűzöm a listámhoz.
    osszeseredmeny.append(egyeredmeny)
    
print("A listában", len(osszeseredmeny)," eredmény van.")
noiDb = 0
minSzazalek = 100

#1. Számolja meg és írja ki a képernyőre a minta szerint hogy hány női sportoló teljesítette a teljes távot!
file.seek(0)
file.readline()
for sor in file:
    adatOk = Eredmeny(sor)
    if adatOk.kategoria == "Noi" and adatOk.tavSzazalek == 100:
        noiDb = noiDb + 1
        
print("Ennyi olyan női versenyző volt aki teljesítette a távot: " , noiDb)
        
#2. Kérje be a felhasználótol egy sportoló nevét majd határozza meg és írja ki a minta szerint hogy a sportoló indult-e a versenyen!
# Ha a sportoló indult a versenyen akkor azt is írja ki a képernyőre hogy a teljes távot teljesítette-e!(Feltételezheti hogy nem indultak.
# azonos nevű sportolók ezen a versenyen.)

nevek = input("Adja meg a sportoló nevét:")
bennevan = False
for adatOk in osszeseredmeny:
    if adatOk.nev == nevek:
        bennevan = True
        if adatOk.tavSzazalek == 100:
            print("teljesítette a távot")
        else: 
            print("Nem teljesítette a távot")
        
if bennevan:
    print("szerepel")
else: 
    print("Nem szerepel")
    

#3. Írassa ki az első sportoló idejét órában! Pl 1:30:00 -> 1,5

ido = osszeseredmeny[0].ido.split(":")
oraban = (int(ido[0])*3600 +int(ido[1])*60+int(ido[2])) /3600
print(oraban)

#4. Készítsen egy függvényt (idoOraban.) ami megkapja a versenyző időeredményét majd visszaadja az időt órában! Pl. 1:30:00 -> 1,5
def idoOraban(eredmeny: str) -> float:
    ido = eredmeny.split(":")
    oraban1 = (int(ido[0])*3600 +int(ido[1])*60+int(ido[2])) /3600
    return oraban1
print(idoOraban(osszeseredmeny[0].ido))  

def b():
    pass

#5. Határozza meg és írja ki a minta szerint a teljes távot teljesítő férfi sportolók átlagos idejét órában! Feltételezheti
#hogy legalább egy ilyen sportoló volt(28,347)
fdb = 0
osszes = 0

for adatOk in osszeseredmeny:
    if adatOk.kategoria == "Ferfi" and adatOk.tavSzazalek == 100:
        fdb = fdb + 1
        osszes += idoOraban(adatOk.ido)
print("Ennyi olyan férfi versenyző volt aki teljesítette a távot: " , fdb)
print("Összesen ennyi idő volt:", osszes/fdb)

#zárójeles feladat hány olyan célba érkezet versenyző van akinél se az előte levő se az utaánna levő nem teljesítette a távat 
darab = 0
for i in range(1,len(osszeseredmeny)-1):
    if osszeseredmeny[i].tavSzazalek == 100 and osszeseredmeny[i-1].tavSzazalek < 100 and osszeseredmeny[i+1].tavSzazalek < 100:
        darab += 1

print(darab)
