print("Szia! \n polip")

#értékadás változónak
nettoAr = 1500

#nettó ár változó kiírása
print(nettoAr)

#brutó ár kiírása
print(nettoAr*1.27)

#nettó ár változó kiírása magyarázattal
print("A nettó ár:",nettoAr,"ft",sep="")

#egyágú feltétel:
if(5<6):
    print("Hello!")

#kétágú feltétel:
if 5<6: print("Kisebb.")
else: print("Nem kisebb.")

#feltétel változókkal 
a = 243
b = 243
if a<b: print("Az 'a' kisebb 'b'-nél.")
else: print("Az 'a' nagyobb vagy egyenlő'b'-vel.")

#feltétel adatbekéréssel 
a = input("Add meg 'a'-t: ")
b = input("Add meg 'b'-t: ")

if a<b: print("A(z) " , a , " kisebb mint a(z)", b , ".")
else: print("A(z) " , a , " nagyobb vagy egyenlő mint a(z)", b , ".")

#egymásba ágyazott feltétel adatbekéréssel 
x = input("Add meg 'x'-t: ")
y = input("Add meg 'y'-t: ")

if x<y: print("A(z) " , x , " kisebb mint a(z)", y , ".")
else:
    if x>y:  print("A(z) " , x , " nagyobb mint", y , ".")
    else: print("A két szám egyenlő.")

#a szám 10-20 tartományon kívül van
a = int(input("Add meg 'a'-t: "))

if a < 20 or a > 20:print("A(z)", a , "a 10-20 tartományon kívül van.")
else: print("a feltétel nem teljesül.")

#a szám nagyobb 10-nél és osztható 4-gyel?
a = int(input("Add meg 'a'-t"))

if a > 10 and a % 4==0:print("A(z)", a ,"osztható 4-gyel")
else: print("A feltétel nem teljesül")

#a szám kisebb 20-nál és osztható 2-vel vagy 3-mal
a = int(input("Add meg 'a'-t"))

if a < 20 and a % 2==0 or a % 3==0:print("A(z)", a ,"osztható 2-vel vagy 3-mal")
else: print("A feltétel nem teljesül")




