#Fonksiyona kaç değer verirsem vereyim toplama olarak döndür

#args istediğim kadar deger dondurur

def isim(*args):
    print(args) #isim dondu
    print(args[0]) #deniz dondu

isim("deniz","okyanus")
den=(1,3,5)
print(den)

#ARGSTA DEMET DONDURDUK

def isimsoyisim(**kwargs):
    print(kwargs)


isimsoyisim(adı="deniz")
#kwargs -> sozluk donuduryo



def toplaBeni(*toplam):
    sayi=0
    for eleman in toplam:
        sayi+=eleman
        return sayi

print(toplaBeni(8,1,90)) 