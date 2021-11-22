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
code =""
code += "cmp rdi, 0x3;"
code += "jg label;"
code += "jmp [rsi+0x8*rdi];"
code += "label:;"
code += "jmp [rsi+0x20]"

code_asm = pwnlib.asm.asm(code)
chall.send(code_asm)

print(chall.recvall())
