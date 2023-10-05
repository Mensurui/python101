import random
pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'G', 'H', 'I', '1', '2', '3','@','#','!', 'l', 'm', 'n', 'F', 'G', 'H', 'I','\n'
         'z', 'a', 'b', 'c', 'd', 'e','M', 'n', 'F', 'G', 'H', 'I', '1', '2', '3,','(','}','/'
         ]

password = ""

for x in range(10):
    password = password + random.choice(pass1)[0]
    
print("Your new password: " + password)