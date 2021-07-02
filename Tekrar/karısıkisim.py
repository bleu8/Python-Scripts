import random

def karıstır():
    ad=["john","emily","emma","elizabeth","jordan"]
    soyad=["parker","gold","candy","ali","quinn"]
    return "{} {}" .format(random.choice(ad),random.choice(soyad))



for i in range(5):
    print(karıstır())