import random

def uret():
    n=random.randint(1,4)
    if n==1:
        return "*"

    elif n==2:
        return "R"


    elif n==3:
        return "G"

    elif n==4:
        return "B"
    



agackati=int(input("agac kaç katlı olsun?"))


for k in range(agackati):
    print(" "*(agackati-1-k),end=" ")
    for i in range(k*2+1):
        print(uret(),end="")
    print()
