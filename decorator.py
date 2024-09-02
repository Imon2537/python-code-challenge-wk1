# it takes a function inside another function

    
    
def apply_decorator(func):
    def decorator_func():
        print("Decorator Applied")
        return func

    return decorator_func()

# decorator = apply_decorator(someFunc())
# print(decorator)


