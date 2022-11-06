import hashlib

email ='jkr@gmail.com'
pwd = 'password'

pwd_encode = pwd.encode()
pwd_hash = hashlib.md5(pwd_encode).hexdigest()
# print(pwd_hash)

your_email ='jkr@gmail.com'
your_password = 'password'
hashed_your_password = hashlib.md5(your_password.encode()).hexdigest()

if email==your_email and pwd_hash==hashed_your_password:
    print('right password!')
else:
    print("No, it doesn't correct")



#Hacker Password:

hacker_email = 'jkr@gmail.com'
hacker_pwd = '5f4dcc3b5aa765d61d8327deb882cf99'

hashed_hacker_password = hashlib.md5(hacker_pwd.encode()).hexdigest()

if email==hacker_email and pwd_hash==hashed_hacker_password:
    print('right user!')

else:
    print('wrong password!')



