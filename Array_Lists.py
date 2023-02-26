# print factor of number

# number = int(input())
# List = []
# for i in range(1,number+1):
#     if(number % i == 0):
#         List.append(i)
# print(*List)

# check whether n is factor of m

# number = int(input())
# numberTwo = int(input())
# if(number % numberTwo == 0):
#     print("YES")
# else:
#     print("NO")

# check even or odd

# number = int(input())
# if(number & 1 ):
#     print("Odd number")
# else:
#     print("Even number")

# greatest of three numbers

# numOne , numTwo , numThree = map(int,input().split())
# if(numOne > numTwo and numOne > numThree):
#     print(numOne)
# elif( numTwo > numThree):
#     print(numTwo)
# else:
#     print(numThree)

# smallest of three number

# numOne , numTwo , numThree = map(int,input().split())
# if(numOne < numTwo and numOne < numThree):
#     print(numOne)
# elif(numTwo < numThree):
#     print(numTwo)
# else:
#     print(numThree)

# Greeting program of 24 hrs format

# time = int(input())
# if(time < 12):
#     print("Good Morning !!")
# elif(time >= 12 and time < 18):
#     print("Good AfterNoon !!")
# elif(time < 24 and time >= 18):
#     print("Good Evening !!")

# male or female
# String = input()
# if(String == "male"):
#     print("male")
# else:
#     print("Female")

# time calculator

# seconds = int(input("enter seconds:"))
# Hrs = seconds // 3600
# seconds = seconds - Hrs * 3600
# minutes = seconds // 60
# second = seconds - minutes * 60
# print(Hrs , "hrs:" ,int(minutes) ,"min:" , second , "secs" )

# while loop
# numbers = int(input())
# i = 1
# while (i <= numbers):
#     if(i < numbers):
#         print(i, end=",")
#     else:
#         print(i)
#     i += 1

# sum of numbers upto N

# number = int(input())
# i = 1
# count = 0
# while(i <= number):
#     count = count + i
#     i += 1
# print(count)


# method - 2
# number = int(input())
# print([i for i  in range(1,number + 1)])


# even and odd

# number = int(input())
# i = 1
# while(i <= number):
#     if(i % 2 == 0):
#         print(i , end=" ")
#     i += 1

# factorial of number

# number = int(input())
# i = 1
# count  = 1
# while (i <= number):
#     count = count * i
#     i += 1
# print(count)

# prime number or not

# import math
# number = int(input())
# count = 0
# for i in range(2,number):
#     if(number % math.sqrt(i) == 0):
#         count = count + 1
# if(count >= 1):
#     print("Not Prime number")
# else:
#     print("prime number")

# print number divide by 5

# number = int(input())
# List = []
# for i in range(1,number):
#     if(i % 5 == 0):
#         List.append(i)
# print(List)

# sum of odd number

# number = int(input())
# List = []
# for i in range(number):
#     if(i % 2 != 0):
#         List.append(i)
# print(sum(List))

# sum of factors of number

# number  = int(input())
# List = []
# for i in range(1,number):
#     if(number % i == 0):
#         List.append(i)
# print(sum(List))

# sum of prime number

# def isPrimeNumber(number):
#     for j in range(2, number):
#         if(number % j == 0):
#             return False
#     return True
# number = int(input())
# for i in range(2 , number + 1):
#     if (isPrimeNumber(i)):
#         print(i , end=" ")

# reverse number
# number = input()
# print(number[::-1])


# division operator with using loops

# number = int(input())
# numberOne = int(input())
# List = []
# count = 0
# for i in range(number // numberOne):
#     number = number - numberOne
#     List.append(number)
# print(len(List))

# multiplication

# numOne = int(input())
# numTwo = int(input())
# sums = 0
# count = 0
# for i in range(1,numTwo+1):
#     sums = sums + numOne
#     count = count + 1
#     if(count == numTwo):
#         print(sums)

