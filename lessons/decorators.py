def cough_dec(func):

    def func_wrapper():
        # code before function 
        print('*cough*')
        func()
        # code after function
        print('*cough*') 

    return func_wrapper

@cough_dec
def question ():
    print('can you give me a discount on that?')

@cough_dec
def answer():
    print("it's only 50p you cheapstake")

question ()
answer()

#Decorators extend the behavior of a function that is used of without modifying the function itself 
#Used in DJango 