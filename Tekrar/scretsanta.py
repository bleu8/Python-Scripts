import random

isimler=["john","alex","kate","jamie",
"danielle"]

def hediye():

    alanlar=isimler.copy()
    verenler=isimler.copy()

    while len(alanlar)>0:
        alan_index=random.randint(0,len(alanlar)-1)
        verici=random.randint(0,len(verenler)-1)


        while alanlar[alan_index]==verenler[verici]:

            alan_index=random.randint(0,len(alanlar)-1)
            verici=random.randint(0,len(verenler)-1)

        


        print(alanlar[alan_index] , "su kisiye alcak---->", verenler[verici])

        del alanlar[alan_index]
        del verenler[verici]
        
        

hediye()


