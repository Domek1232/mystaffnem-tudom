#Random szám Importálása
import random

print('Súgok:', gondolt_szam)
tipp = input('Gondoltam egy számra. Tippeld meg!')

#Randomszám
import random
randomszam = int(random.randint(1, 10))
print(randomszam)
print("gondoltam egy számra 1 és 10 között")
print("Tippeld meg a számot")
tipp = 0
while tipp != randomszam:
    tipp = int(input("Szám:"))
    print("Próbáld meg újra, téves")
print("Szép volt, eltaláltad!")




