#Számold ki a gúla felszínét, térfogatát
import math
a = int(input("Add meg a(z) gúla alapjának oldalhosszát:"))
m = int(input("Add meg a(z) gúla magasságát:"))

#(V)= térfogat (Ta)=Terület (A)Felszzín
if m>0:
    Ta = pow(a ,2)
    print("A(z) területe:", Ta)
    V = Ta*m /3
    print("A(z) gúla térfogata:", V)

    #(b) az alap fele,T3szög a háromszög területe
    b = a/2
    c2 = m**2 + b**2
    c = math.sqrt (c2)
    T3szog = (a * c)/2
    A = 4 * T3szog + Ta
    print("A(z) gúla felszíne:", A)

    #tanárverzió

    alapel = int(input("Add meg a gúla alapjának élét"))
    gulaMagassag = int(input("Add meg a gúla magasságát:"))

    if (gulaMagassag > 0):
        #a palást háromszogének magassága
        oldalMagassag = math.sqrt(pow(alapel/2,2) + pow(gulaMagassag,2))
        print("A gúla oldalának magassága:", oldalMagassag)

        #a gúla térfogata
        V = (alapel * alapel * gulaMagassag)/3
        print("A gúla térfogata:", V)

        #a gúla felszíne
        F = (2* alapel * oldalMagassag) + alapel * alapel
        print(" A gúla felszíne:",F)

     
   




