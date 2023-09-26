sample_dict = {1:'Coffee', 2:'Tea', 3:'Juice'}
print(sample_dict[1])
#to change the value
sample_dict[2] = 'Mint tea'
print(sample_dict[2])

#to delete a value in the dictionary
del sample_dict[3] 

my_dict = {1:'Football', 2:'Baseball', 3:'Basketball'}

for key, value in my_dict.items():
    print(str(key) + ":" + str(value))