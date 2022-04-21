import math
a = int(input("Adj meg egy számot:"))
b = int(input("Adj meg egy számot:"))

print("a két megadott szám:", a ,"és", b)
c = math.sqrt (pow(a, 2) + pow(b, 2)) 
print("A(z) átfogó hossza:", c)
if (c<0):
     print("nincs megoldás")
