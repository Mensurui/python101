def divide(a,b):
    return a / b


try:
    ans = divide(4, 2)
    print (ans)
except  ZeroDivisionError as e:
    print(e, "Division failed due to ZeroDivisionError")
except Exception as e:
    print(e, "Division failed due to Exception ")
    
items = [1,2,3,4,5]
try: 
    ans = items[2]
    print(ans)
except IndexError as e:
    print(e, "Could not find the number due to IndexError Exception")
except Exception as e:
    print(e, "Could not find the number due to an Exception")