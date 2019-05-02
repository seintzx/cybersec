#!/usr/bin/env python3

# Compute all possibilities for caesar cipher
# NOTE: Not sure it works!!

import sys

text = "OMQEMDUEQMEK"
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
plaintext = ""
shift = 1
while shift <= 26:
    for c in text:
        if c in alphabet:
            plaintext += alphabet[(alphabet.index(c) + shift) %
                                  (len(alphabet))]
    print("Shift Used: " + str(shift))
    print("Ciphertext: " + text)
    print("Plaintext: " + plaintext)
    shift = shift + 1
    plaintext = ""
