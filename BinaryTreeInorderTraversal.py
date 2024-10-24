# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, node, result):
        if node:
            self.traverse(node.left, result)
            result.append(node.val)
            self.traverse(node.right, result)
