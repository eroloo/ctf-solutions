import pwn
from pwn import *
import os 
pwnlib.context.context.log_level="DEBUG"
pwnlib.context.context.os = 'linux'
pwnlib.context.context.arch = 'amd64'

def get_value(var_name, proc):
    proc.recvuntil("{} = ".format(var_name))
    val = proc.recvuntil("\n").decode("utf-8")
    val.replace(" ", "")
    return val

chall_id = int(os.environ["CHALLENGE_ID"])-193
chall = pwn.process(f"/challenge/embryoasm_level{chall_id}")
chall.recvuntil("Please give me your assembly in bytes (up to 0x1000 bytes): \n")
code = """
mov r9, 0x0
cmp:
cmp rdi, 0x0
je set0
cmp byte ptr [rdi + 1 * r9], 0x00
je end
inc r9
jmp cmp

set0:
mov rax, 0x0

end:
mov rax, r9
"""
code_asm = pwnlib.asm.asm(code)
chall.send(code_asm)

print(chall.recvall())
