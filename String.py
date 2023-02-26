
# palindrome

# string = input()
# start = 0
# stop = len(string) - 1
# while(start < stop):
#     if(string[start] != string[stop]):
#         print("Not palindrome")
#         break
#     else:
#         print("palindrome")
#     start += 1
#     stop -= 1

# sub sequences in string

# s1 = input()
# s2 = input()
# n = len(s1)
# m = len(s2)
# i , j = 0 , 0
# while(i < n and j < m):
#     if(s1[i] == s2[j]):
#         j += 1
#     i += 1
# if(j == m):
#     print('Yes')
# else:
#     print("No")


# Check whether two Strings are anagram of each other

# string1 = input()
# string2 = input()
#
# if(sorted(string1) == sorted(string2)):
#     print("Yes")
# else:
#     print("No")


# str1 = input()
# str2 = input()
#
# NO_OF_CHARS = 256
#
# if (len(str1) != len(str2)):
#     print('No')
#
# count = [0 for i in range(NO_OF_CHARS)]
# i = 0
#
# for i in range(len(str1)):
#     count[ord(str1[i]) - ord('a')] += 1
#     count[ord(str2[i]) - ord('a')] -= 1
#
# for i in range(NO_OF_CHARS):
#     if (count[i] != 0):
#         print("NO")
# print("Yes")

# string = input()
#
# stringOne = string[-2:]
# stringTwo = string[-3:]
# if('er' == stringOne):
#     print("er")
# elif('ist' == stringTwo):
#     print("ist")

# leftmost character in string

# string = input()
# char_count = {}
# L = []
# for char in string:
#     if(char in  char_count):
#         L.append(char)
#     else:
#         char_count[char] = 1
# print(L[0])

# leftmost non-repeating character

# string = input()
# char_count = {}
# L = []
# for char in string:
#     if(char in  char_count):
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# for char in string:
#     if(char_count[char] == 1):
#         L.append(char)
# print(L[0])

# reversing words in string

# string = input().split()
# print(*string[::-1])

# string = input().split()
# List = []
# for i in string:
#     List.insert(0,i)
# print(" ".join(List))

# pattern searching in the string

# string = input()
# pattern = input()
# lengthS = len(string)
# lenghtP = len(pattern)
# L = []
# for i in range(lengthS - lenghtP+1):
#     j = 0
#     while(j < lenghtP):
#         if(string[j+i] != pattern[j]):
#             break
#         j += 1
#     if(j == lenghtP):
#         L.append(i)
#     else:
#         pass
# print(*L)


# a , b , c = map(int,input().split())
# L = []
# for i in range(a , b + 1 , 1):
#     if(i % c == 0):
#         L.append(i)
# # print(min(L))
# if(len(L) == 0):
#     print('-1')
# else:
#     print(min(L))

# Check if given strings are rotations of each other or not

# string1 = input()
# string2 = input()
# if(len(string1) != len(string2)):
#     vari = False
#
# temp = string1 + string1
# if(temp.count(string2) > 0):
#     vari = True
# else:
#     vari = False
# if(vari == True):
#     print("Yes")
# else:
#     print("No")

# Anagram Substring Search (Or Search for all permutations)

# txt = input()
# pat = input()
#
# n = len(txt)
# m = len(pat)
# L = []
# sortedpat = sorted(pat)
#
# for i in range(0, n - m + 1):
#     temp = txt[i:i + m]
#     temp = sorted(temp)
#
#     if (sortedpat == temp):
#         L.append(i)
# if(len(L) == 0):
#     print('No')
# else:
#     print(L)


# List = list(map(int,input().split()))
# List2 = []
# for i in List:
#     List2.append(List.count(i))
# print(set(List2))
# List3 = [2,3]
# if(set(List2) == set(List3)):
#     print("Yes")
# else:
#     print('No')

# Lexicographic rank of a String
#
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# def lexicographic_rank(s):
#     n = len(s)
#     rank = 1
#     for i in range(n):
#         smaller = 0
#         for j in range(i+1, n):
#             if s[j] < s[i]:
#                 smaller += 1
#         rank += smaller * factorial(n-i-1)
#     return rank
# s = input()
# print("Lexicographic rank of", s, "is", lexicographic_rank(s))

number = int(input())

total_time = 21 * 60 + number

hours = total_time // 60

minutes = total_time % 60

hours = '{0:2d}'.format(hours)

minutes = '{0:2d}'.format(minutes)

final_time = hours + ":" + minutes

print(final_time)