import random 
#boyut 
satir=int(input("sayi gir"))
sutun=int(input("sayi gir"))


m1 = [[0 for x in range(sutun)] for y in range(satir)] #mxn

mt = [[0 for x in range(satir)] for y in range(sutun)] #nxm

###Matrisi rabdom sayılarla dolduralım.
for i in range(satir):
    for j in range(sutun):
        m1[i][j]=random.randint(0,9)
        mt[j][i] = m1[i][j]

print(m1)
print(mt)




######
######  #2 sutun 5 satır var.


