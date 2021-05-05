"""

a=input("vasita gir")
sınıf=input("sınıf giriniz")


if a == "ucak":
        if sınıf == "ekonomi":
            print("200 tl")
        elif sınıf=="business":
            print("300tl")
elif a=="tren":
    if sınıf=="1" :
        print("80 tl")  
    elif sınıf=="2":
        print("120 tl")

elif a=="otobus":
    if sınıf== " ":
        print("90 tl")

else:
    print("gecersiz!")
"""

#kodu iyilestirelim

vasita=input("vasita gir")

if vasita== "otobus":
    print("90")
elif vasita=="tren" or vasita=="ucak":
    sinif=input("sinif gir")
    if vasita== "ucak":
        if sinif=="business":
             print("300")
        elif sinif=="ekonomi":
            print("200 tl")
    elif vasita== "tren":
        if sinif=="1":
            print("80 tl")
        elif sinif=="2":
            print("60tl")
else: 
    print("gecersiz")
