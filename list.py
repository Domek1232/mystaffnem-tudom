#lista létrehozása:
mylist = ["Audi", "Peugeot", "Volkswagen"]
print(mylist)
#ellenőrzés:
print(mylist)

#listaelem elérése:
print(mylist[1])

#listaelemek száma
print(len(mylist))

# a mindenkori utolsó kiíratása:
print(mylist[len(mylist)-1])
print(mylist[-1])

# elem hozzáfűzése (a végéhez)
mylist.append("Dacia")
print(mylist)

#elem beszúrása megadott helyre
mylist.insert(2, "Suzuki")
print(mylist)

#beszúrás a mindenkori utolssó helyre *:
mylist.insert(len(mylist) ,"Renault")
print(mylist)

# listaelem eltávolítása inexszel
mylist.pop(2)
print(mylist)

# listaelem eltávolítása tartalom alapján
mylist.remove("Dacia")
print(mylist)

# lista bejárása
for i in range(len(mylist)):
    print(mylist[i])

#FELADAT: járjuk be a listát, vizsgáljuk meg minden elemnél, hogy Audi
#ha igen írjuk ki: "Ez Audi"
for i in range(len(mylist)):
    if mylist[1] == "Audi":   
        print("Ez Audi")

