

# L = [1,2,3,4,5,6,7,8]
# ele = 3
# if(ele in L):
#     print("Yes")
# else:
#     print("No")

# L = [1,2,3,4,5,6,7,8]
# ele = 10
# if(ele not in L):
#     print("Yes")
# else:
#     print("No")

# def Linear(L,ele):
#     for i in range(len(L)):
#         if(ele == L[i]):
#             return i
#     return -1
#
# L = list(map(int,input().split()))
# ele = int(input())
# res = Linear(L,ele)
# if(res < 0):
#     print(res)
# else:
#     print(res + 1)

# def binarySearch(arr, x):
#     l = 0
#     r = len(arr)-1
#     while l <= r:
#         mid = l + (r-l)  // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             l = mid + 1
#         else:
#             r = mid - 1
#     return -1
#
# arr = list(map(int,input().split()))
# ele = int(input())
# res = binarySearch(arr,ele)
# print(res)


# def binarySearch(arr, l, r, x):
#     while r >= l:
#         mid = l + (r - l) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] > x:
#             return binarySearch(arr, l, mid - 1, x)
#         else:
#             return binarySearch(arr, mid + 1, r, x)
#
#     return -1
#
# arr = list(map(int,input().split()))
# x = int(input())
# res= binarySearch(arr,0,len(arr)-1,x)
# if(res < 0):
#     print(res)
# else:
#     print(res + 1)

# Find first positions of an element in a sorted array

# def first(arr, x, n):
#     low = 0
#     high = n - 1
#     res = -1
#
#     while (low <= high):
#         # Normal Binary Search Logic
#         mid = (low + high) // 2
#
#         if arr[mid] > x:
#             high = mid - 1
#         elif arr[mid] < x:
#             low = mid + 1
#         # If arr[mid] is same as x, we update res and move to the left half.
#         else:
#             res = mid
#             high = mid - 1
#     return res
# L = list(map(int,input().split()))
# ele = int(input())
# res = first(L,ele,len(L))
# print(res)

# Find last positions of an element in a sorted array

# def last(arr, x, n):
#     low = 0
#     high = n - 1
#     res = -1
#
#     while (low <= high):
#         # Normal Binary Search Logic
#         mid = (low + high) // 2
#
#         if arr[mid] > x:
#             high = mid - 1
#         elif arr[mid] < x:
#             low = mid + 1
#         # If arr[mid] is same as x, we update res and move to the right half.
#         else:
#             res = mid
#             low = mid + 1
#     return res
# L = list(map(int,input().split()))
# ele = int(input())
# res = last(L,ele,len(L))
# print(res)

# Find first and last positions of an element in a sorted array

# def first(arr, low, high, key, length):
#     return arr.index(x)
#
# # function to find the last occurrence of the number
# def last(arr, low, high, key, length):
#     return length - 1 - arr[::-1].index(x)
#
# arr = list(map(int,input().split()))
# n = len(arr)
#
# x = int(input())
# print('First Occurrence = ', first(arr, 0, n - 1, x, n))
# print('Last Occurrence = ', last(arr, 0, n - 1, x, n))


# Count number of occurrences (or frequency) in a sorted array

# def first(arr, low, high, key, length):
#     return arr.index(x)
#
# # function to find the last occurrence of the number
# def last(arr, low, high, key, length):
#     return length - 1 - arr[::-1].index(x)
#
# arr = list(map(int,input().split()))
# n = len(arr)
#
# x = int(input())
# print(last(arr, 0, n - 1, x, n) - first(arr, 0, n - 1, x, n) + 1)

# Count 1’s in a sorted binary array

# def first(arr, low, high, key, length):
#     return length - arr.index(x)
#
# arr = list(map(int,input().split()))
# n = len(arr) - 1
#
# x = 1
# res = first(arr,0,n,x,len(arr))
# print(res)

# Search an element in a sorted and rotated Array

# def search(arr, target):
#     start, end = 0, len(arr) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[start] <= arr[mid]:
#             if arr[start] <= target < arr[mid]:
#                 end = mid - 1
#             else:
#                 start = mid + 1
#         else:
#             if arr[mid] < target <= arr[end]:
#                 start = mid + 1
#             else:
#                 end = mid - 1
#     return -1
#
# L = list(map(int,input().split()))
# target = int(input())
# res = search(L,target)
# print(res)

