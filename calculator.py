
#basic calculator
sayi1=int(input("ilk sayi:"))
sayi2= int(input("ikinci sayi"))

secim=int(input("secim yap 1.toplama, 2 carpma 3 bolme 4 cıkarma" ))


if secim==1:
    print("sonuc {}".format(sayi1+sayi2))
elif secim==2:
        print("sonuc {}".format(sayi1*sayi2))

elif secim==3:
        print("sonuc {}".format(sayi1/sayi2))

elif secim==4:
        print("sonuc {}".format(sayi1-sayi2))

else :
    print("hatali")