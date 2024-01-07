#!/bin/python

# For some reason, calling the asm() function
# on ARM based machines throws an exception
# stating: "dpkg-query: no path found matching pattern *bin/i386*linux*-as*
# [ERROR] Could not find 'as' installed for ContextType(cache_dir = '/home/kali/.cache/.pwntools-cache-3.11')"

# Searching into this more I believe that pwntools is written for i386 / x86/64
from pwn import *

print(cyclic(50))
print(cyclic_find("laaa"))

print(shellcraft.sh())
#print(hexdump(asm(shellcraft.sh())))

# Spawns a Local Process Shell
#p = process("/bin/sh")
#p.sendline("echo hello;")
#p.interactive()

# Spawns Remote Shell
# First you want to spawn a listener
#   nc -lp 1234
#r = remote("127.0.0.1", 1234)
#r.sendline("hello!")
#r.interactive()
#r.close

print(p32(0x13371337))
print(hex(u32(p32(0x13371337))))

l = ELF('/bin/bash')

print(hex(l.address))
print(l.entry)

# Global Off-Set Table
print(hex(l.got['write']))

# Procedure Linkage Table
print(hex(l.plt['write']))

# Searching directly in an ELF file
# Seaching for the bytes b
for address in l.search(b'bin/sh\x00'):
    print(hex(address))

#print(hex(next(l.search(asm('jmp esp')))))

r = ROP(l)
print(r.rbx)

