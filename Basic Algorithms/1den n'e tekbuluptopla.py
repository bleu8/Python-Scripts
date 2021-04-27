#first
"""
a=int(input("sayi"))

sum=0
for i in range (1,a):
    if not i%2==0:
        sum=sum+i


print(sum)



"""

#dongu aralıgı
n=int(input("sayi:"))

sum=0
for num in range(1,n,2): #mantıken 1-3-5 diye gidip num'a yazıcak
    sum=sum+num

print(sum)