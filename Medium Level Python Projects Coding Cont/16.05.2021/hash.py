import hashlib

print("md5 cevirmek icin=1")
print("yazıyı sha256 cevirmek icin =2")


while True:
    a=int(input("secim yap"))
    if a==1:
            print("md5' cevriliyor......")
            m=input("yazi gir")
            md5=hashlib.md5(m.encode('utf-8')).hexdigest()
            print("md5 sifreniz",md5)
            break
    elif a==2:
            print("sha256'ya cevriliyor......")
            s=input("yazi gir")
            sha256=hashlib.sha256(s.encode('utf-8')).hexdigest()
            print("sha256 sifreniz",sha256)
            break
    else:
            print("cıkıyorum....")
            break

    