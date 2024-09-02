# function for adding numbers
def add(num1, num2):
    return num1 + num2

sumation = add(23, 65)
print(sumation)



# function for checking if a number is even
def even(number):
    return number % 2 == 0

even_num = even(99)
print(even_num)




# function to return a reversed version of a string
def reverse_string(text):
    return text[::-1]

reverse = reverse_string('mwenda')
print(reverse)



# it returns the number of vowels
def totalVowels(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

count = totalVowels("randervous")
print(count)


#this is a function to calculate the factors of a non-negative interger 
def factorialno(n):
    if n == 0:
        return 1
    else:
        return n * factorialno(n - 1)
    
factorial = factorialno(45)
print(factorial)


# it takes a function inside another function
def apply_decorator(func):
    def decorator_func():
        print("Decorator Applied")
        return func()

    return decorator_func

decorator = apply_decorator(someFunc())
print(decorator)




# this function sorts different tuples 
def sort_by_age(tuples):
    return sorted(tuples, key=lambda x: x[1])

myList = sort_by_age(('ian', 23), ('caleb', 22))
print(myList)



# this funcs combines two dictionaries and mergers them into one
dict1 = {
    'car': 'subaru',
    'model': 'forester'
}
dict2 = {
    'car': 'rolls royce',
    'model' : "cullinan"
}
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

merge = merge_dicts(dict1, dict2)
print(merge)






# this function creates a class that prints out a cars information
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}")
        
obj1 = Car(2002, "corona", "brandy")
print(obj1)