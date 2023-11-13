# GET Scavenger Hunt (50 points)

Description:
There is some interesting information hidden around this site. Can you find it?
Site Link: http://mercury.picoctf.net:27278/.

This challenge looks like the continuation of `Insp3ct0r`, but it requeires a bit more brainwork.

I found many useful informations about web exploitations here: https://github.com/w181496/Web-CTF-Cheatsheet, I suggest giving a general look, as it contains various good informations depending on the challenges.

The flag is fragmented into different parts:
- In the `/index.html` : `picoCTF{t`
- In the `/mycss.css` : `h4ts_4_l0`
- Instead in the `/myjs.js` we find the question `How can I keep Google from indexing my website?`, this made me remember about a particular file used to tell the web crawlers of search engine which html pages they can access. Said file is `robots.txt` where we find : `t_0f_pl4c`
- We get another tip: `I think this is an apache server... can you Access the next flag?`. An important configuration file in Apache webservers is the `.htaccess` file, where we find : `3s_2_lO0k`
- Again another tip, this time it says: `I love making websites on my Mac, I can Store a lot of information there.`. There is a file used to save attributes of a folder in the macOS, that file is the `.DS_Store`. This is where we will find the last part of our flag : `_a69684fd}`

picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_a69684fd}