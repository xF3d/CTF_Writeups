s = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽"
d = ""

for e in s:
    value = ord(e)
    x = chr((value & 0xFF00) >> 8) #2 hex = 8 bits
    y = chr(value & 0xFF)
    d += x + y

print(d)