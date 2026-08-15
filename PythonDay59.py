# Decorators in Python    


# Python decorator is a design pattern that allows 
# you to modify or extend the behavior of a function 
# or method without permanently altering its actual 
# source code.

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Mornign!")
        fx(*args, **kwargs)
        print("Thanks for using this function!")
    return mfx
        

@greet
def hello():
    print("Hello  World!")
 
    
@greet   
def add(a, b):
    print(a+b)

hello()
print("\n")
add(5,2)
















































