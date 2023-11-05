# Matryoshka doll (30 points)

Description:
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one?
Image: [this](https://play.picoctf.org/practice/challenge/129?page=2#:~:text=Matryoshka%20dolls%20are%20a%20set%20of%20wooden%20dolls%20of%20decreasing%20size%20placed%20one%20inside%20another.%20What%27s%20the%20final%20one%3F%20Image%3A%20this)

Matryoshka makes me think about hidden embedded files, let's leave this to `binwalk`. I ran `binwalk -Me <file>`, `-M` standing for Matryoshka itself, which recursively checks for embedded files and `-e` to look for known file types.

A lot of files got extracted and if we get to the end of them we get the flag

picoCTF{ac0072c423ee13bfc0b166af72e25b61}