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
    mov r13, 0x403000                                     # foo() addrr
    mov rax, 0x0                                          # from desc
    cmp rdi, 0x0
    je endif
    
    whileloop:
        cmp byte ptr [rdi], 0x0
        je endwhile
            cmp byte ptr [rdi], 0x5a                      # if [src] <= 90
            jg rdiadd
                push rax                                   #added
                push rdi
                mov dil, byte ptr [rdi]
                call r13
                pop rdi                                # call foo with param in dl
                mov  byte ptr [rdi], al                 # set lowered character
                pop rax
                inc rax
            rdiadd:
            inc rdi
    jmp whileloop
    endwhile:
        
    endif:
        ret
"""
code_asm = pwnlib.asm.asm(code)
chall.send(code_asm)

print(chall.recvall())
