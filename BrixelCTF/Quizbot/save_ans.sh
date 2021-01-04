#!/bin/bash

res=$(curl -X POST -F 'insert_answer=test' -c cookie http://timesink.be/quizbot/index.php)
ans=$(echo $res | hxclean | hxselect -c "#answer")
echo $ans >>answers

#possess a cookie
for (( i=1; $i <= 1000 ; i++ ));
do
 res=$(curl -X POST -F 'insert_answer=test' -b cookie -L http://timesink.be/quizbot/index.php)
 ans=$(echo $res | hxclean | hxselect -c "#answer")
 echo $ans >> answers
done




