from math import sqrt

for i in range(1,1001):
    for j in range(2,int(sqrt(i)+1)):
        if i%j==0:
            break
        
        else:
            print("asal")