class NobelDijasok:
    ev: int
    nev: str
    szuletes: str
    orszag: str
    szulhal: str
    
    def __init__(self,sor: str) -> None:
        adatok = sor.split(';')
        self.ev = int(adatok[0])
        self.nev =adatok[1]
        self.szuletes = adatok[2]
        self.orszag = adatok[3]
                                   


orvosi = open('orvosi_nobeldijak.txt', 'r',encoding='utf-8')

#üres objektumlista létrehozása
# ez egy olyan lista. ami sok NobelDijasok típusú objektumot tartalmaz.

osszesNobelDijas: list[NobelDijasok] = []

orvosi.readline()
for sor in orvosi:
    egyember = NobelDijasok(sor.strip())
    osszesNobelDijas.append(egyember)
print(osszesNobelDijas[10].nev)

for egy in osszesNobelDijas:
    print(egy.ev)

for i in range(len(osszesNobelDijas)):
    print(osszesNobelDijas[1].nev)
    