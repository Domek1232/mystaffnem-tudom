class Labdarugas:
    fordulo: int
    hazaigol: int
    vendeggol: int
    hazaifelido: int
    vendegfelido: int
    hazaics: str
    vendegcs: str
    
    def meccs (self,sor: str) -> None:
        adatok = sor.split(' ')
        self.fordulo = int(adatok[0])
        self.hazaigol = int(adatok[1])
        self.vendeggol = int(adatok[2])
        self.hazaifelido = int(adatok[3])
        self.vendegfelido = int(adatok[4])
        self.hazaics = int(adatok[5])
        self.vendegcs = int(adatok[6])
        def a():
            pass

        
file = open('meccs.txt', 'r',encoding='utf-8')

file.readline()

osszes: list[Labdarugas] = []

    
for e in osszes:
    osszes.append(Labdarugas(e))
    # a létrehozott egyeredmeny hozzáfűzöm a listámhoz.
print(len(osszes))

#Kérj be a felhasználótól egy forduló számát, majd írja a képernyőre a bekért forduló mérkőzéseinek adatait a következő formában:
#Edes-Savanyu: 2-0 (1-0) ! Soronként egy mérkőzést tüntessen fel! A különböző sorokban a csapatnevek ugyanazon a pozíción kezdődjenek!

fordu = input("Adja meg a forduló számát:")
for e in osszes:
    if fordu in e.fordulo:
        print(osszes)