#feladat: 3 bekért számról döntsök el, hogy háromszög-e

a = int(input("Add meg a háromszög'a' oldalát"))
b = int(input("Add meg a háromszög'b' oldalát"))
c = int(input("Add meg a háromszög 'c' oldalát"))
if a<b+c and b<a+c and c<a+b:
    print("Háromszöget alkot")
    print("A háromszög kerülete:", a+b+c)
else: print("Nem alkot háröszöget")

import math

a = int(input("Add meg a háromszög'a' oldalát"))
b = int(input("Add meg a háromszög'b' oldalát"))
c = int(input("Add meg a háromszög 'c' oldalát"))
perimeter = a+b+c
s = (a+b+c) /2
t = math.sqrt((s*(s-a)*(s-b)*(s-c))) ** 0.5
print("A háromszög területe", t, "cm")
print("A háromszög kerülete", perimeter, "cm²")