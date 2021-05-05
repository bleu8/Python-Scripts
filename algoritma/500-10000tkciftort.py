ciftTop=0
tekTop=0
cift_sayac=0
tek_sayac=0

for i in range(500,10000):
        if i %2==0:
            ciftTop+=i
            cift_sayac+=1
        

        else:  
            tekTop+=i 
            tek_sayac+=1
       

print("adet:",tek_sayac)
print("tek sayi toplam" ,tekTop)

print(ciftTop)