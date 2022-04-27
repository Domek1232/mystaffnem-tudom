#osztály létrehozása
class Buszjarat:
    ulesszam: str 
    felszalkmszam: str
    meddigmegykm: str
    
    def __init__ (self,sor: str) -> None:
        adatok = sor.split(' ')
        self.ulesszam = adatok[0]
        self.felszalkmszam = adatok[1]
        self.meddigmegykm = adatok[2]
    def a():
            pass

#fájl megynyitása olvasásra

file = open('eladott.txt', 'r',encoding='utf-8')

file.readline()

#objektumlista deklarálása
busz: list[Buszjarat] = []

#fájl  soraniak objektumra alakítása és hozzá fűzése az obj. listához
for sor in file:
    busz.append(Buszjarat(sor))
print(len(busz))    