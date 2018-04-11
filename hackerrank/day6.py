#!/bin/python3
# Given a string S ,print its even-indexed and odd-indexed characters as space-separated strings on a single line.

import sys

def spit(stri):
    even_s = ""
    odd_s = ""
    for i in range(0,len(stri)):
        if i % 2 == 0:
            even_s += stri[i]
        else:
            odd_s += stri[i]
          
    sti = even_s + " " + odd_s
    return sti      
        
# this is because the first string was the number of string they will enter
n = int(input().strip())

while True:
    try:
        line = input()
        if line:
            print(spit(line))
    except EOFError:
        break
