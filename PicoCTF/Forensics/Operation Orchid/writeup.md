# Operation Orchid (400 points)

Description:

Download this disk image and find the flag.
Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.

File given: [disk.flag.img.gz](https://artifacts.picoctf.net/c/212/disk.flag.img.gz).

First `unzip` the file.

I use `mmls` on the image and go for the largest disk.

Lets see this disk with `fls -o 411648 disk.flag.img`.

Lets check the root directory with `fls -o 411648 disk.flag.img 460`.

We see the `.ash history` and `flag.txt.enc`, after checking them using `icat -o 411648 disk.flag.img <number>` we see that both are useful, the first one tells us what happened to the flag while the second in the result of an encryption.

To get the flag we have to do an aes256 decrypt the flag, lets first get the file in one of four folder to facilitate the process: `icat -o 411648 disk.flag.img 1782 > decrypt.txt`.

If we decrypt with `openssl aes256 -d -salt -in decrypt.txt -out flag.txt -k unbreakablepassword1234567` the end result will be the flag.

picoCTF{h4un71ng_p457_0a710765}