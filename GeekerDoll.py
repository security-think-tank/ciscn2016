global_count = 0
def get_modify_input():
    global global_count
    r14_value = get_reg(r14)
    rax_value = get_reg(rax)
    if rax_value ==0x0000000000482608:
        if r14_value > global_count:
            global_count = r14_value

OnBreakpoint(0x000000000045b909, get_modify_input)

k = []
for j in range(0x30, 0x3a):
    k.append(j)
for j in range(0x41, 0x40+26):
    k.append(j)
for j in range(0x61, 0x60+26):
    k.append(j)

k.append(ord('{'))
k.append(ord('}'))
k.append(ord('_'))

#def start_record():
#OnBreakpoint(0x40790D, start_record)
flag = 'flag{pwnpwnpwn'
for i in range(10):
    for j in k:
        global_count = 0
        try_flag = flag + chr(j)
        print(try_flag)
        gdb.execute('set args ' + try_flag)
        gdb.execute("run")
        print(global_count)
        print(len(try_flag))
        if global_count == len(try_flag):
            flag += chr(j)
            break
print(flag)
