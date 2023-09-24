my_sets = {1, 2, 3, 4, 5, 6, 7, 8, 9}

#unlike lists sets dont allow duplicates

print(my_sets)

#adding elements to a set
my_sets.add(10)
print(my_sets)

#removing elements from a set
my_sets.remove(10)
print(my_sets)

#or you can use the discard function
my_sets.discard(1)
print(my_sets)

#you can use the union function to combine multiple sets
my_sets2 = {7, 8, 9, 10, 11, 12, 13, 14, 15}
#instead of the union function you can simply use the | symbol
print(my_sets.union(my_sets2))

#you can use the intersection function to combine multiple sets
print(my_sets.intersection(my_sets2))
#instead of the intersection function you can simply use the & symbol

#to print all the elements that are in mysets but not in mysets2 you can use the difference function
print(my_sets.difference(my_sets2))
#you can use the minus (-) symbol instead

#to get all the elements that are in mysets and all the elements that are in mysets2 you can use the symetric function
print(my_sets.symmetric_difference(my_sets2))
#you can use the ^ symbol instead

#sets are not sequential and so you can not access them using indeces 
#ie print(mysets[0]) wont work