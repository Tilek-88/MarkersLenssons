"""
#oblast vidimosti peremennyh v funcsiyah
this_var_is_visible = "can be seen inside and outside function"

def var_visibility():
    this_is_not_visible ="cannot be seen outside function"
    print(this_is_not_visible)
    return
var_visibility()

print(this_var_is_visible)
#print(this_is_not_visible)
"""
# def func(a, b):
#     # a =12
#     # b =14
#     return a+b
# func(12, 14)   

# def some_func(name):
#     print(locals())
# some_func("tilek")   
 
# name = "Asus"
# name = "HP"
# print(name)

# name = "Asus"
# def get_name():
#     name = "Hp"
#     return name
# print(get_name()) 
# print(name)   

# def get_information():
#     name = ["John", "Baha", "Ermek"]
#     age = 18
#     print(locals())
# get_information()  

"""
name = "Reychel"
def get_name():
    name = "John"
    age = 18
    print("funcsiya get_name() ego pronstranstvo: ", locals())

print("Vnewnee prostranstvo imeni: ", locals())
get_name()  
"""
# name = "Lenovo"
# def func_one():
#     #name = "func_one()"
#     def func_two(): # zamknutyi 
#         #name = "Acer"
#         print(name)
#         print(locals())

#     func_two()

# func_one()

# LEGB 
# L = local
# E = enclosed
# G = global
# B = Built-ins 





