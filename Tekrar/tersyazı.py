def TersAl(string):
    liste=[]

    for i in string:
        liste.append(i)
    
    liste=liste[::-1]

    x=""
    for i in liste:
        x+=i


    return x

TersAl("ali")