# A szökőév meghatározásához készítsünk saját függvényt!
# Szökőév minden 400-al osztható é, illetve 
#a 4-el osztható, de 100-al nem osztható évek.
def szoko(ev):
    
    return ev%400==0 or (ev%4 == 0 and ev%100 != 0)

ev = int(input("Addja meg az évet:"))
ev2 = int(input("Addja meg a második évet"))
#vizsgálja meg a két szám között lévő szükőévek számát
db = 0
for evek in range(ev, ev2):
    if szoko(evek):
        print(evek)
        db = db +1
if (db == 0):
    print("Nem volt szövőév.")