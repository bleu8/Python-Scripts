#ayların gün mktr

ocak = mart =mayıs=temmuz=agst=ekim=arlk=31
nisan=haz=eyl=kasım=30
sub=28

brmFyt=1.2516

aylık=int(input("aylık kac m3 dogal kullanıyorsun?"))

hangiay=input("hangi ay?")

ay=eval(hangiay)

gunlk=brmFyt/ay


fat=brmFyt*(gunlk*ay)

print(f"gunluk kullanım---> {gunlk} Fatura----> {fat}")