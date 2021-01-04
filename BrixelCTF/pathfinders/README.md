##pathfinders#1

**205 solves**

seems like [pathfinders page](http://timesink.be/pathfinder/index.php?page=admin/.htpasswd) uses basic http auth so let's try to find .htpasswd file by unsecured include php function 


what will page return by this request? 
http://timesink.be/pathfinder/index.php?page=admin/.htpasswd


flag: brixelCTF{unsafe_include} 