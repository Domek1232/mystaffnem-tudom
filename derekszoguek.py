#derékszögűháromszög
a = int(input("Add meg a háromszög'a' oldalát"))
b = int(input("Add meg a háromszög'b' oldalát"))
c = int(input("Add meg a háromszög 'c' oldalát"))
if pow(a, 2) + pow(b, 2) == pow(c, 2):
    print("A háromszög derékszögű")
else:
    print("A háromszög nem derékszögű")

#derékszögűháromszög2
a = int(input("Add meg a háromszög'a' oldalát"))
b = int(input("Add meg a háromszög'b' oldalát"))
c = int(input("Add meg a háromszög 'c' oldalát"))
if a*a + b*b == c*c:
    print("A háromszög így is derékszögű")
else:
    print("A háromszög így sem egy derékszögű")