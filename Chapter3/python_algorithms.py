
def palendrom_checker(line):
    number = len(line)
    is_palindrome = True

    for i in range(number // 2):
        if line[i] != line[number - i - 1]:
            is_palindrome = False
            break

    if is_palindrome:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

line = input("Please enter your words")
palendrom_checker(line)