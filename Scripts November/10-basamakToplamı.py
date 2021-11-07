"""

klavyeden girilen xve y sayinin --> x^y basamak toplami

"""

def btoplam(x,y):
    sayi=x**y
    print(sayi)
    toplam=0
    
    for i in str(sayi):
        toplam+=int(i)
    return toplam


tb=int(input("taban gir"))
us=int(input("us gir"))

print(btoplam(tb,us))
    