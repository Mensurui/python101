#Take an input from the user and append it to the dictionary
my_to_do_list = {}
c = int(input("How many to do list do you want to add: "))

for a in range(c):
    new_to_do_list = input("Write your todolists for today: ")
    my_to_do_list[a+1] = new_to_do_list

# Loop to print all items in the to-do list
for key, value in my_to_do_list.items():
    print(f"{key}: {value}")