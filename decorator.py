# it takes a function inside another function


    
    
def apply_decorator(func):
    def decorator_func():
        print("Decorator Applied")
        return func

    return decorator_func()()


@apply_decorator
def myFunc():
    print("this is a function")
# decorator = apply_decorator(someFunc())
# print(decorator)


