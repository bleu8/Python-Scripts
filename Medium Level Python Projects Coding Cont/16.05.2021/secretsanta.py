import random

names=["john","jeremy","alice","robert","kenny"]

def gift():
    taker=names.copy()  
    giver=names.copy()

    while len(taker) > 0:

            tk=random.randint(0,len(taker)-1)
            gv=random.randint(0,len(giver)-1)

            while taker[tk]==giver[gv]: 
                tk=random.randint(0,len(taker)-1)
                gv=random.randint(0,len(giver)-1)


            print(taker[tk] ,"will give the gift" ,giver[gv])

            del taker[tk]
            del giver[gv]


gift()