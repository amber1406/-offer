#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result=False
        if pRoot1 is None or pRoot2 is None:
            return result
        #从根节点开始判断，比较是否相同，不相同则继续比较左子树，右子树
        else:
            return self.TreeAofTreeB(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(
                pRoot1.right, pRoot2)

    def TreeAofTreeB(self, pRoot1, pRoot2):
        #比较两个二叉树，直到B二叉树为空，则说明节点相同，包含
        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.TreeAofTreeB(pRoot1.left, pRoot2.left) and self.TreeAofTreeB(pRoot1.right, pRoot2.right)


A = TreeNode(1)
A1 = A.left = TreeNode(2)
A2 = A.right = TreeNode(3)
A1.left = TreeNode(4)
A1.right = TreeNode(5)

B = TreeNode(2)
B.left = TreeNode(4)
B.right = TreeNode(5)
S = Solution()
print(S.HasSubtree(A,B))

