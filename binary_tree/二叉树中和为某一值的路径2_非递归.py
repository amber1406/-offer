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
        queue = []
        queue.append((root,[root.val]))
        while queue:
            root,path = queue.pop(0)
            if not root.left and not root.right and sum(path)==expectNumber:
                #题目要求在返回值的list中，数组长度大的数组靠前，因为越往前插入符合条件的路径长度越小
                result.insert(0,path)
            if root.left:
                queue.append((root.left,path+[root.left.val]))
            if root.right:
                queue.append((root.right,path+[root.right.val]))
        return result




A = TreeNode(10)
A1 = A.left = TreeNode(12)
A2 = A.right = TreeNode(5)
A2.left = TreeNode(4)
A2.right = TreeNode(7)

s = Solution()
print(s.FindPath(A,22))
