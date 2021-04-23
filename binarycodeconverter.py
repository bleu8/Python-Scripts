s1=int(input(" cevirmek istedigin sayi gir:"))
binary=[]
#6 girdik 6 %2 =0 append --> 6/2 =3 --> en basa 3%2 =1 append ettik 3//2= tam kısmını alıcak 1 
# 1 1 0 --> binary is ready!!!
#ama burda while sartından dolayı bastaki 1 yok
while s1 > 1:
    binaryCode = s1 %2 
    binary.append(binaryCode)
    s1= s1 //2
binary.reverse()

print("1", end ="") #end birlestirmek icin. Asagıya inmemesi icin

for i in binary :
    print(i,end="")