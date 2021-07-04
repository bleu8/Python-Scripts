# def tersAl(s):


#     #stringler immuatble bu yuzden bos str^'ye atıp ypmlyz

#     ters=""

#     for i in s:
#         ters+=i+ters

#     return ters

# tersAl("ali")



#daha kısası

def ters(s1):  #index 0dan basladıgı icin  geriye sayıcaz son indexten basa kadar 0 dahil degl -1 yazdık
    for i in range(len(s1)-1,-1,-1):
        print(s1[i],end="")

ters("ali")