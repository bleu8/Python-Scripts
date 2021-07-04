while True:
    vasıta=input("vasıta seciniz ---> ucak/tren1-tren2/otobus--->")


    if vasıta=="ucak":
            grup=input("grup sec---> ekonomi/business---->")   
            if grup=="ekonomi":
                print("200 tl")
            elif grup=="business":
                print("400 tl")
    elif vasıta=="tren1":
            print("80tl")
    elif vasıta=="tren2":
            print("120 tl")
    elif vasıta=="otobus":
        print("90 tl")

    else:
        print("gecersiz")

    print("rezervasyon ayarlandı")

