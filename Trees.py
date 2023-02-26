
# class Node:
#     def __init__(self,data,left,right):
#         self.left = left
#         self.right = right
#         self.data = data
#     def PrintTree(self):
#         print(self.data, self.left, self.right)
#
# root = Node(10, 3, 5)
# root1 = Node(20, 4, 5)
# root.PrintTree()
# print()
# root1.PrintTree()

# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key
#
# def insert(root, key):
#     if root is None:
#         return Node(key)
#     else:
#         if root.val == key:
#             return key
#         elif root.val < key:
#             root.right = insert(root.right, key)
#         else:
#             root.left = insert(root.left, key)
#     return root
#
#
#
#
# def traverse(root):
#     if root:
#         traverse(root.left)
#         print(root.val, end= " ")
#         traverse(root.right)
#
#
# r = Node(10)
# r = insert(r, 45)
# r = insert(r, 3)
# r = insert(r, 1)
# r = insert(r, 2)
# r = insert(r, 0)
#
# traverse(r)


# Algorithm Inorder(tree)
#
# Traverse the left subtree, i.e., call Inorder(left->subtree)
# Visit the root.
# Traverse the right subtree, i.e., call Inorder(right->subtree)

# class Node:
#     def __init__(self,key):
#         self.left = None
#         self.right = None
#         self.val = key
#
# def printInorder(root):
#     if root:
#         printInorder(root.left)
#         print(root.val , end=" ")
#         printInorder(root.right)
#
# root = Node(25)
# root.left = Node(15)
# root.right = Node(50)
# root.left.left = Node(10)
# root.left.right = Node(22)
# root.right.left = Node(35)
# root.right.right = Node(70)
#
# printInorder(root)
# Algorithm Preorder(tree)
#
# Visit the root.
# Traverse the left subtree, i.e., call Preorder(left->subtree)
# Traverse the right subtree, i.e., call Preorder(right->subtree)


# class Node:
#     def __init__(self,key):
#         self.left = None
#         self.right = None
#         self.val = key
#
# def printPreorder(root):
#     if root:
#         print(root.val, end=" ")
#         printPreorder(root.left)
#         printPreorder(root.right)
#
# root = Node(25)
# root.left = Node(15)
# root.right = Node(50)
# root.left.left = Node(10)
# root.left.right = Node(22)
# root.right.left = Node(35)
# root.right.right = Node(70)
#
# printPreorder(root)

# Algorithm Postorder(tree)
#
# Traverse the left subtree, i.e., call Postorder(left->subtree)
# Traverse the right subtree, i.e., call Postorder(right->subtree)
# Visit the root



class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def printPostorder(root):
    if root:

        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val, end=" ")

root = Node(25)
root.left = Node(15)
root.right = Node(50)
root.left.left = Node(10)
root.left.right = Node(22)
root.right.left = Node(35)
root.right.right = Node(70)

printPostorder(root)