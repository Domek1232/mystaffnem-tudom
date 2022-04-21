# Írasd ki az összes sort
file = open("adatok.txt",'r')
for e in file:
    print(e)
# Olvasd be a fájl első sorát, amely megadja, hogy összesen hány adatsor van.    
file.seek(0,0)
sor1 = file.readline().strip()
print(sor1)
# Írasd ki egy sorokszama.txt fájlba a sorok számát. 
file.seek(0,0)
sorszam = open("sorokszama.txt",'w')
sorszam.write(file.readline())
# Írasd ki külön az adatsorokat és külön az összes sorok számát.
file.seek(0,0)
print("sorok száma:",sor1)

sor2 = file.readline().strip()
print("Sorok száma a 2. sortól:",sor2)

sor3 = file.readline().strip()
print("Sorok száma a 2. sortól:",sor3)

sor4 = file.readline().strip()
print("Sorok száma a 2. sortól:",sor4)

sor5 = file.readline().strip()
print("Sorok száma a 2. sortól:",sor5)

sor6 = file.readline().strip()
print("Sorok száma a 2. sortól:",sor6)

sor7 = file.readline().strip()
print("Sorok száma a 2. sortól:",sor7)


# a sorokban levő 3 szám szorzatát írd ki. Csak az adatsorokkal dolgozz!