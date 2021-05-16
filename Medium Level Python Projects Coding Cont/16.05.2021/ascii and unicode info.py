b=ord("a") #---->ascii kodu 

s=chr(97) #ascii --> karakter 

S= "A\u00c4B\U000000E8c"
#unicode --utf8/utf16-utf32
d=S.encode("utf-8")#parantezbos kalsa bile utf-8
print(d)

#ASCİDE TÜRKÇE KARAKTER YOKTUR.
T="Türkce"

a=T.encode("ascii","ignore")
print(a)