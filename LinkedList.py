# # class Node:
# #     def __init__(self,dataVal = None):
# #         self.dataVal = dataVal
# #         self.NextVal = None
# #
# # class SLinkedList:
# #     def __init__(self):
# #         self.headVal = None
# #
# #     def ListPrint(self):
# #         printVal = self.headVal
# #         while printVal is not None:
# #             print(printVal.dataVal)
# #             printVal = printVal.NextVal
# #     def AtBeg(self,newData):
# #         NewNode = Node(newData)
# #         NewNode.NextVal = self.headVal
# #         self.headVal = NewNode
# #
# # List = SLinkedList()
# # List.headVal = Node("MonDay")
# # e2 = Node("TuesDay")
# # e3 = Node("WednesDay")
# # List.headVal.NextVal = e2
# # e2.NextVal = e3
# # List.AtBeg("SunDay")
# # List.ListPrint()
#
#
# # class Node:
# #     def __init__(self,dataVal):
# #         self.dataVal = dataVal
# #         self.next = None
# #
# # class LinkedList:
# #     def __init__(self):
# #         self.head = None
# #
# #     def printList(self):
# #         temp = self.head
# #         while(temp):
# #             print(temp.dataVal,end =" ")
# #             temp = temp.next
# #
# # LList = LinkedList()
# # LList.head = Node(1)
# # second = Node(2)
# # third = Node(3)
# #
# # LList.head.next = second
# # second.next = third
# #
# # LList.printList()
#
#
# Add a node at the front
# class Node:
#     def __init__(self,dataVal):
#         self.dataVal = dataVal
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def printList(self):
#         temp = self.head
#         while(temp):
#             print(temp.dataVal,end =" ")
#             temp = temp.next
#
#     def push(self,newData):
#         new_node = Node(newData)
#         new_node.next = self.head
#         self.head = new_node
#
# LList = LinkedList()
# LList.head = Node(1)
# second = Node(2)
# third = Node(3)
# LList.push(10)
# LList.push(11)
#
# LList.head.next = second
# second.next = third
#
# LList.printList()


# Add a node at the end
# class Node:
#     # Function to initialise the node object
#     def __init__(self, data):
#         self.data = data  # Assign data
#         self.next = None  # Initialize next as null
# # Linked List class contains a Node object
# class LinkedList:
#     # Function to initialize head
#     def __init__(self):
#         self.head = None
#     # Function to insert a new node at the beginning
#     def push(self, new_data):
#         # 1 & 2: Allocate the Node &
#         #        Put in the data
#         new_node = Node(new_data)
#         # 3. Make next of new Node as head
#         new_node.next = self.head
#         # 4. Move the head to point to new Node
#         self.head = new_node
#     # Utility function to print the linked list
#     def append(self,new_data):
#         new_node = Node(new_data)
#         if(self.head is None):
#             self.head = new_node
#             return
#         else:
#             last = self.head
#             while(last.next):
#                 last = last.next
#         last.next = new_node
#     def printList(self):
#         temp = self.head
#         while (temp):
#             print(temp.data,end=" ")
#             temp = temp.next
#
# # Code execution starts here
# if __name__=='__main__':
#     LList = LinkedList()
#     LList.push(10)
#     LList.push(11)
#     LList.push(1)
#     LList.push(0)
#     LList.append(20)
#     LList.append(30)
#
#     print('Created linked list is: ')
#     LList.printList()

# class Node:
#     # Function to initialise the node object
#     def __init__(self, data):
#         self.data = data  # Assign data
#         self.next = None  # Initialize next as null
# # Linked List class contains a Node object
# class LinkedList:
#     # Function to initialize head
#     def __init__(self):
#         self.head = None
#     # Function to insert a new node at the beginning
#     def push(self, new_data):
#         # 1 & 2: Allocate the Node &
#         #        Put in the data
#         new_node = Node(new_data)
#         # 3. Make next of new Node as head
#         new_node.next = self.head
#         # 4. Move the head to point to new Node
#         self.head = new_node
#     # Utility function to print the linked list
#     def insertAfter(self,prev_node,new_data):
#         if(prev_node is None):
#             print("Out")
#             return
#         new_node = Node(new_data)
#         new_node.next = prev_node.next
#         prev_node.next = new_node
#
#     def printList(self):
#         temp = self.head
#         while (temp):
#             print(temp.data,end=" ")
#             temp = temp.next
#
# # Code execution starts here
# if __name__=='__main__':
#     LList = LinkedList()
#     LList.push(10)
#     LList.push(11)
#     LList.push(1)
#     LList.push(0)
#     position = LList.head.next.next.next.next
#     LList.insertAfter(position,9)
#
#     print('Created linked list is: ')
#     LList.printList()

