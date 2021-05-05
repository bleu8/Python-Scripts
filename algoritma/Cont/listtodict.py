araba = {"marka":"lambo",
"model":"huracan",
"yil":"2010"
}



print(araba)
print(araba["marka"])

araba['yıl']=2020  #tektırnak

#sozlugu for dongusu kullanarak listeye attık
cars ={}
for deg in range(3):
    print(araba[deg])