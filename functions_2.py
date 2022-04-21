#   Függvény: Névvel elátott, adott feladatott elvégző utasítások sorozata.
#   A függvényt használat előtt definiálni kell.
#   Formája:
#   1.Függvény fej leírása:
#   ======================
#   def függvény_neve(formális paraméterlista) -> függvény_visszatérési_értékének_a_típusa:
#   2: Függvény törzs leírása:
#   ======================
#   tetszőleg számú utasítás

from xmlrpc.client import boolean


def összead(a: int , b: int) -> int:  #a függvény feje
    # def => függvény definiciót bevezető kulcsszó
    # összead => a függvény azonosítója (neve)
    # () => operátorok a paraméterek megadására
    # a: int, b: int => függvény formális paraméterei azonosítóval és típussal (típus opcio)
    # -> => függvény visszatérési értékét ezután az "operátor" után adhatjuk meg (opcionális)
    # int => a függvény visszatérési értékének a típusa
    
    return a + b #függvény törzse

    
# A függvény hívása 
# A hívás szintaxisa:
# függvény azonosítója(aktuális paraméterlista)
összead(3, 4) # A függvény visszatérési értéke így elveszik
print(összead(3, 4)) # A függvény visszatérési értékét a képernyőre írjuk
összeg: int = összead(3, 4) # A függvény visszatérési értékét eltároljuk
print(összeg)

#Feladat: Készítsünk függvényt ami vissza adja két szám legnagyobb közös oszóját
def lnko(a, b):  
    if (b == 0):  
        return a  
    else:  
        return lnko (b, a % b)  
a =int (input ("Add meg az első számot: "))   
b =int (input ("Add meg a második számot: "))    
num = lnko(a, b)   
print("Lnko a kettő számnak a: ")  
print(num)  

#Feladat: írj egy logikai értékkel visszatérő python függvényt, amely
#paraméterenként kap egy egész számot, és eldönti,
#hogy osztható-e 2-vel és 3-al is egyszere
def oszthatoe(a: int) -> boolean:
    if (a % 2 == 0 and a % 3 == 0):
        return True
    else:
        return False
print(oszthatoe(a))