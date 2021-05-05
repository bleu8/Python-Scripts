#baska bir sınıftan ozellikleri ve metodları miras alma
#Farklı klass ozeliklerini altta kullanıyoruz
class Kisi:
    def __init__(self,ad,soyad):
        self.ad=ad
        self.soyad=soyad


    def goster(self):
        print(self.ad,self.soyad)


people=Kisi("johhny","depp")
people.goster()

class Actor(Kisi):
    pass

#ozellikleri yazmadım 

o1= Actor("Keanu","Reeves")
o1.goster()




