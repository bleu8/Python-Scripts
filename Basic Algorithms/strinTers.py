"""a=(input("isim ver"))

#1.yol
a=a[::-1]
print(a)"""

#mantıgı : string uzunlug buldu ve tersten donhu kurdu.


#2.yol

a=(input("isim ver"))

uzunluk=len(a)
print(uzunluk)

#Ters Dongu 
ters=""
for i in range(uzunluk-1,-1,-1): #indexten dolayı 0 a kadar dersek son sayıyı almıyor Python
    ters+=a[i] #harf harf alıp terse ekliyoz

print(ters)

