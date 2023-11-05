import requests 
  
# Making a HEAD request 
r = requests.head('http://mercury.picoctf.net:53554/') 
  
# print headers recived 
print(r.headers) 
  
# print body recived 
print(r.content) 