# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 10:29:29 2021

@author: deno
"""
"""
takim
mac sayisi
galibiyet malubiyet ayarla
toplam skor

"""


takim=input("takim gir?")
oyn=int(input("kac mac?"))

top=0
oyn
while oyn>0:
        mack=int(input("kazandiysa 1 \nkaybettiyse---2\n berabere--->3\n"))
        
        if mack==1:
            top=+5
        elif mack==2:
            top-=3
        else:
            top=top+0
        oyn-=1
            
            
with open("arsenal.txt") as dos:
    dos.write("arsenal.txt",top) 
    dos.write(str(top))
    dos.close()
with open("arsenal.txt") as dos:
    print(dos.read())       
