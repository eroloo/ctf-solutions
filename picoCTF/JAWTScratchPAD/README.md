## JAWT Scratchpad ( 400 points ) 

I belive that the task is pretty simple just to get familiar with JWT 

After gettin in page there is a form prompting for login; admin login returns 
**"YOU CANNOT LOGIN AS THE ADMIN! HE IS SPECIAL AND YOU ARE NOT"** 

I belive that task is to possess a cookie signed for admin credentials and authors suggest using john-the-ripper software 

What is important - default version of JTR from debian repositories (1.8.0) doesn't really support JWT so I decided to download [jumbo version](https://github.com/openwall/john).

### Solution

**login as 'test' user as an example and see that JWT cookie appeared in browser**

| ![]https://ibb.co/dppF0vL?size=150

**download a cookie**
echo "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidGVzdCJ9.IAu_YSHppFe8hXH_BSPb4OLJYGUi8wXqXdS0T33cKbA" > cookie

**run john to crack propably easy key**
sudo /opt/run./john --incremental:Lower cookie
key is 'ilovepico'

**sign a new cookie to admin credentials**
easy to do on official [JWT webpage](https://jwt.io/)
paste new cookie and upload a flag

| ![]https://ibb.co/0DNk8Tz?size=150
