num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39, 53, 67, 89, 11]

count = 0
#changing the place of the two iterators i.e. index and number will alter how the code is supposed to work...
for index, number in enumerate(num_list):
    count += 1
    if number > 45:
        print("Numbers over 45:", number)
    else:
        print("Numbers under 45:", number)
    if number == 36:
        print("Number found at position:", index)
        break
        
print(count)

    