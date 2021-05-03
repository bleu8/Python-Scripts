#kullanıcıdan ad soyad okul no dan olusan sifre isteniyor.sifre 
#ad soyad ilk ve son harfleri okul no'nun sonundaki 4 rakamadaki 
#tek sayıların toplamından oluscaktır.Sifreyi veren kodu yaz.

"""
ad =input("ad gir")
soyad=input("soyad gir")
s= (input("numara gir"))

#542351234 
#n1,n2,n3,n4----> sayi index
if int(s[-1]) % 2 == 1 :
    n1=int (s[-1])
else:
    n1=0
if int(s[-2]) % 2 == 1 :
    n2=int(s[-2])
else:
    n2=0
if int(s[-3]) % 2 == 1 :
    n3=int(s[-3])
else:
    n3=0
if int(s[-4]) % 2 == 1 :
    n4=int(s[-4])
else:
    n4=0

toplam=n1+n2+n3+n4
print(ad[0]+ad[-1]+soyad[0]+soyad[-1]+str(toplam))
"""

#sayac metoduyla kodu optimize edelim.



ad =input("ad gir")
soyad=input("soyad gir")
s= (input("numara gir"))

 
#--> sayi indexleriyle 
toplam=0


if int(s[-1]) % 2 == 1 :
    toplam=toplam+int(s[-1])

if int(s[-2]) % 2 == 1 :
        toplam=toplam+int(s[-2])

if int(s[-3]) % 2 == 1 :
        toplam=toplam+int(s[-3])

if int(s[-4]) % 2 == 1 :
        toplam=toplam+int(s[-4])


print(ad[0]+ad[-1]+soyad[0]+soyad[-1]+str(toplam))