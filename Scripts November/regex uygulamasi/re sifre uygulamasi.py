import re

dogum="1999"
karakter=["\?","\*","\%"]

def kontrol(sifre):
    if len(sifre)<8:
        raise Exception("en az 8 karakter")
    elif not re.search("[a-z]",sifre):
        raise Exception("sifreniz en az ibr kuck harf icermeli")
    elif not re.search("[A-Z]",sifre):
        raise Exception("en az bir buyuk harf icermeli")
    elif not re.search("[0-9]",sifre):
        raise Exception("sifreniz en az bir rakam icermelidir")
    elif not re.search(str(karakter),sifre):
        raise Exception("sifreniz ? *  % icermeli!!!")
    elif sifre.startswith(dogum)==True:
        raise Exception("dogum tarihi ile  baslayamaz!!!")
    elif sifre.endswith(dogum)==True:
        raise Exception("dogum tarihi ile bitemez!!!")
    else:
        print("sifre basarilidir.")
        
while True:
    try:
        sifre=input("olustur")
        kontrol(sifre)
    except Exception as hata:
        print(hata)
    else:
        break
        
        