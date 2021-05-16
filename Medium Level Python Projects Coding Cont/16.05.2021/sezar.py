#Sezar Encryption

metin="python"

sifre=" "



for i in metin:
    print(ord(i))  #asciii
    print(i , "=>" ,chr(ord(i)+5))  #decial 5 attı
    sifre=sifre+chr(ord(i)+5)  #sifreye ekle
print(metin, "--->" ,sifre)



