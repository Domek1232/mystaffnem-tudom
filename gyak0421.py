class Labdarugas:
    fordulo: int
    hazaigol: int
    vendeggol: int
    hazaifelido: int
    vendegfelido: int
    hazaics: str
    vendegcs: str
    
    def __init__ (self,sor: str) -> None:
        adatok = sor.split(' ')
        self.fordulo = int(adatok[0])
        self.hazaigol = int(adatok[1])
        self.vendeggol = int(adatok[2])
        self.hazaifelido = int(adatok[3])
        self.vendegfelido = int(adatok[4])
        self.hazaics = adatok[5]
        self.vendegcs = adatok[6]
        def a():
            pass

def forditottake(a: int, b: int, c: int, d:int) -> bool:
    return (c > d and b > a) or (d > c and a > b)
    def b():
        pass

        
file = open('meccs.txt', 'r',encoding='utf-8')

file.readline()

osszes: list[Labdarugas] = []

    
for sor in file:
    osszes.append(Labdarugas(sor))
    # a létrehozott egyeredmeny hozzáfűzöm a listámhoz.
print(len(osszes))

#1.) kérj be a felhasználótól egy forduló számát, majd írja a képernyőre a bekért forduló mérkőzéseinek adatait a következő formában:
#Edes-Savanyu: 2-0 (1-0) ! Soronként egy mérkőzést tüntessen fel! A különböző sorokban a csapatnevek ugyanazon a pozíción kezdődjenek!

fordu = input("Adja meg a forduló számát:")
for e in osszes:
    if int(fordu) == e.fordulo:
        print(e.hazaics)
        
# 2.) kérjünk be a felhasználótól egy csapat nevet és válaszolj hogy van-e ilyen csapat
csapat = input("Add meg a csapat nevét:")
szerepel = False
for e in osszes:
    if csapat == e.hazaics or csapat == e.vendegcs:
        szerepel = True

if (szerepel):
    print("Szerepel a listában az a csapat amit megadott.")
else:
    print("Nem szerepel a listában az a csapat amit megadott.")
    
# 3.) Határozza meg, hogy a bajnokság során mely csapatoknak sikerült megfordítaniuk az állást
# Ez azt jelenti, hogy a csapat az első félidőben 

print("A következő csapatok fordítottak:")
for e 

        
# 4.)hány gólt löttek a Nyulak vendeg pályán
nyulakgol = 0 

for e in osszes:
    if e.vendegcs.strip() == "Nyulak":
        nyulakgol += e.vendeggol
        
print("A Nyulak ennyi golt lőtek:" , nyulakgol)    