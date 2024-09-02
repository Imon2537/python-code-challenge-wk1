# this function sorts different tuples 
def sort_by_age(tuples):
    return sorted(tuples, key=lambda x: x[1])

tuple1 = ('ian', 20)
tuple2 = ('caleb', 24)
myList = sort_by_age((tuple1,tuple2))
print(myList)

