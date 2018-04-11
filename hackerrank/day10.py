#!/bin/python3

import sys



n = int(input().strip())

a = bin(n)[2:].split('0')

print(len(a))
