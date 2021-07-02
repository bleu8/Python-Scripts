a=int(input("agacınız kac katlı olsun?"))


for k in range(a):
        print(" " * (a-1-k))
        for i in range(k*2+1):
            print("*")

print()