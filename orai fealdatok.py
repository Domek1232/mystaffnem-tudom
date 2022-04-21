# 1.feladat:
#Kérjen be a program 2 számot, és írja ki, hogy melyik nagyobb, melyik kisebb. Azt is írja ki, ha egyenlőek.
#Számok bekérése
u = int(input("Adjon meg egy tetszőleges számot:"))
k = int(input("Adjon meg mégegy tetszőleges számot:"))
if u<k:
    print("A nagyobb szám:", k,)
if u>k:
    print("A nagyobb szám:", u,)
if u == k:
    print("A két szám egyenlő")

# 2. feladat:
# Kérd be egy háromszög oldalait, majd határozd meg és írd ki, hogy a háromszög megszerkeszthető-e! 
# (A háromszög akkor megszerkeszthető, ha bármely két oldalának az összege nagyobb mint a harmadik oldal.)
f: int =(input('f = '))
g: int =(input('g = '))
h: int =(input('h = '))
#A háromszög megszerkeszthető-e!
if f<g+h and g<f+h and h<f+g:
    print("Háromszög megszerkeszthető")
else: print("Háröszög nem megszerkeszthető")

#3. feladat:
# Kérd be egy háromszög oldalait, majd számold ki a kerületét, és az alábbi képlettel a területét is:
#Oldalak bekérése
a = int(input("Add meg a háromszög 'a' oldalát:"))
b = int(input("Add meg a háromszög 'b' oldalát:"))
c = int(input("Add meg a háromszög 'c' oldalát:"))


#4. feladat:
# Kérd be egy téglalap oldalait és tárolja őket VALÓS típusú változókba, majd határozd meg, 
# a téglalap területét és kerületét!
#Téglalap oldalai
d = float(input("Add meg a téglalap 'd' oldalát:"))
e = float(input("Add meg a téglalap 'e' oldalát:"))
#Terület
T = d * e
#Kerület
K = 2 * (d + e)
print("A téglalap területe", T ,"cm")
print("A téglalap kerülete", K, "cm²")

# Kérjen be a program 2 számot, és írja ki, hogy melyik nagyobb, melyik kisebb. Azt is írja ki, ha egyenlőek.
# Oljuk meg a MIN,MAX függvénnyel.
if a == b:
    print("A két szám egyenlő.")
else:
    print("A nagyobb szám", max(a,b), ", a kisebb", min(a,b),",")
    
                                                #---->Közép szintű feladatok<----

#1. Feladat

#Tölts fel egy listát 10 darab kétjegyű egész számmal! A lista elemeit írd a képernyőre.

import random 

lista = []
for i in range(10):
    lista.append(random.randint(10,99))
    print(lista[i])      
       
#Készíts egy függvényt prime néven, ami eldönti egy számról, hogy prímszám-e. 
#(Egy szám akkor prím, ha pontosan 2 osztója van.)

from xmlrpc.client import boolean

def prime(szam: int) -> boolean:
    osztok = 0
    for i in range(szam): 
        if szam %(i+1) == 0:
            osztok = osztok +1
    return osztok == 2  

#eldönti hogy a listába található-e prím szám
#verzion1
vanebenneprim = False
for i in range(10):
    if (prime(lista[i])):
        vanebenneprim = True    

if vanebenneprim == True:
    print("Van benne prím szám:")
else:
    print("Nincs benne prím szám.")
    
#version2
primdb = 0
for i in range(10):
    if(prime(lista[i])):
        primdb = primdb + 1
        
if primdb > 0:
    print("Van benne prím szám:")
else:
    print("Nincs benne prím szám.") 
    

           