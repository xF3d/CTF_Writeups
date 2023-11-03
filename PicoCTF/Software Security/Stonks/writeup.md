# Stonks (20 points)

Description:

I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure!

We are in whitebox, the code: [vuln.c](https://mercury.picoctf.net/static/a4ce675e8f85190152d66014c9eebd7e/vuln.c).
The service is running on `nc mercury.picoctf.net 59616` at the moment of writing.

To find a vulnerability we have to read the source code and try to find any potential vulnerability. Found a vulnerability at `printf(user_buf);` in the `int buy_stonks(Portfolio *p)` function. We can perform a Format String Injection here and get the stack's content, including the flag.

Python's `pwn` library will assist us. Lets send lots of `%x` that will print hex data, so we are sure we are getting the flag, then we get the data and strip it of any useless characters.

We tecnically have the flag, but we need to do a few more steps: we need to convert it from big edian to little edian. Then we get only the character that are ASCII, those are the only ones we need. Let's run the program and we get the flag.

picoCTF{I_l05t_4ll_my_m0n3y_bdc425ea}