# table
# table = int(input())
# number = int(input())
# if(number == 1):
#     for i in range(1,11):
#         print(f"{table}X{i}=",table*i)
# else:
#     for i in range(10,0,-1):
#         print(f"{table}X{i}=",table*i)

# sqaures the integers

# number = int(input())
# List = []
# for i in range(1,number):
#     List.append(i**2)
# print(*List)

# import math
# number = int(input())
# for i in range(1,int(math.sqrt(number)) + 1):
#     if(i**2 < number):
#         print(i**2 , end=' ')


# largest elements

# def largest(L):
#     n = len(L)
#     maxi = L[0]
#     for i in range(1,n):
#         if(L[i]>maxi):
#             maxi = L[i]
#     return maxi
#
#
# L = list(map(int,input().split()))
# res = largest(L)
# print(res)

# second largest not working properly

# def second_largest(L):
#     n = len(L)
#     largest = min(L)
#     secondLargest = 0
#     for i in range(n):
#         if(L[i]>largest):
#             secondLargest = largest
#             largest = L[i]
#         else:
#             secondLargest = max(secondLargest,L[i])
#     return secondLargest
#
#
# L = list(map(int,input().split()))
# res = second_largest(L)
# print(res)

# List is sorted or not

# def Sorted(L):
#     L1 = sorted(L)
#     if(L1 == L):
#         return True
#     else:
#         return False
#
# L = list(map(int,input().split()))
# res = Sorted(L)
# print(res)

# def Sorted(L):
#     i = 1
#     flag = 0
#     while(i<len(L)):
#         if(L[i]<L[i-1]):
#             flag = 1
#         i += 1
#     if(not flag):
#         return "Yes"
#     else:
#         return "No"
#
# L = list(map(int,input().split()))
# res = Sorted(L)
# print(res)

# reverse_list

# def reverse_list(L):
#     low = 0
#     high = len(L)-1
#     while(low < high):
#         temp = L[low]
#         L[low] = L[high]
#         L[high] = temp
#         low += 1
#         high -= 1
#     return L
#
# L = list(map(int,input().split()))
# res = reverse_list(L)
# print(*res)

# remove duplicates from List

# L = list(map(int,input().split()))
# L1 = []
# for i in L:
#     if(i not in L1):
#         L1.append(i)
# print(L1)

# move all zeros to end

# L = list(map(int,input().split()))
# for i in L:
#     if(i == 0):
#         L.remove(i)
#         L.append(0)
# print(*L)

# rotation of List

# L = list(map(int, input().split()))
# count = int(input())
# L = (L[len(L) - count-1:len(L)] + L[0:len(L) - count-1])
# print(L)

# Leaders of List

# L = list(map(int, input().split()))
# L1 = []
# size = len(L)
# max_from_right = L[size - 1]
# print(max_from_right, end=' ')
# for i in range(size - 2, -1, -1):
#     if max_from_right < L[i]:
#         print(L[i], end=' ')
#         max_from_right = L[i]

# maximum difference in list
# my_list = [1, 7, 3, 9, 5]
# max_diff = max(my_list) - min(my_list)
# print(max_diff)

# maximum difference in list j>i

# def maxiDiff(L):
#     maxi_diff = L[1]-L[0]
#     min_ele = L[0]
#     for i in range(1,len(L)):
#         maxi_diff = max(maxi_diff , L[i]-min_ele)
#         min_ele = min(min_ele,L[i])
#     return maxi_diff
#
# L = list(map(int,input().split()))
# res = maxiDiff(L)
# print(res)

# frequency of elements

# L = list(map(int,input().split()))
# L1 = list(set(L))
# for i in L1:
#     print(i,":",L.count(i))

# my_list = list(map(int,input().split()))
# frequency = {}
# for i in my_list:
#     if i in frequency:
#         frequency[i] += 1
#     else:
#         frequency[i] = 1
# print(frequency)

# stock buy and sell # Can understand by graph of shares

# L = list(map(int,input().split()))
# profit = 0
# for i in range(1,len(L)):
#     if(L[i]>L[i-1]):
#         profit += (L[i]-L[i-1])
# print(profit)

