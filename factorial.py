#this is a function to calculate the factors of a non-negative interger 
def factorialno(n):
    if n == 0:
        return 1
    else:
        return n * factorialno(n - 1)
    
factorial = factorialno(45)
print(factorial)