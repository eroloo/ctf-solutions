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
    xor rax, rax
    mov r10, 0x0
    mov r9, 0x0
    check:
    cmp r9, rsi
    je end
    adding:
    add r10d, dword ptr [rdi + 0x4 * r9]
    add r11, r10
    xor r10d, r10d
    inc r9
    jmp check
    end:
    mov rdx, 0
    mov rax, r11
    div rsi """

code_asm = pwnlib.asm.asm(code)
chall.send(code_asm)

print(chall.recvall())
