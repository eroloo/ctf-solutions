## Knock Knock

*** 
We recently found a private SSH key that will allow us to login in the attached machine.

However, we can't seem to be able to login through SSH.

Can you help us out?

No brute force is required.
***

.ova and id_rsa.key files are available for download. 

TLDR
register ova on VB
scan for open ports
login by ftp (knocking for ssh)
nc on 7000,8000,9000 ports 
generate pub.key from priv.key from description
login by username from public key



After downloading a registering .ova on virtualbox I have tried some default login/password but none of known works. 
I belive that we have to connect to Virtual Machine by network so lets create a NAT network with DHCP Server on virtual box 
![](https://i.ibb.co/hFKLfXZ/dhcp.png)

so the address of VM is 192.168.56.101 now and we can scan some ports. Result of nmap is open 21/FTP port. After connection we can download a flag file but it is fake flag.

![](https://i.ibb.co/tZNF8gN/ftp.png)

Taking hint into consideration we can perform knocking by:
```
nc -v 192.168.56.101 7000

nc -v 192.168.56.101 8000

nc-v 192.168.56.101 9000
```

After that additional scanning shows 22/ssh open port so that was a port-knocking. 

We have a key so I have unsuccesfully tried to login by 
```ssh -i key_from_desc 192.168.56.101 ```

but it doesnt work. My thought was to retrive some public key from private by command

```ssh-keygen -y -f ~/.ssh/id_rsa > ~/.ssh/id_rsa.pub```

and that works 

```ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDWX0ICjTiJP6pGEojST+D77hFFmH06No5HOZIdC9+XMLB6ZO1lJRuWkF0qf/UEqyj7Xbb/ZW6q832y5fHPHm0m0EuZVG2kiC83XFECe9NHQNY18HSVUtfAtbKpbQIUmp7a3bayrmM6+iE/aZpSa1RFXHICcfqt6WQeF2EnKRT8aEdt4Ozoc8Ab3gdBMDftqFZsKa6tP3WLNRzkETOrTzAErn5O3CgprYFlz9JO2d7Ca0+nosEvVoYGBQrKQaMkkkWzaTtTsVAU37QN7a7YFXDjdd2CClPJTH93Y/XmTcNDPAHlpf9v4oxfe8CRgh9CWFM8rKuY8vS1yHc7TR/3kXILqP1949OUxscynJ4wPgyhL0IK5shoy4oJGwawrILQN5AFsm4UyS7uRIaFC/UuChBx7T5lDvKJqsuscvw37h5HulFH7i6AVk0msz393zco/ZPHHFlB88weMMFRlecDVTzZdoKVPtkuL21uM+v+CqQ3CwTEOC08b7OClEvWuH1gB8M= ctf@knockknock```

now we have an username so ``` ssh -i key_from_desc ctf@192.168.56.101 works, flag is in / directory. ```
