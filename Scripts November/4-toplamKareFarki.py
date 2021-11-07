"""

ilk 100 dogal saynin toplamlaırın karesiyle 
karelerin toplamı rasındaki fark


"""


def kareTop(n):
    toplm=0
    for i in range(n+1):
        toplm+=n**2
    return toplm
        
      
def topKare(h):
    top=0
    for u in range(h+1):
        top+=h
    return top**2

print(topKare(100),kareTop(100),topKare(100)-kareTop(100))

        
        