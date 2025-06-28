import random

def generate_password(main_password: str, num: int):
    # Characters that will be used in the password
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    # Checking the length of the main password and the length of the password
    if len(main_password) < 6 or len(main_password) > 12:
        raise ValueError("Password must be between 6 and 12 characters long.")
    if num < 6 or num > 12:
        raise ValueError("Password length must be between 6 and 12 characters long.")
    # Select 3 random characters from the main password
    random_main = random.sample(main_password, 3)
    # We glue 3 random symbols with the rest of the random symbols.
    base = random_main + [random.choice(chars) for _ in range(num - len(random_main))]
    # Mix the characters and highlight the main password.
    highlighted = []
    for char in base:
        if char in random_main:
            highlighted.append(f"\033[1;32m{char}\033[0m")  
            random_main.remove(char)  
        else:
            highlighted.append(char)
    
    base = highlighted
    random.shuffle(base)
    password = ''.join(base)

    return password


print('''
Password Generator
==================
''')

main_password = str(input('Enter the main password: '))
num = int(input('Password lenght: '))
print(generate_password(main_password, num))
