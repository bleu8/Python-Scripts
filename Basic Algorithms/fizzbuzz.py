sayi = int(input("sayı girin-->"))

if sayi % 15 == 0:
    print("FizzBuzz")
elif sayi % 3 == 0:
     print("Fizz")
elif sayi %5 == 0:
    print("Buzz")
    

    #mantık hatası 

"""sayi = int(input("sayı girin"))


if sayi % 3 == 0:
    print("Fizz")
elif sayi %5 == 0:
    print("Buzz")    #yukarıdakiler zaten saglandı alta girmez fizbuzz yukarıya tasınırsa o dar aralıgı tarayacaktır. 
elif sayi %5 and sayi %3  == 0
print("FizzBuzz")"""