def dot_product(list1, list2):
    len1, len2 = len(list1), len(list2)
    
    if len1 < len2:
        list1 += [0] * (len2 - len1)
    elif len1 > len2:
        list2 += [0] * (len1 - len2)
    
    result = 0
    for i in range(max(len1, len2)):
        result += list1[i] * list2[i]
    print(result)
    return result

    
    
    
list1 = input('Enter the components of the first vector: ')
list2 = input('Enter the components of the second vector: ')

list1 = [int(x) for x in list1.split()]
list2 = [int(x) for x in list2.split()]

dot_product(list1, list2)

    
    
#take a list of numbers i.e list1, list2
#next access the numbers in the list
#now add the numbers and get a scalar result
 