# XOR between hex strings
# Convert both string into integer
# int(StrToConvert, BaseOfStr)
# BaseOfStr is the format of the string
# ie: base= 16 for hex, base= 2 for binary
# XOR the two integer and convert then into hex


def hexor(s1, s2):
    h1 = int(s1, 16)
    h2 = int(s2, 16)
    res = hex(h1 ^ h2)
    print res
    return res[2:-1]


#MAIN
s1 = '1c0111001f010100061a024b53535009181c'
s2 = '686974207468652062756c6c277320657965'

print hexor(s1, s2)
