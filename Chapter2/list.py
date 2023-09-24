list1 = [1, 2, 3, 4, 5, 6]

# to add 
list1.insert(0,7)
print (list1)

list1.extend([8,9,10])
print (list1)

list1.append(11)
print (list1)

# to remove
list1.pop(0)
print(list1)

del list1[0]
print (list1)

#iterate over a list
for x in list1:
    print ("Value: ", x)