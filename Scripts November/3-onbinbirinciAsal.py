def asal(n):
    for bolen in range(2,n//2):
        if n%bolen==0:
            return False
    return True


sira=6
sayi=13
        
        #6.siradaki sayi 13
        
while sira<10001:
    sayi+=1
    if asal(sayi):
        sira+=1
        
        
print("sayi-->",sayi)
        