# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return
        
        result = [ ]
        stack = [root]
        while stack:
            u = stack.pop()
            result.append(u.val)
            if u.right:
                stack.append(u.right)
            if u.left:
                stack.append(u.left)
        return result
