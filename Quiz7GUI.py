serial = '0000000000509020'
serial = '1100000000509020'
dict = {}
for i in range(10):
    dict[chr(0x30+i)]=i
for j in range(6):
    dict[chr(0x41+j)]=10+j

from zio import *
def reverse(v24):
    return int(BIN(chr(v24))[::-1],2)

def get_value(c):
    return dict[c]

v40 = l32(0)+l32(0x4097a800) #dump from memory

result = 0
for i in range(8):
    a1 = get_value(serial[2*i])
    a2 = get_value(serial[2*i+1])
    if i&1:
        v24 = a1-a2
    else:
        v24 = a1+a2

    v27 = reverse(v24&0xff)
    v28 = ord(v40[i])

    print hex(v27),hex(v28)

    if (v27^v28)>0xf:
        add_value = (v28 - v24)&0xf
        print v28, v24, add_value
        print 'enter if'
    else:
        add_value = 0x18e8e
    result += add_value

print hex(result)
