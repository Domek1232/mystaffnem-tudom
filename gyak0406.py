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
                                      
# Hány Nobel díjas van?
orvosi.readline()
osszesen = 0
for sor in orvosi:
    osszesen += 1
    
print("A fájlban", osszesen,"sor van.")

# Hány magyar Nobel díjas van?
orvosi.seek(0)
orvosi.readline()

magyarok = 0
for sor in orvosi:
    egyember = NobelDijasok(sor.strip())
    if (egyember.orszag == "H"):
        magyarok = magyarok + 1
        
print("A fájlban",magyarok,"magyar díjazott van.")

# Mikor kapták az első Nobel díjat?
orvosi.seek(0)
orvosi.readline()
elsoNobeldij = 2022
for sor in orvosi:
    egyember = NobelDijasok(sor.strip())
    if (egyember.ev < elsoNobeldij):
        elsoNobeldij = egyember.ev

print("Az első orvosi Nóbel díj", elsoNobeldij,"-ban/ben adták ki.")
# Szerepel-e a listában Archibald nevű ember?
orvosi.seek(0)
orvosi.readline()
szerepel = False
for sor in orvosi:
    egyember = NobelDijasok(sor.strip())
    if ("Archibald" in egyember.nev):
        szerepel = True
if (szerepel):
    print("Szerepel a listában Archibald nevű díjazott.")
else:
    print("Nem szerepel a listában Archibald nevű díjazott.")
# Írasd ki soronként, hogy hány éves korában halt meg a díjazott.(ha még él ,ne írja ki.)
orvosi.seek(0)
orvosi.readline()
for so in orvosi:
    egyember = NobelDijasok(sor.strip())
    evek = egyember.szuletes.split("-")
    if(evek[1] != ""):
        print(egyember.nev,": ", int(evek[1])-int(evek[0]))