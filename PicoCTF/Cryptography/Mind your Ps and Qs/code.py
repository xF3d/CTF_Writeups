c = 8533139361076999596208540806559574687666062896040360148742851107661304651861689;
n = 769457290801263793712740792519696786147248001937382943813345728685422050738403253;
e = 65537;

#Thank you http://factordb.com/
p = 1617549722683965197900599011412144490161;
q = 475693130177488446807040098678772442581573;
phi = (p-1) * (q-1);

#Function to convert the output to ascii, thank you https://github.com/Sazzad-Saju/RSA_Algorithm/blob/master/RSA%20Algorithm.py
def ConvertToStr(num):
    st = ""
    while (num != 0):
        temp = num % 256
        st += chr(temp)
        num = num - temp
        num = num // 256
    st = st[::-1]
    return st

# Compute modular inverse of e
d = pow(e, -1, phi) #first is base, second exponent, thrid mod
print( "d:  " + str(d) );

# Decrypt ciphertext
mes = pow(c, d, n)
mes = ConvertToStr(mes)
print(mes)