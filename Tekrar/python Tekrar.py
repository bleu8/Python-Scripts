#kontrol yapıları---------
"""
a=50
b=60

if a<b:
    print("a <b")

elif a==b :
    print("esit")

else:
    print("kucuk")



"""
"""
x=int(input("sayi gir"))
y=int(input("sayi gir"))

if x>y:
    print("x>y")
elif x<y:
    print("kucuk")
else:
    print("esit")

is1="ali"
is2="ALİ"

if is1>is2:
    print("a")
else:
    print("b")

    #asciiye göre oluyo bu olay
"""


#while
"""
a=0

while a<5:
    print("*")
    a=a+1
print("-------")
a=3
while a>0:
    print("*")
    a=a-1





i=0
while i<100:
    if i%2==0 and i %5==0:
        print(i,end="\t")
        i=i+1

"""


#for
"""
while True:
    a=input("devam mı?")

    if a=="yes":
        break


for i in range(0,100,2):
    print("*")



"""
"""
#dikdortgen olusturma
for k in range(3):
    for i in range(4):
        print("*",end=" ")
print()
"""
"""

while input("devam mı?") =="evet":

    a=int(input("kac satır?"))
    b=int(input("kac sutun?"))

    for i in range(a):
        for m in range(b):
            print("*",end=" ")
    print()

"""

#void fonksiyonlar


#def f1():
#      print("hello")

# # f1()


"""
def fn(a,b,c):
    print(a,b,c)


fn(3,2,5)

"""



#fonk içinde defalut verirsen dgierlerine de vermek zoerundasın


#astrokod Fonksiyonlar
"""
def slm(ad):
    print("slm"+ ad)

slm("\tali")
"""



#-faktoriyel 

def fact(a):

    if a>=0:
        if a==0:
            return 1
        else:
            sonuc=1
            for i in range(1,a+1):
               sonuc*=i
            return (sonuc)

    
    else:
        print("negatif kullanılamaz!!!")


'''
n=fact(5)
print(n)
'''

#sinus hesabı

def sin(acı):
    sonuc=0
    for i in range(10):
        tek=2*i+1
        isaret=pow(-1,i)
        deger=isaret*pow(acı,tek)/fact(tek)
        sonuc=sonuc+deger

    return sonuc


l=sin(3.14/2)
print(l)

