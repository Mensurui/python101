def divide(a,b):
    return a / b


try:
    ans = divide(4)
    print (ans)
except  ZeroDivisionError as e:
    print(e, "Division failed due to ZeroDivisionError")
except Exception as e:
    print(e, "Division failed due to Exception ")