#Az első karaktert nagybetűvé alakítja
mondat = "géza kék az ég"
#--capitalize()-- capitalize(): az első karaktert nagybetűíti
print(mondat.capitalize())

#--swapcase()-- Kisbetűket cseréli ki nagybetűkre
print(mondat.swapcase())

#--title()-- Minden szó első karakterét nagybetűvé alakítja
print(mondat.title())

#--startswith()-- Igaz értéket ad vissza, ha a karakterlánc a megadott értékkel kezdődik
print(mondat.startswith("gé"))

#--endswith()-- Igaz értéket ad vissza, ha a karakterlánc a megadott értékkel végződik
print(mondat.endswith("gé"))
	
#--find()--	A megadott kifejezés kezdetének indexét adja
print(mondat.find("kék"))

#--rfind()-- Megkeresi a karakterláncot egy megadott érték után, és visszaadja a keresési hely utolsó helyét
print(mondat.rfind("a"))
	
#--index()-- Megkeresi a karakterláncot egy megadott érték után, és visszaadja a keresés helyét
print(mondat.index("az"))
	
#--rindex()-- Megkeresi a karakterláncot egy megadott érték után, és visszaadja a keresési hely utolsó helyét
print(mondat.rindex("é"))
	
#--isalnum()-- Igaz értéket ad vissza, ha a karakterlánc minden karaktere alfanumerikus
print(mondat.isalnum())
	
#--isalpha()-- Igaz értéket ad vissza, ha a karakterlánc összes karaktere szerepel az abc-ben
print(mondat.isalpha())
	
#--isdecimal()--  Igaz értéket ad vissza, ha a minden karakter tizedesjegy


#--isdigit()-- Igaz értéket ad vissza, ha a karakterlánc minden karaktere számjegy


#--islower()-- Igaz értéket ad vissza, ha a karakterlánc összes karaktere kisbetű
print(mondat.islower())

#--isnumeric()--  Igaz értéket ad vissza, ha a karakterlánc minden karaktere szám
print(mondat.isnumeric())

#--isspace()--	Igaz értéket ad vissza, ha a karakterlánc minden karaktere szóköz
# sortörés: \n tabulátor? \t és sóköz (stb)
ures = "     "
print(ures.isspace())

#--istitle()-- Igaz értéket ad vissza, ha minden szó nagy kezdő betűs
print(mondat.istitle())

#--isupper()--	Igaz értéket ad vissza, ha a karakterlánc minden karaktere nagybetű
print(mondat.isupper())

#--join()-- Az iterálható elemeket karakterláncokká alakítja
lista = ("Gizi", "Géza")
x = "*".join(lista)
print(x)
 
#--strip()-- A karakterlánc vágott változatát adja vissza
str1 = "      banana"
print(str1.strip)
 
#--lstrip()-- A karakterlánc bal oldali vágási változatát adja vissza
str1 = "      banana      "
print(str1)
print(str1.lstrip())

#--rstrip()-- A karakterlánc jobb vágású változatát adja vissza
str1 = "      banana      "
print(str1)
print(str1.rstrip())
 
#--split()-- Felosztja a karakterláncot a megadott elválasztónál, és egy listát ad vissza
szöveg = "kecske-ló-kuty-béka"
lista = szöveg.split("-")
print(lista)

#--rsplit()-- Felosztja a karakterláncot a megadott elválasztónál, és egy listát ad vissza(max paraméter nékül ugyan az mint a split)
szöveg = "kecske-ló-kuty-béka"
lista = szöveg.rsplit("-")
print(lista)

#--splitlines()--Felosztja a karakterláncot sortöréseknél, és egy listát ad vissza
szöveg = "kecske\nló\nkuty\nbéka"
print(szöveg)
lista = szöveg.splitlines()
print(lista)