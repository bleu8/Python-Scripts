from math import sqrt
for i in range(1,1001):
    if int(sqrt(i))**2==i: #karekokunu alıp karesini alınca sayı tsamsayı cıkarsa sayı tamsayıdır
        print("karekok {} = {} {} tamsayi olan bir sayidır".format( i,sqrt(i), i))
