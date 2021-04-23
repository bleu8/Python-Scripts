def metin(cumle,sayi=0):

    harfler="aeıioöuüAEIİOÖUÜ"

    for karakter in cumle:

        if karakter in harfler:

            sayi=sayi+1

    return sayi




cumle=str(input("cumle gir:"))


print("cumledeki unlu harfler:{}".format(metin(cumle)))
    