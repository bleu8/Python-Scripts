sayi=int(input("kaca kadar?"))
print(2)
for i in range(3,sayi):
    kontrol=False
    for k in range(2,i):
        if i%k==0:
            kontrol=True
if kontrol == False:
    print(i)