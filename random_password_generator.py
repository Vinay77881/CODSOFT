import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
         'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
         'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',
         'T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','_','+']
print("Welcome to password generator")
total_chars=int(input("How many symbols do you need in your password?\n"))
password_list=[]
for i in range(total_chars):
    password_list.append(random.choice(letters + numbers + symbols))
random.shuffle(password_list)
password=""
password = ''.join(password_list)
print(f"The generated password is: {password}")