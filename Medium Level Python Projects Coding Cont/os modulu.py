#BILGILENDIRME LINUX ONCESİ

#isletim sistemi hk bilgi verir.
#name  getcwd mkdir rename remove name  makedirs


import os

#print(dir(os)) #butun moduller asagıda

#print(os.name) #--> nerdeyim? dosya olarak

#print(os.getcwd()) #hangi klasordeyim?

#print(os.mkdir("yenidosya")) #yenidosya acıcak yanda açtı bile :D

#print(os.makedirs("newfile")) #yeni açılan dosya içine klasor

"""
for dosya in os.listdir():
    if dosya.endswith(".py"): 
        print(dosya)"""

#burda yandaki butun.py uzantılı dosyaları gorduk



#os.system("notepad.exe")
#sistemden not defteri actık 

#file ismi degistirme

os.rename("newfile","yeni")


#alt dosya silme
#os.removedirs("yeni/yenidosya")