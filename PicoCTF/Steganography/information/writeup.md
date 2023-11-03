# information (10 points)

Description:

Files can always be changed in a secret way. Can you find the flag? 

Image given: [cat.jpg](https://mercury.picoctf.net/static/a614a27d4cb251d04c7d2f3f3f76a965/cat.jpg)

I start with a naive approach to search for a flag in plain sight `cat cat.jpg | grep picoCTF`, however nothing interesting comes out.

Maybe it is hidden using steganography, so I try to find useful info by uploading it to [Stegonline](https://stegonline.georgeom.net/).

Nothing again, I decide to see the whole file with `cat cat.jpg` and find these 2 base64 strings `W5M0MpCehiHzreSzNTczkc9d` , `cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9`.

The first one is useless data whereas the second one has the flag we are looking for.

picoCTF{the_m3tadata_1s_modified}