# FUNCTION FILTER, ratabo s failami, (REDUCE, LAMBDA)
#filter(func, iterable_object)
"""
def get_even_numbers(num): # filter rabotaet tolko true , prinimaet odin argument 
    if num % 2 == 0:
        return True
    else:
        return False

numbers = [x for x in range(1, 100)]
print(list(filter(get_even_numbers, numbers)))            
"""
"""
alphabets = ['a', 'b', 'c', 'd']
def filterVowels(alph):
    vowels = ['a', 'j', 'o', 's', 'c']
    if alph in vowels:
        return True
    else:
        return False

filteredVowels = list(filter(filterVowels, alphabets))
print(filteredVowels)        
"""

"""
products = ["Acer","Lenovo", "Hp", "Asus"]
def filterproducts(product):
    if product in products:
        return True
    else:
        return False

result = list(filter(filterproducts, ["Lenovo", "Macbook"]))
print(result)            
"""

# def genderFilter(obj):
#     people = {"John":"M", "Raychel":"F", "Sonya":"F","Ermek":"M","Bayan":"M"}
#     if obj in people.values():
#         return True
#     else:
#         return False    

# result = filter(genderFilter, ["M"])
# for x in result:
#     print(x)

"""
dictofNames = {
    7: "sam",
    8: "john",
    9:"mathew",
    10: "riti",
    11: "miki",
}
newDict = dict(filter(lambda elem: elem[0] % 2 == 0, dictofNames.items()))

print("Filtered Dictionary :")
print(newDict)
"""

# dictofNames = {
#     7: "sam",
#     8: "john",
#     9:"mathew",
#     10: "riti",
#     11: "miki",
#     12: "joni"
# }
# newDict = dict(filter(lambda elem: len(elem[1]) == 6, dictofNames.items()))

# print("Filtered Dictionary :")
# print(newDict) 

# people = {"John":"M", "Raychel":"F", "Sonya":"F", "Ermek":"M", "Bayan":"M"}
# newDict = dict(filter(lambda elem: elem[1] == "M", people.items()))
# print(newDict)
"""
people = {"John":"M", "Raychel":"F", "Sonya":"F", "Ermek":"M", "Bayan":"M"}
def genderFilter(elem):
    if elem[1] == "M":
        return True
    else:
        return False

newDict = dict(filter(genderFilter, people.items()))
print(newDict)
"""

# # Lambda anonimnye funcsiya , lambda arguments: expresion
# x = lambda a, b: a*b 
# print(x(5, 6))

# x = lambda a, b, c: a+b+c
# print(x(5,6,2))
"""
def sort_int(x):
    return int(x)

def sort_el(x):
    return x[-1]

data = ['21', '38', '45', '56', '88']
print(sorted(data, key = sort_int)) # 
print(sorted(data, key = sort_el)) # po vtoroi sigre sortirovali
"""

# data = ['21', '38', '45', '56', '88']
# print(sorted(data, key = lambda x: int(x)))
# print(sorted(data, key = lambda x: x[-1]))

# def multiply(a, b):
#     return a*b
# print(multiply(5, 6))    

# name_lengths = map(len, ['Masha', 'Raychel', 'Alibek'])
# print(list(name_lengths))

# squres = map(lambda x: x*x, [1,2,3,4,5])
# print(list(squres))
"""
#   METHOD REDUCE   # slojenie elementa s levo do konsa 
from functools import reduce

sum_ = reduce(lambda a, x: a+x, [1,2,3,4,5])
print(sum_)
"""

# i = lambda x, y: x if x < y else y
# print(i(1, 2))

list_ = [1, 2, 3, 4, 5]  # num - eto ravno vnutri lista 1,2,3,4,5
new_list = lambda list_: [num*5 for num in list_]
print(new_list(list_))


