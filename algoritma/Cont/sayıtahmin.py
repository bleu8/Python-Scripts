import random 

ras=random.randint(1,1000)
#print(ras)
tahmin_sayi=0 #Tahmin Sayacı
yazılar=["bırak artık sayacı bozdun",
"never give up power may be with you",
"bilemedi ki xd"]
while True:
    tahmin_sayi+=1
    tahmin=int(input("1 ile 1000 arası sayi gir"))

    if tahmin_sayi>3:
        print(random.choice(yazılar))


    if ras==tahmin:
        print(f"bildin {tahmin_sayi}. tahminde")
        break

    elif ras>tahmin:
        print(f"girdigin {tahmin}degerini arttır")

    elif ras<tahmin:
        print("azalt")


