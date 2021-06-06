***T3a_T1me***

*John lives in the UK and loves cream bisucits the most. Can you guess what he does not like?*
*John hates being rick-rolled*


On the webpage we need to answer for question and guess which kind of biscuits John doesnt like. In case of wrong answer user is redirected to /wrong page.


 ```curl -iL https://timeisthekey.herokuapp.com/wrong``` 

 result has one suspicious header:

 ```Set-Cookie: key=; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT```

what is more, I have notied that /flag path returns redirection.

After few hours I focues on ```John hates being rick-rolled``` hint and in connection with expired cookie header I have tried to set my cookie to

```key:RICKASTLEYLINK``` and acccess /flag path - it works!

 *John absolutely hates scones! Let them rot!
aaaAAA{aa15_1a_4_a00a13_a4a3}*

lets try to answer question by ```scones```
now flag seems possible to decode```spbYPB{pd15_1o_4_y00g13_c4i3}```




