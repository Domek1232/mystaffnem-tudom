class Buszjarat:
    vegall: int
    buszmeg: int
    jani : int
    
    def __init__(self,sor:str)-> None:
        adatok = sor.split(' ')
        self.vegall = int(adatok[0])
        self.buszmeg = int(adatok[1])
        self.jani = int(adatok[2])
        
file = open('eladott.txt','r', encoding = 'utf-8')
file.readline()
busz:list[Buszjarat] = []
for sor in file:
    busz.append(Buszjarat(sor))
print(len(busz))