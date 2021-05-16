pincode=1234
puk=1212
deneme=3

while True:
    kod=int(input("kod gir"))
    if kod !=pincode:
        print("tekrar dene")
        deneme-=1
        print("kalan",deneme)
    else:
        print("hosgeldiniz")
        break
    if deneme==0:
        print("deneme hakkı bitti puk kodu gir")
        break

pu1=int(input("puk kodu gir"))
if pu1!=puk:
    print("bloke oldunuz")
else:
    print("giriş yapıldı...")
