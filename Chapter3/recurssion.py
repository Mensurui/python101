def find_solution_reccurssion(n):
    if n == 1:
        return 1
    else:
        return n * find_solution_reccurssion(n-1)
    
print(find_solution_reccurssion(4))