
print("bilmediğiniz degere 0 yazın")
v=int(input("voltaj gir"))
i=int(input("akım gir"))
r=int(input("resistans gir"))



if v== 0:
    v=i*r 
    print("voltaj ----> ",v)

elif i== 0:
    i=v/r 
    print("akım ----> ",i)


else:
    r=v/i
    print("rez----->",r)