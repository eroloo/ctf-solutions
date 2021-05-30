from pwn import *

flag=""
items = ["Correct!"]
count = 1 # do ciagu counter
nterms=100#max do ciagu
fibotable =[]
n1 = 1
n2 = 2
strr = ""
ans1="1"
ans2=""
flag_catched=0

while count < nterms:
    fibotable.append(n1)
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    count += 1
print(f"fibo table to {fibotable}")

r = remote('umbccd.io', '6000')

while ans1:
   # r.recvline_contains(items, keepends=False, timeout=pwnlib.timeout.Timeout.default) # recv Correct answer!
    numbers=r.recvline_startswith("[", keepends=False, timeout=1) # line contains a bytes table of numbers in task
    if numbers==b'':
        flag=r.recvline()
        print(flag)
        flag=r.recvline()
        print(flag)
        flag=r.recvline()
        print(flag)

    tasknumbers=str(numbers,'utf-8').replace("[", "").replace(" ", "").replace("\n", "").replace("]", "").split(",")

    for number in tasknumbers:
        if int(number) in fibotable:
            strr = f"{number}"
            r.sendline(strr)
            print(f'Liczba {number} jest fibo')
