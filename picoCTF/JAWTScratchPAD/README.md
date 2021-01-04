## JAWT Scratchpad ( 400 points ) 

I belive that the task is pretty simple just to get familiar with JWT 

After gettin in page there is a form prompting for login; admin login returns 
**"YOU CANNOT LOGIN AS THE ADMIN! HE IS SPECIAL AND YOU ARE NOT"** 

I belive that task is to possess a cookie signed for admin credentials and authors suggest using john-the-ripper software 

What is important - default version of JTR from debian repositories (1.8.0) doesn't really support JWT so I decided to download [jumbo version](https://github.com/openwall/john).

### Solution

**1. login as 'test' user as an example and see that JWT cookie appeared in browser**

| ![](https://i.ibb.co/Zgg56rY/Zrzut-ekranu-z-2020-12-23-23-30-34.png?size=150)

**2. download a cookie** </br>
echo "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidGVzdCJ9.IAu_YSHppFe8hXH_BSPb4OLJYGUi8wXqXdS0T33cKbA" > cookie

**3. run john to crack propably easy key** </br>
sudo /opt/run./john --incremental:Lower cookie </br>
key is 'ilovepico' </br>

**4. sign a new cookie to admin credentials**
easy to do on official [JWT webpage](https://jwt.io/)
paste new cookie and upload a flag

| ![](https://i.ibb.co/ng2TZ9K/Screenshot-at-2021-01-04-17-45-53.png)
