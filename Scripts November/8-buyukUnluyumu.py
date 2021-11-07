"""
bir kelimenin buyuk unlu uyumuna uyup uymadıgını bulan fonk

"""

def Buyuku(kelime):
    kalin=["a","ı","o","u"]
    ince=["e","i","ö","ü"]
    
    kalins=0
    inces=0
    
    for i in kelime:
        if i in kalin:
            kalins+=1
        elif i in ince:
            inces+=1
    if kalins==0 or inces==0:
        return True
    return False

for g in range(5):
    kelime=input("Kelime Gir>>>")
    if Buyuku(kelime):
        print("Uyuyor")
    else:
        print("Uymuyor")
            
    