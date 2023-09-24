my_tuples = (1, "string", 4.5, True)

print(my_tuples[3])
print(type(my_tuples))

#tells us the number of occurrences of the elements in the tuple
print(my_tuples.count("string"))

#tells us the index of the element
print(my_tuples.index(4.5))

#we can loop over the elements of the tuple too
for tuple in my_tuples:
    print(tuple)

#beware since unlike lists tuples are immutable

my_tuples[1] = 5