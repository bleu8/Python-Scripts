# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 10:29:41 2021

@author: deno
"""

'''Mahmut a ulkesinde yasamkatadir bu ulkenin 
banknot degerleri 100 50 ve  10,1
Mahmutun parasina gore en az sayida 
banknot kullanmasi icin kac adet 
banknotu
olmali'''


while True:
    
    para=int(input("Para gir---->"))
    yuzluk=para/100 
    print("yuzluk--->",yuzluk)
    elli=int(para-(yuzluk*100)/50)
    print(elli)
    on=int(para-(yuzluk*100)-(elli*50)/10)
    print(on)
    bir=int(para-(yuzluk*100)-(elli*50)-(on*10))
    top=yuzluk+elli+on+bir
    print(top) 
            
    if para==0:
        print("bye")
        break
          