"""
You are given a binary tree.

Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.

Example:

Given the following binary tree

    5
   / \
  12  32
     /  \
    8    4

your function should return the depth = 3.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value:
            # The value must go left
            if self.left is None:
            # Create a new node as a left child of current node
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
            
        else:
            # The value must go right
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # let the right hand Node figure it out
                self.right.insert(value)
                
    def search(self, target):
        if target == self.value:
            # we have found the item
            return True
        if target < self.value:
            # search the left side of the tree
            if self.left is None:
                return False
            # if a node exists to the left, call the search on that node
            return self.left.search(target)
            
        else:
            # search the right side of the tree
            if self.right is None:
                return False
            return self.right.search(target)
        

root = BSTNode(8)
root.insert(5)
root.insert(7)
root.insert(10)
root.insert(13)

print(root.search(7))
print(root.search(9))
print(root.search(10))