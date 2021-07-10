

a=int(input("sayı gir"))
bolen =0

for i in range(1,a+1):
    if a%i==0:
        bolen=+i


if bolen ==a:
    print("mukemmel")

else:
    print("degildir")