# def fun(n):
#     if n == 0:
#         return
#     print(n)
#     fun(n-1)
#     print(n)
# number = int(input())
# res = fun(number)
# print(res)


# def fun(n):
#     if(n== 0):
#         return
#     fun(n-1)
#     print(n)
#     fun(n-1)
# number = int(input())
#
# res = fun(number)
# print(res)


# def fun(n):
#     # it uses log2(n) formula => 2^n values
#     # we can modify the base of log using other integers place of "2"
#     if(n==1):
#         return 0
#     else:
#         return 1 + fun(n//2)
#
# number = int(input())
# res = fun(number)
# print(res)

# def fun(n):
#     # it uses log3(n) formula => 3^n values
#     # we can modify the base of log using other integers place of "3"
#     if(n<3):
#         return 0
#     else:
#         return 1 + fun(n//3)
#
# number = int(input())
# res = fun(number)
# print(res)

# def fun(n):
#     # it returns binary equivalent of numbers..
#     if(n==0):
#         return
#     fun(n//2)
#     print(n%2,end="")
#
# number = int(input())
# res = fun(number)
# print(res)


# prints N to 1 natural numbers
# def fun(n):
#     if(n==0):
#  #       print(1)
#         return
#     else:
#         print(n,end=" ")
#         fun(n-1)
#
# number = int(input())
# fun(number)


# prints 1 to N natural numbers
# def fun(n):
#     if(n==0):
#         # print(1)
#         return
#     else:
#         fun(n-1)
#         print(n, end=" ")
#
# number = int(input())
# fun(number)

# factorial using tail recusion

# def fact(n,k):
#     if(n == 0 or n ==1):
#         return k
#     else:
#         return fact(n-1,k*n)
#
# res = fact(int(input()),1)
# print(res)

# generation of all substrings

# def generate_subsets(string, index, current, subsets):
#     if index == len(string):
#         subsets.append(current)
#         return
#     generate_subsets(string, index+1, current, subsets)
#     generate_subsets(string, index+1, current+string[index], subsets)
#
# subsets = []
# string = input()
# generate_subsets(string, 0, "", subsets)
# print(subsets)

# def rope_cutting_recursion(length, a, b, c):
#     if length == 0:
#         return 0
#     if length == 1:
#         return a
#     if length == 2:
#         return b
#     if length == 3:
#         return c
#     return max(rope_cutting_recursion(length-1, a, b, c), rope_cutting_recursion(length-2, a, b, c) + b, rope_cutting_recursion(length-3, a, b, c) + c)
#
# length = 5
# a = 1
# b = 5
# c = 2
# print(rope_cutting_recursion(length, a, b, c))

# tower of hanoi

# def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
#     if n == 0:
#         return
#     tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
#     print("Move disk", n, "from", from_rod, "to", to_rod)
#     tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)
#
# n = int(input())
# tower_of_hanoi(n, 'A', 'C', 'B')


# def permute(data, i, length):
#     if i == length:
#         print("".join(data))
#     else:
#         for j in range(i, length):
#             # swapping the ith and jth elements
#             data[i], data[j] = data[j], data[i]
#             permute(data, i + 1, length)
#             # backtracking
#             data[i], data[j] = data[j], data[i]
#
# string = input()
# n = len(string)
# a = list(string)
# permute(a, 0, n)

# Josephus problem
"""
The Josephus problem is a mathematical problem that describes a counting-out game where a
 group of people are arranged in a circle and a fixed number (usually called "step size")
 is used to count out and eliminate every nth person until only one person remains.
"""
# def josephus(n, k):
#     if n == 1:
#         return 1
#     else:
#         return (josephus(n - 1, k) + k-1) % n + 1
# n = int(input())
# k = int(input())
# print(josephus(n,k))












