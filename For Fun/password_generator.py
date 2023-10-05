import random

pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'G', 'H', 'I', '1', '2', '3', '@', '#', '!', 'l', 'm', 'n', 'F', 'G', 'H', 'I',
         '\n', 'z', 'a', 'b', 'c', 'd', 'e', 'M', 'n', 'F', 'G', 'H', 'I', '1', '2', '3', '(', '}', '/'
         ]

password = ""

for x in range(10):
    password = password + random.choice(pass1)

print("\033[92mYour new password: " + "\033[31m" +password + "\033[0m")


'''
Black: \033[30m
Red: \033[31m
Green: \033[32m
Yellow: \033[33m
Blue: \033[34m
Magenta: \033[35m
Cyan: \033[36m
White: \033[37m
'''
