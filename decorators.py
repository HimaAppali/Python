# decorator is a function that takes other function as input and gives modilfied version
def announce(f):
    def wrapper():
        print('function about to start')
        f()
        print('function ended')
    return wrapper

# hello function is used as wrapper function and wrapped inside the announce function
@announce
def hello():
    print('hello world')

#call hello function
hello()