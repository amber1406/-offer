# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        result=[]
        if not root:
            return result
        self.sum=expectNumber
        self.DFS(root, result, [root.val])
        return result

    def DFS(self, root, result, path):
        if not root.left and not root.right and sum(path) == self.sum:
            result.append(path)
        if root.left:
            self.DFS(root.left, result, path + [root.left.val])
        if root.right:
            self.DFS(root.right, result, path + [root.right.val])

A = TreeNode(1)
A1 = A.left = TreeNode(2)
A2 = A.right = TreeNode(3)
A1.left = TreeNode(4)
A1.right = TreeNode(5)
A2.left = TreeNode(6)
A2.right = TreeNode(7)

s = Solution()
print(s.FindPath(A,8))
