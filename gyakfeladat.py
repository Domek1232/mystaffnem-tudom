#Kérjen be három egész típusú számot és tárolja el,majd
a = int(input("Adjon meg egy tetszőleges egész számot:"))
b = int(input("Adja meg a második tetszőleges egész számot:"))
c = int(input("Adja meg a harmadik tetszőleges egész számot:"))
#írja ki, hogy melyik a nagyobb, melyik a kisebb és melyik a "középső"szám!
maximum = max(a,b,c)
minimum = min(a,b,c)
if (a != maximum and a != minimum):
    medium = a
if (b != maximum and b != minimum):
    medium = b
#Feltételezheti, hogy a három szám nem egyenlő
else:
    medium = c
print(minimum, medium, maximum)

#az a feladat megoldás ahogy el kezdtem 
szamok = [a,b,c]
szamok.sort()
print("legkisebb: ",szamok[0], "középső:",szamok[1], "legnagyobb: ", szamok[2])