#ellenorzo input: Kérjünk be a felhasználótól egy számot.
#Amíg 1 és 20 közötti párosat nem ad meg.
import random

egyeshusz = random.randint(1,10)
#Első tartomány bekérése a felhasználótól.
a = num = int(input('Add meg a tartományt alsó határát: '))
#Második tartomány bekérése a felhasználótól.
b = num = int(input('Add meg a tartomány felső határát: '))
gondoltSzam = random.randint(a,b)
num = int(input("Írd be a számot: "))
while tipp != gondoltSzam:
    tipp = int(input('Nem talált, próbáld újra: '))
gondoltSzam = num % 2
if gondoltSzam > 0:
    print("Ez egy paratlan szam.")
else:
    print("Ez egy paros szam.")