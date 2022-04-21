import random
#Hozz létre egy üres listát!
szamok = []
for i in range(0, 10):
#Töltsd fel 10 random számmal.    
    szamok2 = random.randint(1,10)
    szamok.append(szamok2)
    print(szamok2)
# Kérj be a felhasználótól egy számot, szúrd be a 2. helyre.
a = int(input("Adj meg egy tetszőleges számot:")) 
szamok.insert(1,a)
#Rendezd sorba a listát
szamok.sort()
print(szamok)