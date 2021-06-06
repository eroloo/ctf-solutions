***ArchTic***

Can you help Nemo find the flag? Nemo loves a challenge—and a flag. 

link goes to dockerhub where we can pull a container

```docker pull madjelly8504/ctf_challenge```
```sudo docker run -it madjelly8504/ctf_challenge /bin/bash```

with bash attached and root privileges

```cat /root/.bash_history```

*
...
cd /usr/lib/python3.9/site-packages/libmount/cache/data/text/12.12.2021/strings/challenge_dir
...
*

in this directory 
```ls -a```
```cat .flag.txt```