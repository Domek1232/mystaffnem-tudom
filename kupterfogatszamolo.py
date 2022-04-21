#Feladat:
#Készítsünk egy olyan függvényt ami kiszámolja a kúp térfogatát
#Függvény:
#r sugárból és M magasságból kiszámolja a kúp térfogatát
#V = r^2* Pi*M/3
from cmath import pi
  
def terf(r: int, M: int) -> float:
    return r * r * pi * M / 3

sugar = 10
magasság = 20    
print(terf(sugar,magasság))
