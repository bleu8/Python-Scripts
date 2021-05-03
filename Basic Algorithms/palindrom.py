#tersten yazımi kendisi olan sayılar

for i in range(100,100000):
    s= str(i) #sayi 
    t=s[::-1]
    if s==t:
        print(s)