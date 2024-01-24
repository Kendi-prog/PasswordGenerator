import random
name = input('Enter name:')
print(f'Hello {name}.Welcome to Password Generator.')

password_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-|\?><:;"1234567890'
number_of_passwords = int(input('Enter the number of passswords you want to be generated: '))
password_length = int(input('Enter the length of each password: '))

print(f'Here are your Passwords {name}:')
for n in range(number_of_passwords):
    password = ''
    for l in range(password_length):
        password += random.choice(list(password_characters))
    print(password)