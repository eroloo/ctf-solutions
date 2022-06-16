file rev4

rev4: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=afd81de432060b7e6382aa9c69eccefd597beed1, for GNU/Linux 3.2.0, not stripped

after making binary executable it asking for the key and give message "Access denied" after providing key. 

1. Opening file in GHIDRA
2. High level overview of main() function
	- ask for key
	- encode() user input
	- compare to bytes in memory

![Alt text](/AccessDeniedCTF2022/binary/main-ghidra.png?raw=true "Title")

3. Dig into encode() function
	- 11 line = get rand() value which will be the same during every execution of program
	- 12 line = uVar3 will be null in every scenario becouse rand() is no longer than (0xff + 0x2) bytes (tested in test.c file)
	- 13 line in shorcut is iVar2 = user_input & 0x3fffffff becouse iVar3 is null
	- 14 line = iVar1 is also null becouse iVar2 is maximum 32 bits in length in default. (MAX_RAND value + 255) & 3fffffff > 0 
	- 15 line is byte = byte & 7f
![Alt text](/AccessDeniedCTF2022/binary/encode-ghidra.png?raw=true "Title")


general idea:
	byte in memory = user_byte + rand() & 0x3fffffff & 0x7f
reverse idea:
	user_byte = byte in memory - rand() & 0x3fffffff & 0x7f

code: 
```
# Python
import random

# bytes from program memory
ans_encoded = ["48", "29", "4c", "58", "44", "72", "2e", "51", "17", "36", "1f", "0f", "6d", "5e", "16", "7a", "6f",
               "75", "46",
               "57", "7e", "19", "57", "75", "29", "4c", "0d", "14", "68", "7e", "3b", "4d", "1a", "1e", "79", "30",
               "10", "3b",
               "53", "0a", "11", "3c", "66", "78", "0e", "1d", "0f", "36", "60", "66", "4a"]

# random numbers generated in C loop
random_numbers = [1804289383, 846930886, 1681692777, 1714636915, 1957747793, 424238335, 719885386, 1649760492,
                  596516649, 1189641421, 1025202362, 1350490027, 783368690, 1102520059, 2044897763, 1967513926,
                  1365180540, 1540383426, 304089172, 1303455736, 35005211, 521595368, 294702567, 1726956429, 336465782,
                  861021530, 278722862, 233665123, 2145174067, 468703135, 1101513929, 1801979802, 1315634022, 635723058,
                  1369133069, 1125898167, 1059961393, 2089018456, 628175011, 1656478042, 1131176229, 1653377373,
                  859484421, 1914544919, 608413784, 756898537, 1734575198, 1973594324, 149798315, 2038664370,
                  1129566413, 184803526]

for i in range(len(ans_encoded)):
    after_encoding = str("0x") + str(ans_encoded[i])
    after_encoding_int = int(after_encoding, 16)
    before_encoding_byte = after_encoding_int - random_numbers[i] & 0x3fffffff & 0x7f

    print(chr(int(before_encoding_byte)), end='')
print("\n")
```



