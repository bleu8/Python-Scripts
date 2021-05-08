import requests

while True:
    number=input("kim")
    mesaj=input("mesajınız")
    if "" in number or mesaj== " ":
        break

#Kendi ip mize random num almak için api kullanmamız lazım


    resp=requests.post('https://textbelt.com/test',{
        'phone' : '{}' .format(number), 
        'message': '{}' .format(mesaj),
        'key':  'textbelt'
        })


    print("islem {} kalan hak {} ".format('basarılı' if resp.json()[success]=='True'
                        else 'Basarisiz' ,resp.json()['quoteRemaining']))

    c=input("'exit()' or 'Enter' ")
    if c =="exit()":
        break
    else :
        pass