# def square(number):
#     # print(number**2) use this one or below one
#     return number**2

# result = square(4)
# print(result)

#---------------------

# def add(n1,n2):
#     return n1+n2

# print(add(5,5))
# -----------

# def mul(p1,p2):
#     return p1*p2
# print(mul('a',5))
# print(mul(6,5))
# print(mul(5,'a'))
# --------------------

# import math
# def circle(Radius):
#        return math.pi * Radius **2
# print(circle(2))
# ------------------

# def greet(name):
#     return "hello, "+  name+"!"
# print(greet("user"))
# ------------------------

#lembda usecase :

# cube = lambda x: x**3    
# print(cube(3))
#----------------------------

# def sum_all(*args):
#     return sum(args)
# print(sum_all(1,2))
# print(sum_all(1,2,5,3,8))
# ------------------------------------------------------

# def sum_all(*args):
#     for i in args:
#         print(i*2)
#     return sum(args)
# print(sum_all(1,2))
# print(sum_all(1,2,5,3,8))
#--------------------------
# def print_kwargs(name,city):
#     print(name,city)
# print_kwargs(name="mahek",city="mumbai")
# -------------------------------------

# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")
# print_kwargs(name="mahek",city="mumbai")
# print_kwargs(name="mahek")
# print_kwargs(name="mahek",city="mumbai",enemy="sara")
# ------------------------------------------------------------

# def even_gen(limit):
#     li = []
#     for i in range(2,limit+1,2):
#         li.append(i)
#     return li
         
# print(even_gen(10)) 
# ----------------------------------------------------------------------------------------------

#yeild : 

# def even_gen(limit):
#     for i in range(2,limit+1,2):
#          yield i
         
# for num in even_gen(10):
#      print(num)
# ----------------------------------------------------

#recursive for factorial 
def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))