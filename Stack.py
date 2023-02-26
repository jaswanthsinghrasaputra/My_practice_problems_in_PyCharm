
# stack = []
# stack.append(10)
# stack.append(29)
# stack.append(19)
# stack.pop()
# print(stack)

# from sys import maxsize
#
# def createStack():
#     stack = []
#     return stack
#
# def isEmpty(stack):
#     return len(stack) == 0
#
# def push(stack,item):
#     stack.append(item)
#     print(item,"is pushed into stack")
#
# def pop(stack):
#     if(isEmpty(stack)):
#         return str(-maxsize -1)
#     else:
#         return stack.pop()
#
# def top(stack):
#     if(isEmpty(stack)):
#         return str(-maxsize-1)
#     else:
#         return stack[len(stack)-1]
#
# stack = createStack()
# push(stack, str(10))
# push(stack, str(20))
# push(stack, str(30))
# print(pop(stack), " popped from stack")
# print(top(stack), "Top element")
# print(*stack)


# class StackUsingArray:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, item):
#         self.stack.append(item)
#
#     def pop(self):
#         if (not self.isEmpty()):
#             lastElement = self.stack[-1]
#             # del(self.stack[-1])
#             self.stack.pop(self.stack[-1])
#             return lastElement
#         else:
#             return("Stack is empty")
#
#     def isEmpty(self):
#         return self.stack == []
#
#     def printStack(self):
#         print(self.stack)
#
# s = StackUsingArray()
# print("Stack Using Array")
# while(True):
#     e1 = int(input("1 for Push\n2 for Pop\n3 to check if it is Empty\n4 to print Stack\n5 to exit\n"))
#     if(e1 == 1):
#         item = input("enter elements to push in stack")
#         s.push(item)
#     if(e1 == 2):
#         print(s.pop())
#     if(e1 == 3):
#         print(s.isEmpty())
#     if(e1 == 4):
#         s.printStack()
#     if(e1 == 5):
#         break

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# class Stack:
#     def __init__(self):
#         self.head = None
#
#     def isEmpty(self):
#         if self.head == None:
#             return True
#         else:
#             return False
#
#     def push(self,data):
#         if self.head == None:
#             self.head = Node(data)
#         else:
#             newnode = Node(data)
#             newnode.next = self.head
#             self.head = newnode
#
#     def pop(self):
#         if self.isEmpty():
#             return None
#         else:
#             poppednode = self.head
#             self.head = self.head.next
#             poppednode.next = None
#             return poppednode.data
#
#     def peek(self):
#         if self.isEmpty():
#             return None
#         else:
#             return self.head.data
#
#     def display(self):
#         iternode = self.head
#         if self.isEmpty():
#             print("Stack Underflow")
#         else:
#             while (iternode != None):
#                 print(iternode.data, end="")
#                 iternode = iternode.next
#                 if (iternode != None):
#                     print(" - ", end="")
#             return
#
#
#
#
# MyStack = Stack()
# while(True):
#
#     print("\nPush , enter value too.. here ")
#     print("Pop ")
#     print("Quit ")
#     print("Display ")
#     operation = input().split()
#
#     operation1 = operation[0].strip().lower()
#     if(operation1 == 'push'):
#         MyStack.push(operation[1])
#     elif(operation1 == 'pop'):
#         MyStack.pop()
#     elif(operation1 == 'display'):
#         MyStack.display()
#     elif(operation1 == 'quit'):
#         break


