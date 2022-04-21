mylist = ["alma" , "dió" ,"autó" ,"nyomtató", "Aranka" ]

#lista kiírása egymás alá.

for i in range(0, len(mylist)):
    print(mylist[i])
#lista elemeinek hosszának kiíratása.

for i in range(0, len(mylist)):
    print(mylist[i], ":", len(mylist[i]), "karakterből áll")
#egymás alá irassuk ki azokat a szavakat amely "A"-val kezdődik.

for i in range(len(mylist)):
    if mylist[i][0] == "a":
        print(mylist[i] , end = ",")

#egymás alá írassuk ki azokat a szavakat amely "A"-val kezdődik.
#a kis és nagy betűket ne különböztesse meg.

for i in range(len(mylist)):
    if mylist[i][0].lower() == "a" :
        print(mylist[i] , end = " ")

#szerepel-e a modnatba a rétes szó
mondat = "Ki szereti a rétest?"
print("rétes" in mondat)

#a lista mindenkori utolsó elemébe van-e y karakter
print("y" in mylist[len(mylist)-1])