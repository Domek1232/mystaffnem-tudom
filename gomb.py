#gömb
import math
r = int(input("Add meg a gömb sugarát: "))
felszin = 4* math.pi * pow(r,2) 
terfogat = (4/3)* math.pi * pow(r,3)
decimal_terfogat = "{:.2f}".format(terfogat)
decimal_felszin = "{:.2f}".format(felszin)
print("A gömb térfogata: ",decimal_terfogat,"cm", sep='')
print("A gömb felszíne: ",decimal_felszin, "cm²",sep='')

#hajó
print("     /\\")
print("    /  \\")
print("\\- - - - - /")
print(" \\________/")

#vonal
print(" \\")
print("  \\ ")
print("   \\")
print("    \\")
print("     \\")