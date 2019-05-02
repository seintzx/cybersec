#!/usr/bin/env python

import binascii, base64

s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

#hex string to string
hx = bytes.fromhex(s).decode('utf-8')

print(hx)

# base64 encode, the .encode() is to give bytes (required)
print(base64.b64encode(hx.encode()))
