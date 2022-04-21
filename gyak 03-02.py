#kérjünk be a felhasználótol két sringet de nevezhetjük mondatnak
mondat = input("Adj meg egy tetszőleges mondatott:")
mondat2 = input("Adj meg még egy tetszőleges mondatot:")
#melyik mondat hosszabb
if mondat > mondat2:
    print("A", mondat ,"nagyobb ,mint" ,mondat2)
else: print("A",mondat2 ,"nagyobb ,mint a",mondat)

#igaz-e hogy mind két mondat pontra végződik
if mondat.endswith(".") and mondat2.endswith("."):
    print("Mind a két mondat pontra végződik")
else:
    print("Egyik mondat sem végződik pontra")
#igaz-e hogy mindkét mondat nagybetővel kezdődik

#feladat2
szoveg = "A számítógép-programozás (vagy egyszerűen programozás) egy vagy több absztrakt algoritmus megvalósítását jelenti egy bizonyos programozási nyelven."
#1.Hányadk karakter a kötőjel?(a szóköz is karakter)
print(szoveg.find("-"))
#2.A szöveg első karaktere betű?
print(szoveg.isalpha()[0])
#3.Darabold fel a szöveget szóközök mentén a szvak nevű változóba!
szavak = szoveg.split(" ")
print(szavak)
#4.Vágd le a felesleges szóközöket a szöveg végéről.
print(szoveg.rstrip())
#5.Fűzd hozzá metódussal a következő szöveget: "(Wikipedia)"

#szorgalmi: Határozd meg 1 utasítással, milyen karakter áll a kötőjel előtt?
print(szoveg(szoveg.find("-")-1))

#Feladat3
#Írjunk egy függvényt paraméterként kap egy számot random le generál egy annyi számból álló listát és ki írja.
import random

def randomszamok (a: int):
