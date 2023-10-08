# str[start:stop:step]
#Extended slice syntax start and stop are indeces in which the function manipulates the strings the step parameter
#is where the the function jumps while it traverses the given string 

trial = "reversal"
new_trial = trial[2:5:-1]
print(trial)
print(new_trial)

# now using recursion

def string_reverse(str):
    if len(str) == 0 :
        return str
    else:
        print(str)
        return string_reverse(str[1:]) + str[0]

    
str ="Mensur"
reverse = string_reverse(str)
print(reverse)

