#!/bin/bash
res=$(curl -X GET -c cookie http://timesink.be/quizbot/index.php)
while read line; do
    res=$(curl -X POST -F "insert_answer=${line}" -b cookie -L http://timesink.be/quizbot/index.php)
    echo $(echo $res | hxclean | hxselect body:first-child)
done < answers 
#send last
line='el greco'
res=$(curl -X POST -F "insert_answer=el greco" -b cookie -L http://timesink.be/quizbot/index.php)
echo $res
#get flag I belive