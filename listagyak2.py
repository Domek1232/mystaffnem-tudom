# FELADAT: Kérj be a felhasználtótól 5 számot az alábiak szerint:
#"Add mega lista 2. elemét:"
#kérdezd meg tőle azt is,hogy az adott számok hányadik helyre szeretné tenni, és oda illeszd be! 
szamok = []
for i in range (5):
    print=("add meg a lista", i+i, "elemét")
    szám = int(input (""))
    szamok.insert(i,szám)
    print(szamok)
