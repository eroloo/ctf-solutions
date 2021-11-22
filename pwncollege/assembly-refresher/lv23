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
    mov rbp, rsp
    sub rsp, 0xff
    mov rbx, 0x0    #b
    mov r11, 0x0    #i 
    mov rcx, rsi
    dec rcx
    nop #rsi size
    nop #rdi src address
    
    for1:
    cmp r11, rcx   #1st for cmp incremented r11 to size-1
    jg exit1for
        xor r13, r13
        mov r13b, byte ptr [rdi+r11]
        mov r12, rbp
        sub r12, r13
        inc byte ptr [r12] #increment byte on stack
        inc r11
    jmp for1
    
    exit1for:
    mov r12, 0x0    #max freq byte
    mov r10b, 0x0    #max freq
    xor rbx, rbx
    xor rcx, rcx
    mov rbx, 0x1
    for2:
    cmp bl, 0xff   # if bl = 0xff stop program jmp exitfor
    je exitfor2
        if2:
        mov rcx, rbp
        sub rcx, rbx
        cmp byte ptr [rcx], r10b   # r u max freq byte
            jle exitif
            mov r10b, byte ptr [rcx]   # most freq
            mov r13, rbp
            sub r13, rcx
            exitif:
        inc bl
    jmp for2

    exitfor2:
    mov rax, r13
    mov rsp, rbp
    ret
"""
code_asm = pwnlib.asm.asm(code)
chall.send(code_asm)

print(chall.recvall())
