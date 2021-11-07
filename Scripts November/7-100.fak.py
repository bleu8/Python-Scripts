"""

100! basamaklari toplami

"""

def fact(n):
    carpim=1
    for i in range(2,n+1):
        carpim*=i
    return carpim

sonuc=fact(100)

toplam=0  #string olarak forla icinde gezicez
for b in str(sonuc):
    toplam+=int(b)

print(toplam)       
        