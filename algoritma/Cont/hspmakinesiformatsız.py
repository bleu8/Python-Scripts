


while True:

        a=int(input("sayi gir"))
        b=int(input("sayi gir"))
        print("bir islem sec\n")
        islem=int(input("toplama--> 1 \n fark--> 2 \n carpma--->3 \n bolme--->4" ))


        if islem==1:
            print("sonuc" ,a+b)
        elif islem==2:
            print("sonuc" ,a-b)
        elif islem==3:
            print("sonuc" ,a*b)
        elif islem==4:
            print("sonuc" ,a/b)

        else:
            print("invalid")