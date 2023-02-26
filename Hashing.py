#
# # a = 4
# # print(hash(a))
# # b = 23.23
# # print(hash(b))
# # c = "qwertyytrewq"
# # print(hash(c))
# #
# # tuple_val = (1, 2, 3, 4, 5)
# # print(hash(tuple_val))
# #
# # List =  [1, 2, 3, 4, 5]
# # print(hash(List))
#
# # Implementation of hash functions
#
# HashTable = [[] for i in range(10)]
# # print(HashTable)
#
# def Hashing(keyvalue):
#     return keyvalue % len(HashTable)
#
# def insert(HashTable , keyvalue , value):
#     hash_key = Hashing(keyvalue)
#     HashTable[hash_key].append(value)
#
# def search(HashTable , value):
#     res = any(value in sub for sub in HashTable)
#     if(res):
#         print(value , "is present")
#     else:
#         print(value ,"is not present")
#
# insert(HashTable, 10, 'Allahabad')
# insert(HashTable, 25, 'Mumbai')
# insert(HashTable, 20, 'Mathura')
# insert(HashTable, 9, 'Delhi')
# insert(HashTable, 21, 'Punjab')
# insert(HashTable, 21, 'Noida')
# insert(HashTable , 3 , 'jaswanth')
#
# search(HashTable , "singh")
# search(HashTable , 'Mathura')
#
#
# print(HashTable)

