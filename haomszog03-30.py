list = []
haromszog = open("haromszogek.txt", 'r')
for sor in haromszog:
    print(sor)
haromszog.seek(0,0)

sor1 = haromszog.readline().strip()

sor2 = haromszog.readline().strip()
print(sor2)

list = haromszog.readline().split()
print(list)
print(max(list))
print(list[1])

ko = open("ki.txt",'w')
ko.write(list[1])

haromszog.seek(0,0)
for e in range(4):
   sor4 = haromszog.readline().split()
print(sor4)