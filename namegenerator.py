#isim soyisim uretme

import random 

def isimolustur():
    ad=["dennis","james","jamie"]
    soyad=["rodman","mccavoy","jackson"]
    
    return "{} {}".format(random.choice(ad),random.choice(soyad))


print("-"*30)

for i in range(10):
        print(isimolustur())
    
print("-"*30)