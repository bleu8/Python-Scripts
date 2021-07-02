import random
import string

rakam=string.digits
semboller=string.punctuation
kucuk=string.ascii_lowercase
buyuk=string.ascii_uppercase
all_of=[rakam,semboller,kucuk,buyuk]

sifre=""


for j in range(4):
        for i in range(2):
            sifre+=all_of[j][random.randint(0,9)]


print(sifre)



