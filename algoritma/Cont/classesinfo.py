class Sınıf():
    ornek=50


n1=Sınıf() #nesne olustrudk
print(type(n1))
print(n1.ornek) #sınıflardan nesne olustrup kullandık



#__init__ fonksiyonu #tanımlarsak tüm sınıflarla otomatik tanımlanır


class Kisi():
    def __init__(self,isim,yas):
        self.isim=isim
        self.yas=yas
   
    def selam(self):
        print("merhaba",self.isim)

kisi1=Kisi("Ahmet",54)
kisi2=Kisi("")

print(kisi1.isim)
print(kisi1.yas)

kisi1.selam()


kisi1.isim =John 

kisi2.selam()


