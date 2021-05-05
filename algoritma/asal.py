
bolen_sayac=0

for j in range(3,100):   #burdan j seciyoruz
    bolen_sayac=0   

    for i in range(2,j): #i  sectin (j zaten dahil degil)j'ye kadar 2den baslayıp bolmup bolmedigini kontrol et
        if j%i==0:
            bolen_sayac+=1


    if bolen_sayac==0:  #2 ve gerisindeki katlar bolmuyorsa asal

        print(j)

