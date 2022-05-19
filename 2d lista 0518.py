#file megnyitása
file = open('ub2017egyeni.txt', 'r',encoding='utf-8')

# lista létrehozása a sorok számára
lista = []

# első sor beolvasása (fejléc, nem csinálunk vele semmit)
file.readline()

#fájl sorainak bejárása 

for sor in file:
     #listához hozzáfűzöm
    lista.append(sor.strip().split(";"))
print(lista) 

#1. Feladat Van-e Zsolt keresztnevű induló 
print("--- 1. Feladat: ---")
vane = False
for k in range(len(lista)):
    if 'Zsolt' in lista[k][0]: 
        vane = True

if vane == True:
    print("Van benne Zsolt keresztnevű induló.")
else:
    print("Nincs benne Zsolt keresztnevű induló.")

# 2. Feladat Hány Noi induló volt?
print("--- 2. Feladat: ---")
NoiDb = 0
for z in range(len(lista)):
    if lista[z][2] == "Noi":
        NoiDb += 1

print("Ennyi olyan női versenyző volt aki teljesítette a távot: ", NoiDb)

#3. Feladat Átlagosan hány százalékát futották le a távnak.
print("--- 3. Feladat: ---")
ossz = 0
for f in range(len(lista)):
    ossz += int(lista[f][4])
print(ossz / len(lista), "% -a az átlag")

#4. Feladat Hány férfi futotta le 25 óránál kevesebb idő alatt a teljes távot?
print("--- 4. Feladat: ---")
fefifut = 0
for t in range(len(lista)):
    if lista[t][2] == "Ferfi" and int(lista[t][3].split(":")[0]) < 25:
        fefifut += 1
print(fefifut ,"Férfi futotta le 25 óránál kevesebb idő alatt a teljes távot.")