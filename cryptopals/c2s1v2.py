#!/usr/bin/env python

from binascii import unhexlify
from Crypto.Util.strxor import strxor


# Write a function that takes two equal-length buffers and
# produces their XOR combination.
def fixed_xor():
    s = '1c0111001f010100061a024b53535009181c'
    key = '686974207468652062756c6c277320657965'
    result = '746865206b696420646f6e277420706c6179'

    # convert all to int from base 16
    shex = int(s, 16)
    keyhex = int(key, 16)

    # 1. Use bitwise operator ^ (supports only int in base 16)
    print('- Using ^ operator...')
    out = format(shex ^ keyhex, 'x')  # hex string rapresentation
    print(out)
    assert (out == result)
    print(unhexlify(result).decode('utf-8'))
    print('---------------------\n')

    # 2. Use Crypto lib (pycrypto)
    print('- Using Crypto lib...')
    out = strxor(unhexlify(s), unhexlify(key))
    print(out.decode('utf-8'))
    print('---------------------')


if __name__ == '__main__':
    fixed_xor()
