class Buszjarat:
    buszmeg: int
    kmszalo: int
    marko: int
    
    def __init__(self,sor:int)-> None:
        adatok = sor.split(' ')
        self.buszmeg = int(adatok[0])
        self.kmszalo = int(adatok[1])
        self.marko = int(adatok[2])
    def a():
            pass
    
        
file = open('eladott.txt', 'r',encoding = 'utf-8')
file.readline()
busz: list[Buszjarat]= []
for sor in file:
    busz.append(Buszjarat(sor))
print(len(busz))