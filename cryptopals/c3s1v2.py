#!/usr/bin/python3

from binascii import unhexlify
from Crypto.Util.strxor import strxor_c


# Single-byte XOR cipher
def crack_xor():
    cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

    cipherHex = unhexlify(cipher)
    print(cipherHex)
    import sys
    # English letters frequency http://www.data-compression.com/english.html
    #  etaoinsrhdlucmfwgypbvkxqjz
    englishFreq = {
        ' ': 0.1918182,
        'e': 0.1041442,
        't': 0.0729357,
        'a': 0.0651738,
        'o': 0.0596302,
        'i': 0.0558094,
        'n': 0.0564513,
        's': 0.0515760,
        'r': 0.0497563,
        'h': 0.0492888,
        'd': 0.0349835,
        'l': 0.0331490,
        'u': 0.0225134,
        'c': 0.0217339,
        'm': 0.0202124,
        'f': 0.0197881,
        'w': 0.0171272,
        'g': 0.0158610,
        'y': 0.0145984,
        'p': 0.0137645,
        'b': 0.0124248,
        'v': 0.0082903,
        'k': 0.0050529,
        'x': 0.0013692,
        'q': 0.0008606,
        'j': 0.0009033,
        'z': 0.0007836,
    }

    def fitness(string):
        string = string[1]
        score = 0
        print(string)
        for letter in string:
            try:
                score += englishFreq[chr(letter).lower()]
            except KeyError:
                pass
        return score

    # Complete ascii 0-255, 32 = Space, 122 = z
    out = max( [(i, strxor_c(cipherHex, i)) for i in range(0, 255)], key=fitness )

    print('Key: {}\nPlain Text: {}'.format(out[0], out[1].decode()))
    
    # # Explaination of what is 'out' up above
    #
    # for i in range(0,255):
    #     b = strxor_c(cipherHex, i)
    #     a = fitness(strxor_c(cipherHex, i))
    #     if a > maxx:
    #         maxx = a
    
    assert (strxor_c(out[1], ord('X')) == cipherHex)

if __name__ == '__main__':
    crack_xor()
