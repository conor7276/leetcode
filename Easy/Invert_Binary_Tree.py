# 226. Invert Binary Tree https://leetcode.com/problems/invert-binary-tree/
# Runtime: 36 ms, faster than 86.72% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 13.9 MB, less than 57.02% of Python3 online submissions for Invert Binary Tree.
# Recursion uses more memory but may be faster. Iterative solution will use less memory but may be slower.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive Solution O(N)
        if(root == None): # if node is empty, case is for if tree is entirely empty
            return None
        if(root.left == None and root.right == None): # if tree has one node or if the node has no children
            return root
        if(root.left == None or root.right == None): # if the parent node has one child
            if(root.left != None and root.right == None): # if the right node is null swap left and right
                root.right = root.left
                root.left = None
                self.invertTree(root.right)
                return root
            if(root.right != None or root.left == None): # if the left node is null swap right and left
                root.left = root.right
                root.right = None
                self.invertTree(root.left)
                return root
        else: # if the parent node has two children swap both
            swap = root.left
            root.left = root.right
            root.right = swap
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
        return root