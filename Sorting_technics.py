# def bubble(L):
#     n = len(L)
#     for i in range(n):
#         for j in range(n-1-i): # to decrease iterations
#             if L[j] > L[j + 1]:
#                 L[j], L[j + 1] = L[j + 1], L[j]
#     return L
#
# L = list(map(int,input().split()))
# bubble(L)
# for i in range(len(L)):
#     print(L[i],end=" ")

# Optimized Implementation of Bubble Sort:

# def bubble(L):
#     n = len(L)
#     for i in range(n):
#         swapped = False
#         for j in range(n-1-i): # to decrease iterations
#             if L[j] > L[j + 1]:
#                 L[j], L[j + 1] = L[j + 1], L[j]
#                 swapped = True
#         if(swapped == False):
#             break
#
# L = list(map(int,input().split()))
# bubble(L)
# for i in range(len(L)):
#     print(L[i],end=" ")


# def selection(L):
#     n = len(L)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1,n):
#             if(L[min_idx] > L[j]):
#                 min_idx = j
#         L[i],L[min_idx] = L[min_idx],L[i]
#
# L = list(map(int,input().split()))
# selection(L)
# for i in range(len(L)):
#     print(L[i],end=" ")
#
#
# # 4th smallest element ..
# def selection(L):
#     n = len(L)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1,n):
#             if(L[min_idx] > L[j]):
#                 min_idx = j
#         L[i],L[min_idx] = L[min_idx],L[i]
#
# L = list(map(int,input().split()))
# if(len(L)<4):
#     print("-1")
# else:
#     L2 = []
#     selection(L)
#     for i in range(len(L)):
#         # print(L[i],end=" ")
#         L2.append(L[i])
#     print(L2[3])

# insertion sort

# def insertion(L):
#     for i in range(1,len(L)):
#         key = L[i]
#         j = i -1
#         while j >= 0 and key < L[j]:
#             L[j + 1] = L[j]
#             j -= 1
#         L[j + 1] = key
#     return L
#
# L = list(map(int,input().split()))
# print(insertion(L))

# def mergeSort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         L = arr[:mid]
#         R = arr[mid:]
#         mergeSort(L)
#         mergeSort(R)
#
#         i = j = k = 0
#
#         while i < len(L) and j < len(R):
#             if L[i] <= R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
#
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
#
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1
#
# def printList(arr):
#     for i in range(len(arr)):
#         print(arr[i], end=" ")
#     print()
#
# arr = list(map(int,input().split()))
# print("Given array is", end="\n")
# printList(arr)
# mergeSort(arr)
# print("Sorted array is: ", end="\n")
# printList(arr)

# def generateStrobogrammatic(n):
#     def generate(m, n):
#         if m == 0:
#             return ['']
#         if m == 1:
#             return ['0', '1', '8']
#         list = generate(m - 2, n)
#         res = []
#         for num in list:
#             if m != n:
#                 res.append('0' + num + '0')
#             res.append('1' + num + '1')
#             res.append('6' + num + '9')
#             res.append('8' + num + '8')
#             res.append('9' + num + '6')
#         return res
#
#     return generate(n, n)
#
# strobogrammatic_numbers = generateStrobogrammatic(2)
# print("4-digit strobogrammatic numbers:", strobogrammatic_numbers)
# # print("Total number of 4-digit strobogrammatic numbers:", len(strobogrammatic_numbers))


# intersection of two arrays

# L = list(map(int,input().split()))
# L2 = list(map(int,input().split()))
# res = []
#
# set1 = set(L)
#
# for i in L2:
#     if i in set1 and i not in res:
#         res.append(i)
#
# print(res)

# union of two arrays

# L1 = list(map(int,input().split()))
# L2 = list(map(int,input().split()))
# new_L = []
#
# for i in L1:
#     if i not in new_L:
#         new_L.append(i)
#
# for i in L2:
#     if i not in new_L:
#         new_L.append(i)
#
# print(new_L)

# inversion in the array

# L = list(map(int,input().split()))
# res = 0
# for i in range(0,len(L)-1):
#     for j in range(i+1,len(L)):
#         if(L[i]>L[j]):
#             res += 1
# print(res)

# partition function

# L = list(map(int,input().split()))
# L1 = []
# ele = int(input())
# for i in range(len(L)):
#     if(L[i]<=ele):
#         L1.append(L[i])
# for i in range(len(L)):
#     if(L[i]>ele):
#         L1.append(L[i])
#
# print(L1)

# def partition(array, low, high):
#     # Choose the rightmost element as pivot
#     pivot = array[high]
#  # Pointer for greater element
#     i = low - 1
#   # Traverse through all elements compare each element with pivot
#     for j in range(low, high):
#         if array[j] <= pivot:
#             # If element smaller than pivot is found swap it with the greater element pointed by i
#             i = i + 1
#             # Swapping element at i with element at j
#             (array[i], array[j]) = (array[j], array[i])
#     # Swap the pivot element with  greater element specified by i
#     (array[i + 1], array[high]) = (array[high], array[i + 1])
#
#     # Return the position from where partition is done
#     return i + 1
#
# def quick_sort(array, low, high):
#     if low < high:
#         # Find pivot element such that element smaller than pivot are on the left element greater than pivot are on the right
#         pi = partition(array, low, high)
#         # Recursive call on the left of pivot
#         quick_sort(array, low, pi - 1)
#         # Recursive call on the right of pivot
#         quick_sort(array, pi + 1, high)
#
# array = list(map(int,input().split()))
# quick_sort(array, 0, len(array) - 1)
#
# print(f'Sorted array: {array}')

# Kth smallest element

# arr = list(map(int,input().split()))
# N = len(arr)
# K = 4
#
# s = set(arr)
# print(s)
#
# for itr in s:
# 	if K == 1:
# 		print(itr) # itr is the Kth element in the set
# 		break
# 	K -= 1

# chocolate distribution

# arr = list(map(int,input().split()))
# arr.sort()
# m = int(input())
# min_diff = arr[len(arr)- 1] - arr[0]
# for i in range(len(arr) - m + 1):
#     min_diff = min(min_diff, arr[i + m - 1] - arr[i])
#
# print(min_diff)

