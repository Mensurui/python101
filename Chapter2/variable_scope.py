#global variable 
my_global_variable = 10

def fn1():
    enclosed_variable = 5
   # print("trying to access the local variable from within the enclosed variable", locals_variable)
    def fn2():
        locals_variable = 1
        print("I can access global variables from anywhere and hence the following,",  my_global_variable)
        print("I can access enclosed variables from a local variable and hence the following,",  enclosed_variable)
        print("But for the local variables they can only be accessed from within a local function, ",  locals_variable)
    fn2()
    
fn1()