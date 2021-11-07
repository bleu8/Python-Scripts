#en uzun collatz dizisi


"""

n- ciftse -> n/2 
tek ise --> 3n+1


13ten baslayip 1de sonlanan olusan dizi collatz 



bir milyonun altındaki hangi baslangic sayisi en uzun 
zinciri uretir?
"""

enUz=0
aranan=0
for sayi in range(999999,300000,-1):
    zincir=0
    n=sayi
    while n!=1:
        zincir+=1
        if n%2==0:
            n//=2 #tamsayili 
        else:
            n=3*n+1
    if zincir>enUz:
        enUz=zincir
        aranan=sayi
print("zincir sayisi",enUz,"sayi",aranan)
            
    