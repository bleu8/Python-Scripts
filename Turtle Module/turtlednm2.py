import turtle


kalem=turtle.Turtle()
kalem.speed(1)



kalem2=turtle.Turtle()
kalem2.color("magenta")
kalem2.width(20)
kalem2.speed(2)

kalem2.circle(100)


def kare(boy):
    for i in range(4):
        kalem.forward(boy)
        kalem.right(90)

def yildiz(boy):
    
    kalem.color("yellow")
    kalem.width(10)
    
    for i in range(5):
        kalem.forward(boy)
        kalem.right(144)

yildiz(200)


