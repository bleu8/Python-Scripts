def cevir(metin,sayi=[]):
    for i in range(len(metin)-1,-1,-1):
        sayi.append(metin[i])
    return "".join(sayi)

cumle=input("bir cumle gir:")

print("tersi: {}".format(cevir(cumle)))

#format icine fonk call yapabiliyoruz.

