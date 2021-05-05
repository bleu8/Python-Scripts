#Try kod çalısıyor
#except hata durumu 
#FİNALLY hatadan bagımsız calısması için


try:
    print(x)
except NameError:
    print("tanımsız") #NameError çıkarsa
except:
    print("baska bir hata olustu bilinmiyor") #buraya gitmwdi nameeroor var
finally:
    print("burası hep çalıscak")


#istedigimiz durumlarda hata olusturabiliyoruz

a=5
try:
    if a<6:
        raise Exception("hata olusturduk")

except:
    pass #atladı ilk hata mesajını 

if not type(a) is str:
    raise TypeError("sayi degil")