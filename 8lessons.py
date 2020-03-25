"""
# FUNCTION ABS()

number = -123
abslolute_value = abs(number)
print(abslolute_value)
"""
"""
# FUNCTION ALL() dlya sravnenie 
iterable_object = [1, 2, 3, 4, 5]
print(all(iterable_object))
iterable_object = [1, 2, 3, 4, 0]
print(all(iterable_object))
"""

"""
iterable_object = [1, 2, 3, 4, 0]
print(all(iterable_object))

def all_(iter):
    for x in iter:
        if not x:
            return False
    return True
print(all_([1, 2, 3, 4, 5]))            
"""

# # FUNCTION ANY()
# tuple_ = ("","","")
# print(any(tuple_))

"""
# FUNCTION BOOL(1) prinimaet odin obekt, 
print(bool(0))
print(bool(1))
print(bool([]))
print(bool([0]))
print(bool([]) == False)
"""

"""
# FUNCTION ASCII / kojdaya bukva oznachaet sifry 
example = ascii("krilicsu") #na ruskom 
print(example)
"""
"""
# FUNCTION CALLABLE  # vyzyvaemyi 
def adder(n1, n2):
    return n1 + n2
is_callable = callable(adder)
print("Function is callable: ", is_callable)    
"""
"""
# FUNCTION CHR() uni kod po imeni koda
print(chr(77))
print(chr(56))
"""
"""
# SLUG = "friendly url"
https://example.com/first_ofstep_programming/
https://example.com/second_ofstep_programming/
https://examole.com/1/
pervaya novost
"""
"""
# FUNCTION DIVMOD()
print(divmod(12, 5))
print(divmod(10, 5))

a, b = divmod(12, 5) #mnojestvo
print(a)
print(b)
"""
"""
def add(a, b):
    return a+b

def test_add():
    result = add(12, 6)
    assert result == 18
    print("Okey")
test_add()
"""
# TDD 
# def test_multiple():
#     result = test_multiple(12, 2)
#     assert result == 24

# # decimal divmod
# #float()
# from decimal import Decimal
# import math
# print(math.pi)
"""
# FUNCTION ENUMERATE()
seasons = ["Spring", "Summe", "Fall", "Winter"]
new = list(enumerate(seasons))
print(new)
"""

# # FUNCTION MAP()
# numbers = ["1","2","3","4","5"]
# print(numbers)
# new_numbers = list(map(int, numbers))
# print(new_numbers)

# def uppercase(char):
#     return char.upper()

# list_ = ["a","b","c"]
# new_list = list(map(uppercase, list_))
# print(new_list)
"""
def map_(func, iterable_object):  
    new_list = []
    for num in iterable_object:
        new_list.append(func(num))
    return new_list

print(map_(int, ["5","10","12"]))
"""

# def generate_link(link):
#     base_url = "https/example.com"
#     return base_url + link

# print(list(map(generate_link, ["/hello/world/kg","world/hello/kg"])))




