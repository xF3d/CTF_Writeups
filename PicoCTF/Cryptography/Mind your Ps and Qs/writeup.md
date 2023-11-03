# Mind your Ps and Qs (20 points)

Description:

Download this disk image and find the flag.
Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.

The has some useful values [values](./values.txt).

`Decrypt my super sick RSA` on our way.

For a strong RSA encryption we need Ps and Qs that are very large, otherwise we end up with a "small" (in RSA the suggested amount is 2048 bits, so 2^2048 key size!) `n` value, like in this case. There are different way to compute `p` and `q`, but I will use [FactorDB](http://factordb.com/).

We obtain `p` and `q` and use them to calculate `phi`:

`p = 1617549722683965197900599011412144490161;
q = 475693130177488446807040098678772442581573;
phi = (p-1) * (q-1);`

Now to get the private key/exponent all that is left is compute the modular inverse of `e mod phi`. We use said exponent to decrypt the message and convert it back to ASCII to obtain the flag. You can find the code [here](./code.py).

picoCTF{sma11_N_n0_g0od_45369387}