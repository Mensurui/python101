def appendNum(lst, item):
    nl = lst.copy()
    nl.append(item)
    print(nl)
lst = [1,2,3,4]
print(lst)
print(appendNum(lst, 5))