a = '''
0x83,0x44,0xD1,0x66,0xA8,0x19,0xC0,0x57,
0xFC,0xB0,0x8D,0xCD,0x4B,0x2C,0x75,0x43,
0x1A,0x7C,0xF5,0xBF,0x97,0x5C,0xA0,0xE7,
0x74,0x10,0xAD,0x7A,0xDA,0x68,0xB6,0xA9,
0x6C,0xB1,0x06,0x67,0x10,0xF0,0xF8,0x03,
0x59,0x1B,0x67,0x40,0x84,
'''.replace('0x', '').replace(',', '').replace('\n', '').decode('hex')

c = ''
for i in range(1, len(a)):
    c += chr(ord(rsbox[ord(a[i])])^ord(a[i-1]))

from zio import *
print HEX(c)


plain = 'lag{C'

key = ''
for i in range(5):
    key += chr(ord(c[i])^ord(plain[i]))
    print hex(ord(c[i])), hex(ord(plain[i])), hex(ord(c[i])^ord(plain[i]))

print key

print len(c)

i = 1
if True:
    plain2 = ''
    for j in range(5):
        plain2 += chr(ord(key[j])^ord(c[4+i+j]))
    for j in range(5):
        plain2 += chr(ord(key[j])^ord(c[9+i+j]))
    for j in range(5):
        plain2 += chr(ord(key[j])^ord(c[14+i+j]))
    for j in range(5):
        plain2 += chr(ord(key[j])^ord(c[19+i+j]))
    for j in range(5):
        plain2 += chr(ord(key[j])^ord(c[24+i+j]))
    for j in range(5):
        plain2 += chr(ord(key[j])^ord(c[29+i+j]))
    for j in range(5):
        plain2 += chr(ord(key[j])^ord(c[34+i+j]))
    for j in range(4):
        plain2 += chr(ord(key[j])^ord(c[39+i+j]))
print i, plain2
