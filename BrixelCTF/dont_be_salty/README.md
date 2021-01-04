##dont_be_salty

task is to brute-force salted password with known salt

I've decided to use JTR.

let's just edit john.conf file and add some code here


[List.External:my_salt]
void filter()
{
	int i;

// Find end of "word"
	i = 0; while (word[i]) i++;

// Hard-coded salt from http://www.openwall.com/lists/john-users/2008/02/01/1
	word[i++] = 's';
	word[i++] = 'a';
	word[i++] = 'l';
	word[i++] = 't';
	word[i++] = 'h';
	word[i++] = 'e';
	word[i++] = 'r';
	word[i++] = 'e';
	word[i] = 0;
}

**./john --external=salt_after --mask=?l?l?l?l?l --format=raw-md5 /ctf/BrixelCTF/dont_be_salty/hash** return key after few seconds