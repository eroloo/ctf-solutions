import pwn
from pwn import *
import os 
#pwnlib.context.context.log_level="DEBUG"
pwnlib.context.context.os = 'linux'
pwnlib.context.context.arch = 'amd64'

def get_value(var_name, proc):
    proc.recvuntil("{} = ".format(var_name))
    val = proc.recvuntil("\n").decode("utf-8")
    return val


chall_id = int(os.environ["CHALLENGE_ID"])-193
chall = pwn.process(f"/challenge/embryoasm_level{chall_id}")
chall.recvuntil("We will now set the following in preparation for your code")
rdi_val = get_value("rdi", chall)

code = "mov rdi, {};".format(rdi_val)
code += "add rdi, 0x331337"
code_asm = pwnlib.asm.asm(code)

chall.send(code_asm)

print(chall.recvall())