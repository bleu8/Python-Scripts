sayi=int(input ("sayi nedir?"))
list = []


for i in range(2,sayi):
    durum=False
    for a in range(2,i):
        if i%a==0:
            durum=True
            break
    if not durum:
        list.append(i)
for i in list:
    print(i)
print("0 le {} arasında {} tane asal var".format(sayi,len(list)))