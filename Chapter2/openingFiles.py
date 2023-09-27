
file = open('test.txt', mode='r')

data = file.read()

print(data)

file.close()

#OR even better

with open('test.txt', mode='r') as test:
    datum = test.readline()
print(datum)