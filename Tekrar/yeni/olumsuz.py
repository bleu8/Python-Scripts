# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 01:47:07 2021

@author: deno
"""

def negativ(string):
    if len(string)>0 and "not" in string:
        return string
    return "not \t" + string

print(negativ("happy"))
print(negativ("not good"))