# Bitwise Algorithms
# a = 10
# b = 45

# print(a&b)
# print(a^b)
# print(a|b)
# print(~a)
#
# print(a<<4) # --- a * pow(2,4)
# print(b>>2) # --- a * 1/ pow(2,2)

# How to Set a bit in the number?

# def setBit(a , pos):
#     a |= (1 << pos)
#     print(a)
# a = int(input())
# pos = int(input())

# setBit(a , pos)

# How to unSet a bit in the number?

# def UnsetBit(a,pos):
#     a &= (~(1 << pos))
#     print(a)
# a = int(input())
# pos = int(input())
#
# UnsetBit(a , pos)


# Toggling a bit at nth position

# def Toggle(a , pos):
#     a ^= (1 << pos)
#     print(a)
# a = int(input())
# pos = int(input())
#
# Toggle(a,pos)


# Count Set bits in an integer

# def CountSetBits(num):
#     count = 0
#     while(num):
#         count += num & 1
#         num >>= 1
#     return count
#
# num = int(input())
# print(CountSetBits(num))

# num = int(input())
# print(bin(num)[2:].count('1'))

# Count unSet bits in an integer

# def CountUnsetBits(num):
#     count = 0
#     update = 1
#     while(update < num +1):
#         if(num & update == 0):
#             count += 1
#         update <<= 1
#     return count
#
# num = int(input())
# print(CountUnsetBits(num))

# num = int(input())
# print(bin(num)[2:].count('0'))

# Binary representation of a given number

# def Binary(num):
#     string = ''
#     if(num > 1):
#         Binary(num // 2)
#     string = string + str(num % 2)
#     print(int(string) , end="")
#
# num = int(input())
# Binary(num)

# def Binary(num):
#     string = ''
#     if(num > 1):
#         Binary(num >> 1)
#     string = string + str(num & 1)
#     print(int(string) , end="")
#
# num = int(input())
# Binary(num)

# num = int(input())
# res = int(bin(num)[2:])
# print(res)

# def Octal(num):
#     string = ''
#     if(num > 1):
#         Octal(num // 8)
#     string = string + str(num % 8)
#     print(int(string) , end="")
#
# num = int(input())
# Octal(num)

# num = int(input())
# res = int(oct(num)[2:])
# print(res)

# num = int(input())
# res = hex(num)[2:]
# print(res)

# # decimal representation of a given binary number

# Binary = input()
# res = int(Binary, 2)
# print(res)

# # decimal representation of a given octal number

# Octal = input()
# res = int(Octal, 8)
# print(res)

# # decimal representation of a given Hexi number

# Hexi = input()
# res = int(Hexi, 16)
# print(res)

# adding to binary string return result in binary string ..

# first = input()
# second = input()
# def add_binary_strings(a, b):
#     return '{:b}'.format(int(a,2) - int(b,2))
# print(add_binary_strings(first,second))

# adding to binary string return result in decimal ..

# first = input()
# second = input()
# third = input()
# def add_binary_strings(a, b , c):
#     return '{:d}'.format(int(a,2) + int(b,2) + int(c,2))
# print(add_binary_strings(first,second,third))

"""
here , from above example we can add two binary string and
return value in any bases
"""

# Turn off the rightmost set bit
# def fun(n):
#     return n & (n - 1)
# n = int(input())
# print("The number after unsetting the rightmost set bit", fun(n))

# Find the Number Occurring Odd Number of Times

# L = list(map(int,input().split()))
# L2 = []
# for i in L:
#     L1  = L.count(i)
#     if(L1 % 2 != 0):
#         L2.append(i)
#     else:
#         pass
# s = set(L2)
# print(*s)

# find whether a given number is power of 2
# num = int(input())
# import math
# if(math.floor(math.log2(num)) == math.ceil(math.log2(num))):
#     print("Yes")
# else:
#     print("No")

# find whether a given number is power of 3
# num = int(input())
# import math
# if(math.floor(math.log(num,3)) == math.ceil(math.log(num,3))):
#     print("Yes")
# else:
#     print("No")

# if (n <= 0):
#     return False
# if (1162261467 % n == 0): here constraints matters!!
#     return True
# else:
#     return False

# num = int(input())
# if(num != 0 and (num & (num - 1)) == 0):
#     print("yes")
# else:
#     print("no")

# xor gate without using xor logic

# num = 5
# num1 = 6
# print((num & (~num1)) | ((~num) & num1))

# Check if two numbers are equal without using arithmetic and comparison operators
# num = 10
# num2 = 20
# if((num ^ num2 )!= 0):
#     print("Not same ..")
# else:
#     print("Same")

# Multiply two numbers without using *

# num  = 12
# num2 = 3
# res = 0
# while(num2 > 0):
#     res = res + num
#     num2 -= 1
# print(res)

# Swap bits in a given number

# num = int(input())
# binary = bin(num)[2:]
# string = binary[::-1]
# res = "{:d}".format(int(string , 2))
# print(res)

# Find the smallest power of 2 greater than or equal to n in Python

# import math
# x = int(input())
# def next_power_of_2(x):
#     return 1 if x == 0 else 2**math.ceil(math.log2(x))
# print(next_power_of_2(x))0

# Program to find parity

# num = int(input())
# if(bin(num).count("1") % 2):
#     print("Odd Parity ..")
# else:
#     print("Even Parity ..")

# Check if binary representation of a number is palindrome

# num = int(input())
# if(bin(num)[2:] == bin(num)[2:][::-1]):
#     print("Palindrome ..")
# else:
#     print("Not Palindrome")

# generating gray code
# def main():
#     n=int(input())
#     for i in range(0, 1<<n):
#         gray=i^(i>>1)
#         print("{0:0{1}b}".format(gray,n))
#
# main()

# No consective set bits in binary number

# def sparse(num):
#     if(num & (num >> 1)):
#         return 0
#     return 1
# num = int(input())
#
# if(sparse(num)):
#     print("sparse number")
# else:
#     print("Not a sparse number")

# Binary to Gray

# def BinarytoGray(num):
#     num = num ^ (num >> 1)
#     return num
# num = int(input())
# print(BinarytoGray(num))
