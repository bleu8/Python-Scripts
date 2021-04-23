name1 = input("sizin isminiz:")

name2= input("onun ismi:")

love = len(name1)+ len(name2)

if len(name1)> len(name2):
    love-=5
else:
    love+=3

love *=42

love = love/(100+len(name2))

love =10 if love > 10 else round(love,0)

print("{} ve {} skor {} 10 üzerinden sevgi puanı ".format(name1,name2,love))
