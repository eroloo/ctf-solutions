## RECORDS

***
This is an easy one, what was the IP address in the first A record after we started using Cloudflare on our domain. 
*** (domain is securebug.se)

first of all, try using DIG

```dig securebug.se```


securebug.se.		300	IN	A	172.67.73.212

securebug.se.		300	IN	A	104.26.0.66

securebug.se.		300	IN	A	104.26.1.66


any of these ip's is correct answer. So I belive, that there was A record in the past and we should check DNS history.

portal ```securitytrails.com``` is good place to browse dns records history

 ![](https://i.ibb.co/PrfhpVK/Records.png)

flag SBCTF{104.27.128.155}