# peak elements in array

# def FindPeak(arr):
#     L = []
#     n = len(arr)
#     if(n==1):
#         L.append(arr[0])
#     if(arr[0]>=arr[1]):
#         L.append(arr[0])
#     if(arr[n-1] >= arr[n-2]):
#         L.append(arr[n-1])
#     for i in range(1,n-1):
#         if(arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]):
#             L.append(arr[i])
#     return L
#
# arr = list(map(int,input().split()))
# print(FindPeak(arr))

# twp pointer methods

# def isPairs(L,key):
#     n = len(L)
#     start = 0
#     end = n - 1
#     while(start < end):
#         if(L[start] + L[end] == key):
#             return True
#         elif(L[start] + L[end] > key):
#             end = end - 1
#         else:
#             start = start + 1
#     return -1
#
# L = list(map(int,input().split()))
# key = int(input())
# print(isPairs(L,key))

# Find a triplet that sum to a given value

# def isPairs(L,key):
#     for i in range(0,len(L)-2):
#         start = i + 1
#         end = len(L)-1
#         while(start < end):
#             if(L[i] + L[start] + L[end] == key):
#                 return True
#             elif(L[i] + L[start] + L[end] < key):
#                 start = start + 1
#             else:
#                 end = end - 1
#     return False
#
# L = list(map(int,input().split()))
# key = int(input())
# print(isPairs(L,key))

# majority element

# def checkMajorityElement(arr, N):
#    mp = {}
#    for i in range(0, N):
#       if arr[i] in mp.keys():
#          mp[arr[i]] += 1
#       else:
#          mp[arr[i]] = 1
#    for key in mp:
#       if mp[key] > (N / 2):
#          return key
#    return -1
# arr = list(map(int,input().split()))
# ans = checkMajorityElement(arr,len(arr))
# if ans != -1:
#    print("Majority Element is: %d" % ans)
# else:
#    print("No majority element in array")



# Python3 program for optimal allocation of pages

# Utility function to check if
# current minimum value is feasible or not.


# def isPossible(arr, n, m, curr_min):
# 	studentsRequired = 1
# 	curr_sum = 0
#
# 	# iterate over all books
# 	for i in range(n):
#
# 		# check if current number of pages are greater than curr_min that means we will get the result after mid no. of pages
# 		if (arr[i] > curr_min):
# 			return False
#
# 		# count how many students are required to distribute curr_min pages
# 		if (curr_sum + arr[i] > curr_min):
# 			# increment student count
# 			studentsRequired += 1
# 			# update curr_sum
# 			curr_sum = arr[i]
# 			# if students required becomes greater than given no. of students, return False
# 			if (studentsRequired > m):
# 				return False
#
# 		# else update curr_sum
# 		else:
# 			curr_sum += arr[i]
#
# 	return True
#
# # function to find minimum pages
#
#
# def findPages(arr, n, m):
# 	sum = 0
#
# 	# return -1 if no. of books is less than no. of students
# 	if (n < m):
# 		return -1
#
# 	# Count total number of pages
# 	for i in range(n):
# 		sum += arr[i]
# # initialize start as 0 pages and end as total pages
# 	start, end = 0, sum
# 	result = 10**9
#
# 	# traverse until start <= end
# 	while (start <= end):
#
# 		# check if it is possible to distribute books by using mid as current minimum
# 		mid = (start + end) // 2
# 		if (isPossible(arr, n, m, mid)):
# 	# update result to current distribution as it's the best we have found till now.
# 			result = mid
# # as we are finding minimum and books are sorted so reduce end = mid -1 that means
# 			end = mid - 1
#
# 		else:
# 			# if not possible means pages should be increased so update start = mid + 1
# 			start = mid + 1
#
# 	# at-last return minimum no. of pages
# 	return result
#
# # Number of pages in books
# arr = [12, 34, 67, 90]
# n = len(arr)
# m = 2 # No. of students
#
# print("Minimum number of pages = ",
# 	findPages(arr, n, m))

