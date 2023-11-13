# Who are you? (100 points)

Description:
Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn 
Site Link: http://mercury.picoctf.net:39114/.

Alright lets check the site. The page says: `Only people who use the official PicoBrowser are allowed on this site!`

I already feel like am gonna play with HTTP packets here so I suggest installing BurpSuite. I am gonna start by changing an element in the header of the request `User-Agent: PicoBrowser`. This site has also helpful insights in such topics https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/.

Ok now it says `I don't trust users visiting from another site.`, alright lets add a referrer header and put the same site `Referer: http://mercury.picoctf.net:39114/` (It isn't a typo, this is the syntax).

The site now tells us `Sorry, this site only worked in 2018.`, it enjoys playing hard to get, lets add yet another header for date this time `Date: Mon, 1 1 2018 1:1:1 GMT`.

It is still holding up with `I don't trust users who can be tracked.` Alright we are getting into the open field of HTTP deprecated headers, this time the header to set is `DNT: 1`.

`This website is only for people from Sweden.` guess we are gonna become swedish now, we are gonna pretend to be a proxy of a sweeden IP address with the header `X-Forwarded-For: 102.177.146.0`. (Found on https://lite.ip2location.com/sweden-ip-address-ranges)

I don't speak sweedish? Of course I do! `Accept-Language: sv,en;q=0.9`. (Or maybe not)

Here the full headers you need to use in case you got fed up halfaway.

User-Agent: PicoBrowser
Referer: http://mercury.picoctf.net:39114/
Date: Mon, 1 1 2018 1:1:1 GMT
DNT: 1
X-Forwarded-For: 102.177.146.0
Accept-Language: sv,en;q=0.9

picoCTF{c0ngr4ts_u_r_1nv1t3d_40d81ca2}