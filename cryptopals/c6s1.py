#Break repeating-key XOR, Cryptopals c6 s1

import base64

# This function compute the Hamming distance between two strings
def hamdist(s1, s2):
    d = 0
    for ch1, ch2 in zip(s1, s2):
        c1 = ord(ch1)
        c2 = ord(ch2)
        while c1 or c2:
            b1 = c1 & 1
            b2 = c2 & 1
            d += b1 ^ b2
            c1 >>= 1
            c2 >>= 1
    return d

def findkey(b64_s):
    key_dict = {}
    low = 9999
    previous = 0
    for size in range(2, 40):
        ham1 = b64_s[previous : size + 1]
        ham2 = b64_s[size + 1 : size * 2 + 1]
        low = hamdist(ham1, ham2)/size
        key_dict = {low : size}
        previous = size
    return(key_dict[low])

def break_xor(b64_s):
    result = '' 
    return result

# Read file
b64_str = ''
with open("file.txt") as f:
    for line in f:
        b64_str = b64_str + str(line)

# Decode and print the result
print break_xor(base64.b64decode(b64_str))
