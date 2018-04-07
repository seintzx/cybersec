#!/usr/bin/python3

# import binascii

plain = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"

def repkeyxor(s, k):
    i = 0
    imax = len(k)
    ciphertext = ''
    for ch in s:
        ciphertext += str(hex(ord(ch)^ord(k[i]))[2:])
        if i == imax -1 :
            i = -1
        i += 1
    return ciphertext

if __name__ == "__main__":
    print(repkeyxor(plain, key))
