#verilen harfin ascii olup olmadıgını bulma

from string import ascii_letters
karakter =input("karakter gir")


if karakter in ascii_letters:
    print("true")
else:   
    print("wrong")

    #Sifrelerde cok onemli