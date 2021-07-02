#asal sayı bulan program (1den 100)

asal=[]

for i in range(1,100):
    for k in range (2,i):
        if i%k==0:
            break
    else:
            asal.append(i)


print("bunlar asal--->",asal)
