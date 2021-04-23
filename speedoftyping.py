import time
import datetime

print("3")
time.sleep(1) #delay 
print("2")
time.sleep(1)
print("1")
time.sleep(1)

zaman=datetime.datetime.now()

metin =input("metin gir") # input yazdık direk bunu str alıcak.

zaman2=datetime.datetime.now()
#metni girdikten sonra fonk cagırılıypr ve bir daha zaman hesaplıyor.
speed=zaman2-zaman

saniye=round(speed.total_seconds(),2)
zaman3=round(len(metin)/saniye,1)

print("toplam süre {}" .format(saniye))
print("{} saniye basına".format(zaman3))
