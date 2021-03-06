#Az elejére másold be a kapott kódot, így egy kész osztállyal rendelkezel, nem neked kell létrehozni.

# OSZTÁLY:

class Haromszog:
    a: int
    b: int
    c: int
    
    # konstruktor
    def __init__(self, sorom) -> None:
        self.a = int(sorom[0])
        self.b = int(sorom[1])
        self.c = int(sorom[2])    
        
    # osztály metódusa: szöveggel visszatérve megmondja, hogy a számok háromszöget alkotnak-e    
    def haromszoge(self) -> str:
        if self.a < self.b+self.c and self.b < self.a+self.c and self.c < self.a + self.b:
            return "Háromszöget alkotnak"
        else:
            return "Nem alkotnak háromszöget."
    
    def vaneo(self,keresett):
        return self.a == int(keresett) or self.b == int(keresett) or self.c == int(keresett)
        
    def derekszogue(self)-> bool:
        return self.a*self.a + self.b*self.b == self.c*self.c
        
    # osztály metódusa: egész számként visszaadja a háromszög kerületét
    def kerulet(self)-> int            :
        return self.a + self.b + self.c
    def t():
            pass

#Majd hozz létre egy file változót, amiben a haromszogek.txt állományt nyitod meg olvasásra. 
#Az állomány soraiban egy-egy háromszög 3 oldalának lehetséges hossza található. 
#A számok nem mindegyike alkot háromszöget.

#File beolvasása    
file = open('haromszog.txt', 'r',encoding='utf-8')

# lista létrehozása a sorok számára
lista = []

# első sor beolvasása (fejléc, nem csinálunk vele semmit)
file.readline()

#A fájl sorait olvasd be 2D lista adatszerkezetbe.
#fájl sorainak bejárása 
for sor in file:
     #listához hozzáfűzöm
    lista.append(sor.strip().split("*"))
print(lista) 

#A lista minden eleméből példányosíts egy egyHaromszog nevű, Haromszog típusú objektumot.
for it in lista:
    print(it)
    egyHaromszog = Haromszog(it)  
    
#Az osztálynak már vannak kész metódusai. 
#A haromszoge() metódus segítségével írasd ki listasoronként, hogy háromszöget alkotnak-e a számok.
    print(egyHaromszog.haromszoge())
    
#A kerulet() metódus segítségével írasd ki az egyes háromszögek kerületét.
    print("A háromszög kerülete:" ,egyHaromszog.kerulet())

#1. Feladat Kérj be a felhasználótól 3 számot (megfelelő adatszerkezetben), majd írd ki neki,hogy háromszöget alkotnak-e!
#EGYIK MEGOLDÁS
bekertSzamok = []
for i in range(3):
    szam: int = int(input("Add meg a háromszög oldalát:"))
    bekertSzamok.append(szam)
    
egyHaromszog = Haromszog(bekertSzamok)
print(egyHaromszog.haromszoge())

#3. Feladat Írj egy új osztály metódust,amelyik logikai értékként megadja, hogy szerepel-e benne 
# egy paraméterént megadott szám (ezt a felhasználótól kérd be)!
keresett: int = int(input("Add meg a keresett számot:"))
print(egyHaromszog.vaneo(keresett))