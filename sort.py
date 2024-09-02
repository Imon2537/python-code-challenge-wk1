# this function sorts different tuples 
def sort_by_age(tuples):
    return sorted(tuples, key=lambda x: x[1])

myList = sort_by_age(('ian', 23), ('caleb', 22))
print(myList)

