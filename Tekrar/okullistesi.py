okul1=["john","dan","jamie"]
okul2=["casey","ben","kate"]

isim =input("isim ?")

if isim in okul1:
    print("1.okulda")
elif isim in okul2:
    print("2.okulda")

else:
    print("eşlesmedi")