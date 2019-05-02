#!/usr/bin/env python


def spit(stri):
    even_s = ""
    odd_s = ""
    for i in range(0, len(stri)):
        if i % 2 == 0:
            even_s += stri[i]
        else:
            odd_s += stri[i]

    sti = even_s + " " + odd_s
    return sti


n = int(input().strip())

while True:
    try:
        line = input()
        if line:
            print(spit(line))
    except EOFError:
        break
