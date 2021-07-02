a=input("your name?----->")
b=input("her/his name?---->")



love = len(a)+len(b)

if len(a)>len(b):
    love-=5

else:
    love+=3

love *=42
love = love/(100+len(b))


print(f" your love {love} out of 10 ")

