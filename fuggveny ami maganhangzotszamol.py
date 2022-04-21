# 1. Feladat
#Készítsünk egy függvényt ami egy paraméterként megkappott szóba meg határozza a magánhangzók számát
from re import I


def maganhangzok_db(nap: str) -> int:
    db: int = 0
    mgh = "aáeéiíuúüűöőoó"
    for i in range(len(nap)):
        if nap[i] in mgh:
            db += i
    return db

print(maganhangzok_db("hétfő"))

#csinálj egy listát amibe a hét napjai vannak

napok = ['hétfő','kedd','szerda','csütörtök','péntek','szombat', 'vasárnap']
for elem in napok:
    print(maganhangzok_db(elem))

#mondjuk  meg azt hogy melyik napban van a legtöbb magánhangzó

maxHely = 0
for i in range(len(napok)):
    if(maganhangzok_db(napok[i]) > maganhangzok_db(napok[maxHely])):
        maxHely = i
print(napok[maxHely])
     