buyukharfler="ABCDEFGHJKLOMNOPRSTUVWYZ"
kucuk="abcdefghjlmnoprstuvwyz"
rakamlar ="0123456789"
ozel_krk=",_.*!'+-"

bhsyisi=0
kckhr=0
rsy=0
oksayi=0



sifre=input("belirlediginiz sifreyi girin....")

for harf in sifre:
    if harf in buyukharfler:
        bhsyisi+=1
    elif harf in kucuk:
        kckhr+=1
    elif harf in rakamlar:
        rsy+=1
    elif harf in ozel_krk:
        oksayi+=1

if bhsyisi== 0 or kckhr ==0 or rsy==0 or oksayi==0:
    print("insecure")

else:
    print("sifre guvenli...")