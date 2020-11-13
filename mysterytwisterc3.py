from Crypto.Cipher import AES
from hashlib import sha1
from codecs import *
def 奇偶校验(k):
    res = ''
    bin_k = bin(int(k,16))[2:]
    for i in range(8):
        for j in range(8):
            if(j!=7):
                res += bin_k[i*8+j]
            else:
                res += str((bin_k[i*8:(i+1)*8-1].count('1')+1)%2)
    return hex(int(res,2))[2:]

#算 '?'
a = [7,3,1,7,3,1]
b = [1,1,1,1,1,6]
c = 0
for i in range(6):
    c += a[i]*b[i]
print(c%10)
#'12345678<8<<<1110182<1111167<<<<<<<<<<<<<<<4'

MRZ_information = '12345678<811101821111167'
SHA1 = sha1(MRZ_information.encode()).hexdigest()
#print(SHA1)
#a095f0fdfe51e6ab3bf5c777302c473e7a59be65
#ea8645d97ff725a898942aa280c43179


Kseed = SHA1[:32]
D = Kseed + '00000001'
H = sha1(decode(D,'hex')).hexdigest()
Ka = H[0:16]
Kb = H[16:32]
key = str(奇偶校验(Ka))+str(奇偶校验(Kb))
print(key)
aes = AES.new(decode(key,'hex'),AES.MODE_CBC,iv=b'\x00'*16)
c = '9MgYwmuPrjiecPMx61O6zIuy3MtIXQQ0E59T3xB6u0Gyf1gYs2i3K9Jxaa0zj4gTMazJuApwd6+jdyeI5iGHvhQyDHGVlAuYTgJrbFDrfB22Fpil2NfNnWFBTXyf7SDI'
print(aes.decrypt(decode(c.encode(),'base64')))

