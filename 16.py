def my_function():   #x is a local variable.
    x=10
    print(x)
my_function()


x=10     # x is a global variable
def my_function():
    print(x)
my_function()


x=10 #global variable
def modify_global():
    global x # non-local scope variable . by using global keyword
    x=20
    
modify_global()
print(x)
