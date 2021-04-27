yazi=input("Yaz")

sesli="aeıioöuü"
seslisum=0

for harf in yazi:
    if harf in sesli:
        seslisum+=1
print("sesli harf",seslisum)
print("sessiz harf",len(yazi)-seslisum)

