# Script

Useful script used in wargames and CTFs, or writed for personal pleasure.

If the name doesn't ring a bell, here's what you need

## Conversion

#### base64 to hex

b642hex.py  
Convert a base64 string into an hex string.  

#### binary to string

bin2str.py  
Convert a binary "number" into ASCII string.  

#### string to hex

str2hex.py  
Convert an ASCII string into an hex string.  

#### string to integer

str2int.py  
Convert an ASCII string into an intereg number.  

## Cryptography

#### caesar cipher

caesar-cipher.py  
Given a string, it computes all the possible combination of the famous caesar cipher.  
NOTE: I am not sure it works!!  

#### xor

xor.py  
Single character XOR encryption and decryption, input and output in hex string.  
Block character XOR encryption and decryption, input and output in hex string.  

#### sha-1

sha1gen.py  
Generates the SHA-1 hex string of an ASCII string.  

## RSA

#### easy decryption

rsa.py  
Taken for good that you how RSA works and its parameters, given `p, q, e, c/m` it generates the plaintext or the ciphertext.  

#### decryption from private key

decrypt\_rsa\_priv.py  
If you somehow have a private key you can get the public and decrypt the text.  
Further instruction inside the script.  
NOTE: You need to know the private key!!
