import random
skor=0


while True:
    print("""*******************TAS KAGIT MAKAS
***************************""")
    rastgele_secim=["tas","kagıt","makas"]

    bilgisayar=random.choice(rastgele_secim)

    kullanıcı=int(input("tas-->1,kagıt-->2,makas-->3 \n"))


    if kullanıcı==1:
        if bilgisayar=="tas":
            print("berabere")
        elif bilgisayar=="makas":
            print("sen kazandın")
            skor+=10
        elif bilgisayar=="kagıt":
            print(f"yenildin ben {bilgisayar} sectim xd")
            skor-=10

    if kullanıcı==2:
            if bilgisayar=="kagıt":
                print("berabere")
            elif bilgisayar=="tas":
                print("sen kazandın")
                skor+=10
            elif bilgisayar=="makas":
                print(f"yenildin ben {bilgisayar} sectim xd")
                skor-=10

    if kullanıcı==3:
            if bilgisayar=="makas":
                print("berabere")
            elif bilgisayar=="kagıt":
                print("sen kazandın")
                skor+=10
            elif bilgisayar=="tas":
                print(f"yenildin ben {bilgisayar} sectim xd")
                skor-=10



print(f"toplam puan {skor}")