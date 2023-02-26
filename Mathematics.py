

"""
Learn all divisibility rules of numbers .. upto as much as you can , easily solution is % operator ..
"""
# https://www.geeksforgeeks.org/mathematical-algorithms/?ref=shm

# LCM of given array elements

# def Lcm_find(num1,num2):
#     if(num1 > num2):
#         num = num1
#         den = num2
#     else:
#         num = num2
#         den = num1
#     rem = num % den
#     while(rem != 0):
#         num = den
#         den = rem
#         rem = num % den
#     gcd = den
#     lcm = num1 * num2 // gcd
#     return lcm
#
# L = list(map(int,input().split()))
# num1 = L[0]
# num2 = L[1]
# lcm = Lcm_find(num1 , num2)
#
# for i in range(2,len(L)):
#     lcm = Lcm_find(lcm , L[i])
# print(lcm)

# import math
# L = list(map(int,input().split()))
# print(math.lcm(*L))

# GCD of more than two (or array) numbers

# def Gcd_find(num1 , num2):
#     while(num2):
#         num1 , num2 = num2 , num1 % num2
#     return num1
#
# L = list(map(int,input().split()))
# num1 = L[0]
# num2 = L[1]
# gcd = Gcd_find(num1 , num2)
#
# for i in range(2,len(L)):
#     gcd = Gcd_find(gcd , L[i])
# print(gcd)

# import math
# L = list(map(int,input().split()))
# print(math.gcd(*L))


# juggler Sequence
# The terms in Juggler Sequence first increase to a peak value and then start decreasing.
# The last term in Juggler Sequence is always 1.
# import math
# def printJuggler(n):
#     a = n
#     print(a, end=" ")
#     while (a != 1):
#         b = 0
#         if (a % 2 == 0):
#             b = (int)(math.floor(math.sqrt(a)))
#
#         else:
#             b = (int)(math.floor(math.sqrt(a) * math.sqrt(a) *
#                                  math.sqrt(a)))
#
#         print(b, end=" ")
#         a = b
# printJuggler(3)
# print()
# printJuggler(9)

# Padovan Sequence
# For Padovan Sequence:
# P0 = P1 = P2 = 1 ,
# P(7) = P(5) + P(4)
#      = P(3) + P(2) + P(2) + P(1)
#      = P(2) + P(1) + 1 + 1 + 1
#      = 1 + 1 + 1 + 1 + 1
#      = 5

# Padovan Sequence: 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37,…..
# Spiral of equilateral triangles with side lengths which follow the Padovan sequence.
#
# def pad(n):
#     pPrevPrev, pPrev, pCurr, pNext = 1, 1, 1, 1
#
#     for i in range(3, n + 1):
#         pNext = pPrevPrev + pPrev
#         pPrevPrev = pPrev
#         pPrev = pCurr
#         pCurr = pNext
#
#     return pNext
# print(pad(10))

# https://www.geeksforgeeks.org/moser-de-bruijn-sequence/

# https://www.geeksforgeeks.org/stern-brocot-sequence/

# https://www.geeksforgeeks.org/newman-conway-sequence/

# Sum of the sequence 2, 22, 222, ………
# https://www.toppr.com/ask/question/find-the-sum-to-n-terms2-22-222/
# sum = 2/ 81 (10 ^ n+ 1 - 9n - 10)

# import math
#
# number = int(input())
# sums = 2/81 * (math.pow(10 ,(number+ 1)) - 9*number - 10)
# print(sums)

# Sum of series 1^2 + 3^2 + 5^2 + . . . + (2*n – 1)^2

# Σn2 = [n(n+1)(2n+1)]/6 - squares of N natural numbers
#  Σ(2n)^2 =[2n(n+1)(2n+1)]/3 - Sum of Squares of First n Even Numbers
# Σ(2n-1)^2 = [n(2n+1)(2n-1)]/3 - Sum of Squares of First n Odd Numbers

# Squares of two numbers	x2 + y2 = (x+y)2-2ab
# Squares of three numbers	x2 + y2+z2 = (x+y+z)2-2xy-2yz-2xz
# Squares of first ‘n’ natural numbers	Σn2 = [n(n+1)(2n+1)]/6
# Squares of first even natural numbers	Σ(2n)2 = [2n(n+1)(2n+1)]/3
# Squares of first odd natural numbers	Σ(2n-1)2 =[n(2n+1)(2n-1)]/3

# number = int(input())
# res = int((number * (2 * number - 1) * (2 * number + 1)) / 3)
# print(res)

# Sum of the series 0.6, 0.06, 0.006, 0.0006, …to n terms

 # sum of n terms = a(1-r^n)/1-r
 # here => 6/10(1-(1/10)^n) / 1-(1/10)
 # then => 6/9 (1-(1/10)^n)
 # then => 2/3 (1-(1/10)^n)

# import math
# number = int(input())
# res = 0.666 * (1 - 1 / math.pow(10, number))
# print(res)

# n-th term in series 2, 12, 36, 80, 150…. -- (n^2 + n^3)

# number = int(input())
# res = (number * number) + (number*number*number)
# print(res)

# Program for dot product and cross product of two vectors
"""
https://www.geeksforgeeks.org/program-dot-product-cross-product-two-vector/
"""


# Program to find correlation coefficient
'''
https://www.geeksforgeeks.org/program-find-correlation-coefficient/
(float)(n * sum_XY - sum_X * sum_Y) / (float)(math.sqrt((n * squareSum_X - sum_X * sum_X)* (n * squareSum_Y - sum_Y * sum_Y)))
'''

# Number of non-negative integral solutions of a + b + c = n

# def three(n):
#     res = 0
#     for i in range(n+1):
#         for j in range(n+1):
#             for k in range(n+1):
#                 if(i+j+k == n):
#                     res += 1
#     return res
# n = int(input())
# print(three(n))

# n = int(input())
# res = (n+1)*(n+2) //2
# print(res)

# Generate Pythagorean Triplets

# n = int(input())
# L = []
# for i in range(1,n):
#     for j in range(1,n):
#         for k in range(1,n):
#             if(i*i + j*j == k*k):
#                 L.append([i,j,k])
# print(L)

# def pythagoreanScaled(n):
#     triplelist = []
#     for x in range(n):
#         one = 3*x
#         two = 4*x
#         three = 5*x
#         triple = (one,two,three)
#         triplelist.append(triple)
#     return triplelist
# num = int(input())
# print(*pythagoreanScaled(num + 1)[1:])

# Check if a number is power of k using base changing method

# def check_kth_power(n, k):
#     while (n % k == 0):
#         n = n / k
#
#     if n != 1:
#         return False
#     return True
#
# print(check_kth_power(128, 2))
"""
https://www.geeksforgeeks.org/prime-numbers/

learn important properites there
"""
# prime efficient one
# def isprime(n):
#   if n==2 and n==1:
#     print('true')
#   else:
#     # formula for cheacking prime or not
#     p=(2**n-1)%n
#     if p==1:
#       print ('true')
#     else:
#       print('false')
# num = int(input())
# isprime(num)

# Left-Truncatable Prime

''''
for i in range(1,len(str(n))):
    res = n // 10**i
    L.append(res)
then check for required conditions    
'''

# def prime_factors(n):
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             factors.append(i)
#     if n > 1:
#         factors.append(n)
#     return factors
# n = int(input())
# print(prime_factors(n))

# find all divisors of number

# num = int(input())
# for i in range(1,num+1):
#     if(num % i == 0):
#         print(i,end=" ")