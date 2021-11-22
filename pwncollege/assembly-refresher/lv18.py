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
code = "";
code += "cmp dword ptr [rdi], 0x7f454c46;"
code += "je label1;"
code += "cmp dword ptr [rdi], 0x00005A4D;"
code += "je label2;"
code += "jne label3;"

code += "label3:"
code += "mov eax, dword ptr [rdi+4];"
code += "imul eax, dword ptr [rdi+8];"
code += "imul eax, dword ptr [rdi+12];"
code += "jmp exit;"

code += "label2:"
code += "add eax, dword ptr [rdi+4];"
code += "sub eax, dword ptr [rdi+8];"
code += "sub eax, dword ptr [rdi+12];"
code += "jmp exit;"

code += "label1:"
code += "add eax, dword ptr [rdi+4];"
code += "add eax, dword ptr [rdi+8];"
code += "add eax, dword ptr [rdi+12];"
code += "jmp exit;"

code += "exit:"

code_asm = pwnlib.asm.asm(code)
chall.send(code_asm)

print(chall.recvall())
