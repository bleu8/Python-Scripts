"""
3 veya 5 in 1000den kucuk tüm katlarının toplamını bulunuz!!

"""

liste=[]
for i in range(1000):
    if i%3==0:
        liste.append(i)
    
    elif i%5==0:
        liste.append(i)


print(liste)

toplam=0
for a in liste:
    toplam=toplam+a

print(toplam)    
    


#aynisi veya baglacli
#%%

liste=[]
for i in range(1000):
    if i%3==0 or i%5==0:
        liste.append(i)


print(liste)

toplam=0
for a in liste:
    toplam=toplam+a

print(toplam)    





#daha kisasi 
#%%
toplam=0
for i in range(1000):
    if i%3==0 or i%5==0:
        toplam=toplam+i


print(toplam)








