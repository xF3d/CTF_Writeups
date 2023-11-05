# keygenme-py (30 points)

No description provided.
File: [code](https://mercury.picoctf.net/static/0c363291c47477642c72630d68936e50/keygenme-trial.py).

The source file of this program is huge, but all we care about is the key, as it contains the flag, so let's see for any code handling that part. The function `check_key(key, username_trial)` handles the check to know if the key is correct.

There is first a lenght check, then `key_part_static1_trial` is checked in a peculiar way: said part is compared to some characters in the SHA256 hash of the username ('MORTEN'). Then lets make a small program that copy pastes the position of said characters in a variable and then assemble the flag. Code [here](./code.py)

picoCTF{1n_7h3_|<3y_of_75fc1081}