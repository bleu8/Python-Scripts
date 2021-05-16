def selection(dizi):
    for i in range(len(dizi)):
        mini=i
        for j in range(i+1,len(dizi)):
            if dizi[mini]> dizi[j]:
                mini=j

        if mini !=i:
            dizi[mini],dizi[i]=dizi[i],dizi[mini]



dizim=[-1,456,-43,53,232,2]
selection(dizim)
print(dizim)