# --------------------------------- Coding Ninjas -------------------------------------------------------------------------

# class Node:
#     def __init__(self , data):
#         self.data = data
#         self.next = None
# a = Node(34)
# b = Node(45)
# c = Node(69)
#
# print(str(a.data) + "->" + str(a.next))
#
# print(str(b.data) + "->" + str(b.next))
#
# print(str(c.data) + "->" + str(c.next))
#
# a.next = b
#
# b.next = c
#
# print(str(a.data) + "->" + str(a.next) + "->" + str(a.next.data) + "->" + str(a.next.next) , end ="")
#
# # print(b.next.data)
#
# print(str(b.data) + "->" + str(b.next) + "->" + str(b.next.data) + "->" + str(b.next.next))

# Now taking input into the linkedlist

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# def printLL(head):
#     while head is not None:
#         print(str(head.data) + "->", end="")
#         head = head.next
#     print("None")
#     return
#
#
# def takeInput():
#     inputList = [int(ele) for ele in input().split()]
#     head = None
#     for currData in inputList:
#         if currData == -1:
#             break
#
#         newNode = Node(currData)
#         if head is None:
#             head = newNode
#
#         else:
#             curr = head
#             while curr.next is not None:
#                 curr = curr.next
#             curr.next = newNode
#
#     return head
#
#
# head = takeInput()
# printLL(head)


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# def printLL(head):
#     while head is not None:
#         print(str(head.data) + "->", end="")
#         head = head.next
#     print("None")
#     return
#
# def takeInput():
#     inputList = [int(ele) for ele in input().split()]
#     head = None
#     tail = None
#     for currData in inputList:
#         if currData == -1:
#             break
#
#         newNode = Node(currData)
#         if head is None:
#             head = newNode
#             tail = newNode
#
#         else:
#             tail.next = newNode
#             tail = newNode
#
#     return head
#
# head = takeInput()
# printLL(head)

# insert at ith position

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# def printLL(head):
#     while head is not None:
#         print(str(head.data) + "->", end="")
#         head = head.next
#     print("None")
#     return
#
# def lenght(head):
#     count = 0
#     while head is not None:
#         count = count + 1
#         head = head.next
#     return count
#
# def insert(head,i,data):
#     if i < 0 or i > lenght(head):
#         return head
#     count = 0
#     prev = None
#     curr = head
#     while count < i:
#         prev = curr
#         curr = curr.next
#         count = count + 1
#     newNode = Node(data)
#     if prev is not None:
#         prev.next = newNode
#     else:
#         head = newNode
#     newNode.next = curr
#     return head
#
# def takeInput():
#     inputList = [int(ele) for ele in input().split()]
#     head = None
#     tail = None
#     for currData in inputList:
#         if currData == -1:
#             break
#
#         newNode = Node(currData)
#         if head is None:
#             head = newNode
#             tail = newNode
#
#         else:
#             tail.next = newNode
#             tail = newNode
#
#     return head
#
# head = takeInput()
# printLL(head)
# head = insert(head,2,90)
# printLL(head)
#
# head = insert(head,0,6)
# printLL(head)
#
# head = insert(head,5,67)
# printLL(head)
#
# head = insert(head,7,71)
# printLL(head)

# 1 2 3 4 -1
# 1->2->3->4->None
# 1->2->90->3->4->None
# 6->1->2->90->3->4->None
# 6->1->2->90->3->67->4->None
# 6->1->2->90->3->67->4->71->None

# reverse a linkedList

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# def printLL(head):
#     while head is not None:
#         print(str(head.data) + "->", end="")
#         head = head.next
#     print("None")
#     return
#
# def takeInput():
#     inputList = [int(ele) for ele in input().split()]
#     head = None
#     tail = None
#     for currData in inputList:
#         if currData == -1:
#             break
#
#         newNode = Node(currData)
#         if head is None:
#             head = newNode
#             tail = newNode
#         else:
#             tail.next = newNode
#             tail = newNode
#
#     return head
#
# def reversal(head):
#     if head is None or head.next is None:
#         return head
#     smallHead = reversal(head.next)
#     curr = smallHead
#     while curr.next is not None:
#         curr = curr.next
#     curr.next = head
#     head.next = None
#     return smallHead
#
# head = takeInput()
# printLL(head)
# head = reversal(head)
# printLL(head)



