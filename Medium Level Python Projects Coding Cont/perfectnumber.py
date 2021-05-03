#mükemmel sayi

# 6  1 2 3


a= int(input("sayi gir:"))

adet =0

for i in range(1,a):  
    if a%i==0:   #bolen buluyoruz
        adet+=1


if adet==a:  #adetlerin toplamı --> girdigin ise mukemmel
    print(a,"girdigin sayi mükemmel")
else:
    print("degil")
