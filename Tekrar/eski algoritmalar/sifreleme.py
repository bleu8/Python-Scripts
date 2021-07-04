#kullanıcıdan alınan ad soyad okulno ile sifrelemem yapılcak
# ilk ve sn harfer okulnonun son 4 rakamındaki tek sayılst toplamındna 


ad=input("adınızı gir")
soyad=input("soyadını gir")
numara=(input("no gir"))


toplam=0


for i in numara[-4:]:
    if i%2==1:
        toplam+=int(i)



print(ad[0]+ad[-1]+soyad[0]+soyad[-1]+str(toplam))