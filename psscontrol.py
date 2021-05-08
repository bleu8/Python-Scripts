#Kullanıcıı giriş bilgilerini dogru girdiği takdirde toplama yaptıran program 

_username= "hesapmakinesi"
_password="hesap1234"


while True:
    username=input("kullanıcı adı?")
    password=input("sifre ver")

    if username != _username:
        print("boyle bir kullanıcı yokktur")


    elif password != _password:
        print("yanlıs parola")
        

    else:
        sayi_adedi=input("toplamak istedigin sayi adedi al")
        toplam=0
        for i in range(sayi_adedi):  #i 0 dan 
                sayi=int(input("lutfen {}. sayiyi gir").format(i+1))
                toplam+=sayi
                print("toplam",toplam)
                break


