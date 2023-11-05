# ARMssembly 0 (40 points)

Description
What integer does this program print with arguments 4004594377 and 4110761777? Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

File: [chall.S](https://mercury.picoctf.net/static/006961dc756fc3f418b0dbe0a42dcee8/chall.S)

I solved this myself, but if you want to understand every assembly step in the file this isn't the place, I don't fully know assembly, I used a program to convert it into C without thinking much.

The file checks and prints the greatests of the 2 numbers given. 4110761777 is the greatest, so we need to hexify that and put it into the flag in the specified format.

picoCTF{f5053f31}