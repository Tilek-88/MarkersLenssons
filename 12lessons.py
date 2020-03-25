#  RECURSION (rekursiya)

"""
def some_func():
    x = int(input("Write number: "))
    if x == 0:
        return 0
    print(x)
    some_func()


some_func()    
"""
"""                 #prostoi rekursiya
def privet(n):
    if n == 0:
        return 0
    else:
        print("hello world")
        return privet(n-1)  # privet(3-1) #privet(2-1) #privet(1-1) = 0 ne budet s rabotavat

privet(3)
"""

# result = [x for x in range(1, 101)]
# print(sum(result))

# result = [1, 2, 3, 4, 5]
# print(sum(result))
"""
def sum_(x):
    if x == 0:
        return 0
    else:
        return x + sum_(x-1)
        # 5 + sum_(5-1), # 4 + sum_(4-1)
        # 3 + sum_(3-1), # 2 + sum_(2-1), 
        # 1 + sum_(1-1), # 1 + 0

        # 3+sum_(3-1)  2+sum_(2-1)  1+sum_(1-1)
print(sum_(3))            
"""

# def factorial(num):
#     if num in [0, 1]:
#        return 1

#     else:
#         return factorial(num-1)*num 
#     #factorial(3-1)*3, factorial(2-1)*2,  factorial(1)

# print(factorial(3))        
"""
def count(n):
    print(n)
    if  n==0:
        return

    else:
        count(n-1)

count(5)
"""
def reverse():
    n = input()
    if n!="q":
        reverse()
        print(n)
    

reverse()            







