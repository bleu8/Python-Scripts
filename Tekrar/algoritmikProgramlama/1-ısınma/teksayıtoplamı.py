#listeden tek sayıları alıp toplayıp dobnduren fonkisyon

def teksayı(liste):
    sayac=0
     

    for i in liste:
        if i %2==1:
            sayac=sayac+i

        return sayac




teksayı([1,34,67,12,31,72])
