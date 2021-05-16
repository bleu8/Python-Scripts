import random
import string

rkm=string.digits
sembol=string.punctuation
kucuk= string.ascii_lowercase
buyuk=string.ascii_uppercase
tum_krk=[rkm,sembol,kucuk,buyuk]


passw=" "

for i in tum_krk:
    for j in range(2):
        passw+= tum_krk[j][random.randint(0,9)]


#sifrede k ielemanları karıstıralım bunu karıstrmak icin shuffle kullanaz


passw=list(passw)
random.shuffle(passw)



yeni=""
for i in passw:
    yeni+=i

print(yeni)

