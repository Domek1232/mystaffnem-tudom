#Hozz létre egy Auto osztályt Tulajdonságai: márka,évjárat,szín,hengerűrtartalom   
#Metódusai: (konstruktor),dudál
class Auto:
    marka: str
    tipus: str
    evjarat: int
    szin: str
    hengerurtartalom: int

    def __init__(self, mark: str, tip: str, evjar: int, szine: str, hengeru: int) -> None:
        self.marka = mark
        self.tipus = tip
        self.evjarat = evjar
        self.szin = szine
        self.hengerurtartalom = hengeru

    def duda(self):
        print("bing csiling")

enKocsim = Auto("VolsWagen", "Golf mk6 r" ,2016,"fekete",2500)
print("Auto márkája:" ,enKocsim.marka)
print("Auto típusa:" ,enKocsim.tipus)
print("Évjárata: ",enKocsim.evjarat)
print("Színe",enKocsim.szin)
print("hengerűrtartalma", enKocsim.hengerurtartalom)
enKocsim.duda()
