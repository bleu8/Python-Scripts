def bubble(dizi):
    for i in range (len(dizi)-1):
        for j in range (len(dizi)-1-i): #swap icin en son elaman cıkıcak yani i 
            if dizi[j] > dizi[j+1]:
                dizi[j],dizi[j+1]= dizi[j+1],dizi[j]

dizi=[-13,-5,676,23,1,76,2,6]


bubble(dizi)
print(dizi)

