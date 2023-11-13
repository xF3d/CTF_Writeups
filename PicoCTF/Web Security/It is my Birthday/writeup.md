# It is my Birthday (100 points)

Description:
I sent out 2 invitations to all of my friends for my birthday! I'll know if they get stolen because the two invites look similar, and they even have the same md5 hash, but they are slightly different! You wouldn't believe how long it took me to find a collision. Anyway, see if you're invited by submitting 2 PDFs to my website.
Site Link: http://mercury.picoctf.net:57247/.

By looking up `MD5 collision` I found https://www.mscs.dal.ca/~selinger/md5collision/. It talks about the algorithm of Wang and Yu, said algorithm can be used to create files of arbitrary length that have identical MD5 hashes. 

We have also 2 example files: `hello.exe` and `erase.exe`, we can create another `.pdf` file from an existing one with an implementation of the algorithm, however I decided to use a simpler approach by just renaming the example files to `hello.pdf` and `erase.pdf`.

picoCTF{c0ngr4ts_u_r_1nv1t3d_40d81ca2}