# # Trapping Rain Water
#
# arr = list(map(int,input().split()))
# res = 0
# n = len(arr)
# for i in range(1, n - 1):
#     left = arr[i]
#     for j in range(i):
#         left = max(left, arr[j])
#     right = arr[i]
#     for j in range(i + 1, n):
#         right = max(right, arr[j])
#     res = res + (min(left, right) - arr[i])
# print(res)


# consecutive ones in List

# arr = list(map(int,input().split()))
# res = 0
# count = 0
# for i in range(len(arr)):
#     if(arr[i]==0):
#         count = 0
#     else:
#         count += 1
#         res = max(res, count)
# print(res)

# Largest Sum Contiguous Subarray

# def maximumSubarraySum(arr):
#     n = len(arr)
#     maxSum = -1e8
#
#     for i in range(0, n):
#         currSum = 0
#         for j in range(i, n):
#             currSum = currSum + arr[j]
#             if(currSum > maxSum):
#                 maxSum = currSum
#
#     return maxSum
# L = list(map(int,input().split()))
#
# print(maximumSubarraySum(L))

# Longest even and odd sequences

# def longestEvenOddSubarray(a, n):
#     ans = 1
#     for i in range(n):
#         cnt = 1
#         for j in range(i + 1, n):
#             if ((a[j - 1] % 2 == 0 and a[j] % 2 != 0) or (a[j - 1] % 2 != 0 and a[j] % 2 == 0)):
#                 cnt = cnt+1
#             else:
#                 break
#         ans = max(ans, cnt)
#
#     if(ans == 1):
#         return 0
#     return ans
#
# a = list(map(int,input().split()))
# n = len(a)
# print(longestEvenOddSubarray(a, n))


# def printGroups(arr, n):
#     # Traverse through all array elements starting from the second element
#     for i in range(1, n):
#         # If current element is not same as previous
#         if (arr[i] != arr[i - 1]):
#             # If it is same as first element then it is starting of the interval to be flipped.
#             if (arr[i] != arr[0]):
#                 print("From", i, "to ", end="")
#             # If it is not same as previous and same as the first element, then previous element is end of interval
#             else:
#                 print(i - 1)
#     # Explicitly handling the end of last interval
#     if (arr[n - 1] != arr[0]):
#         print(n - 1)
# arr = list(map(int,input().split()))
# n = len(arr)
#
# printGroups(arr, n)

# Window Sliding Technique

# computing maxSum of window size

#
# def maxSum(arr,k,n):
#     max_sum = max(arr)
#
#     for i in range(n-k+1):
#         currSum = 0
#         for j in range(k):
#             currSum = currSum + arr[i+j]
#         max_sum =max(currSum,max_sum)
#
#     return max_sum
#
# arr = list(map(int,input().split()))
# k = 3
# n = len(arr)
# print(maxSum(arr,k,n))


"""
The Tribonacci Sequence:
0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768,
10609, 19513, 35890, 66012, 121415, 223317, 410744, 755476,
1389537, 2555757, 4700770, 8646064, 15902591, 29249425, 53798080, 98950096,
 181997601, 334745777, 615693474, 1132436852… so on
"""


# def printTribRec(n):
#     if (n == 0 or n == 1 or n == 2):
#         return 0
#     elif (n == 3):
#         return 1
#     else:
#         return (printTribRec(n - 1) + printTribRec(n - 2) + printTribRec(n - 3))
#
#
# def printTrib(n):
#     for i in range( 1, n):
#         print(printTribRec(i), " ", end="")
#
# n = int(input())
# printTrib(n)

# def bonacciseries(n, m):
#     # Assuming m >= n.
#     a = [0] * m
#     a[n - 1] = 1
#     # Computing every term as sum of previous n terms.
#     for i in range(n, m):
#         for j in range(i - n, i):
#             a[i] = a[i] + a[j]
#
#     for i in range(0, m):
#         print(a[i], end=" ")
#
# N = int(input())
# M = int(input())
# bonacciseries(N, M)



