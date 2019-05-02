# decode single character XOR
import string
import binascii

def singlexor(s):
    encoded = binascii.unhexlify(s)
    for xor_key in range(256):
        for b in encoded:
            decoded = ''.join(chr(ord(b) ^ xor_key))
     print decoded


s = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

singlexor(s)
