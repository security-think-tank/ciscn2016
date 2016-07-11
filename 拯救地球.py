a = 'YWJjZWRmZ2hpamtsbW5vcHFyc3R1dnd4eXoxMjM0NTY3ODkwLCA='
import base64

a2 = base64.b64decode(a)

ddd ='''
        v0[0] = 24;
        v0[1] = 3;
        v0[2] = 18;
        v0[3] = 36;
        v0[4] = 8;
        v0[5] = 19;
        v0[6] = 37;
        v0[7] = 8;
        v0[8] = 18;
        v0[9] = 37;
        v0[10] = 19;
        v0[11] = 7;
        v0[12] = 3;
        v0[13] = 37;
        v0[13] = 0;
        v0[15] = 13;
        v0[16] = 18;
        v0[17] = 22;
        v0[18] = 3;
        v0[19] = 17;
'''

indexs = []
for d in ddd.strip().split('\n'):
    indexs.append(int(d.split('=')[1].split(';')[0]))

print indexs

flag = ''
for index in indexs:
    flag += a2[index]

print flag
print base64.b64encode(flag)
