import random
print("Welcome to Password Generator")
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['(',')','!','@','$','&','*','=','+','#','_']
list=[letters,numbers,symbols]
user_letters=int(input("How many letters would you like in your password?\n"))
user_numbers=int(input("How many numbers?\n"))
user_symbols=int(input("How many symbols?\n"))
password_list=[]
for i in range(user_letters):
    password_list.append(random.choice(letters))
for i in range(user_numbers):
    password_list.append(random.choice(numbers))
for i in range(user_symbols):
    password_list.append(random.choice(symbols))
password=''
random.shuffle(password_list)
for i in range(len(password_list)):
    password+=password_list[i]
print(f"Your password is: {password}")