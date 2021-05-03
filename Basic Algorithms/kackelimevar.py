a = input("bir metin gir")
bosluk=0
for k in a:
    if k == " ":
        bosluk+=1

#Bosluk +1 = Kelime

print("bosluk",bosluk)
print("kelime",bosluk+1)
print("harf",len(a))