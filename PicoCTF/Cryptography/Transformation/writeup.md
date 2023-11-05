# Transformation (20 points)

Description:
I wonder what this really is...
Encrypted flag: [enc](https://mercury.picoctf.net/static/dd6004f51362ff76f98cb8c699510f23/enc)
Encrypt algorithm: `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`

To get the string we need to do the exact opposite of what the encryption algorithm did.

By reading the encryption algorithm we can see that the loop takes 2 steps every cycle, because in one character it stores 2 of the flag's character, let's imagine in hexadecimal the single encrypted character:

`灩 = 0x7069`

we know that 1 hex character is equal to 4 bits, and a single ascii character is also equal to 4 bits. To store the first one it pushed the character `0x70` of 2 hex to the left, obtaining `0x7000`, and then added to the empty portion the next character `0x69`, obtaining `0x7069`.

If we convert `0x70` and `0x69` we get the letter `p` and `i`, the first 2 letters of a flag `picoCTF{xxxx}`. We need to write a python code to do that, we will use bitwise operators to do that:

- To get the first we AND for `0xFF00` obtaining `0x7000`, then we push right by 2 hex to get `0x70`.
- To get the second we AND for `0x00FF` (or just `0xFF`).

We add both characters to a variable and continue until the end of the ciphertext, then we print the flag. Code [here](./code.py)

picoCTF{16_bits_inst34d_of_8_0ddcd97a}