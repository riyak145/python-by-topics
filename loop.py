# numbers = [1,-2,3,-4,5,-6,7,-8,9,10]
# positive_num = 0
# for num in numbers:
#     if num>0:
#         positive_num +=1       
# print(positive_num)            
#------------------

# n=10
# sum_even = 0
# for i in range(1,n+1):
#     if i%2 ==0:
#         sum_even += 1
# print(sum_even)

#----------
#table 
# num = 3
# for i in range(1,11):
#     if i==5: #it will skip 5 and continue
#         continue
#     print(num,'x', i , '=' , num *i)
# ---------------


#reversed 
# str = "python"
# reverse = ""
# for char in str:
#     reverse = char + reverse 
# print(reverse)
# -------------------

# str = "teetrabcabc"
# for char in str:
#     print(char)
#     if str.count(char) == 1:
#         print("char",char)
#         break
#--------------------

#factorial
# num = 5
# factorial = 1

# while num >0:
#     factorial = factorial*num
#     num = num - 1
# print(factorial)
#---------------------

# while True:
#     num = input("value 1 to 10 ")
#     num = int(num)
#     if 1 <= num <= 10:
#         print("yes")
#         break
#     else:
#         print("nope")
#----------------

#prime
# num = 14
# is_prime = True
# if num > 1:
#     for i in range (2,num):
#         if (num % i) ==0:
#             is_prime = False
#             break
# print(is_prime)
#------------------


items = ["apple","banana","orange","apple"]

unique_item = set()
for item in items:
    if item in unique_item:
        print("dup",item)
        break
    unique_item.add(item)