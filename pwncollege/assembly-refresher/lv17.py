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
chall.recvuntil("We will now set the following in preparation for your code")
code = "jmp lv17;"
code += ".rept 0x51; nop; .endr;"
code += "lv17:"
code += "pop rdi;"   
code += "mov rax, 0x403000;"
code += "jmp rax"
code_asm = pwnlib.asm.asm(code)
chall.send(code_asm)

print(chall.recvall())
