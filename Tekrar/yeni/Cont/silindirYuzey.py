# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 10:28:46 2021

@author: deno
"""

import math as m

a=int(input("yaricap?"))

h=int(input("yukseklik?"))

v=m.pi*a*a*h

s=2*m.pi*a**2 +2*m.pi*a*h

print("yuzey alanı",s)
print("hacim",v)
