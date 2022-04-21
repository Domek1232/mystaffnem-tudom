class Kutya:
    nev: str
    fajta: str
    szulido: int

    def __init__(self,neve: str, fajtaja: str,szulideje: int) -> None:
        self.nev = neve
        self.fajta = fajtaja
        self.szulido = szulideje
    
    def ugat(self):
        print("Vau vau...")

# Kutya osztályú objektumok létrehozása (példányosítás) -> 1 konkrét kutya
enKutyam = Kutya("Bodri","puli",2020)
print("Kutyám neve:" ,enKutyam.nev)
print("Kora: ",2022-enKutyam.szulido)

tekutyad = Kutya("Zeusz","német juhász",2020)
print("A te kutyád",tekutyad.nev,", fajtája",tekutyad.fajta,"és születési éve", tekutyad.szulido)
enKutyam.ugat()