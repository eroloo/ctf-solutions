### dont_be_salty

task is to brute-force salted password with known salt

I've decided to use JTR.

let's just edit john.conf file and add some code here


</br>[List.External:my_salt] 
</br>void filter()
</br>{
</br>	int i;
</br>
</br>// Find end of "word"
</br>	i = 0; while (word[i]) i++;
</br>
</br>// Hard-coded salt from http://www.openwall.com/lists/john-users/2008/02/01/1
</br>	word[i++] = 's'; 
</br>	word[i++] = 'a';
</br>	word[i++] = 'l';
</br>	word[i++] = 't';
</br>	word[i++] = 'h';
</br>	word[i++] = 'e';
</br>	word[i++] = 'r';
</br>	word[i++] = 'e';
</br>	word[i] = 0;
</br>}

**./john --external=salt_after --mask=?l?l?l?l?l --format=raw-md5 /ctf/BrixelCTF/dont_be_salty/hash** return key after few seconds