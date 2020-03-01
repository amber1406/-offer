#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return
        queue = [root]
        while queue:
            pop_node = queue.pop(0)
            if pop_node.right is not None:
                queue.append(pop_node.right)
            if pop_node.left is not None:
                queue.append(pop_node.left)
            pop_node.left,pop_node.right = pop_node.right,pop_node.left
        return root

def trvel_tree(root):
    if not root:
        return
    print(root.val,end=" ")
    trvel_tree(root.left)
    trvel_tree(root.right)

A = TreeNode(1)
A1 = A.left = TreeNode(2)
A2 = A.right = TreeNode(3)
A1.left = TreeNode(4)
A1.right = TreeNode(5)
A2.left = TreeNode(6)
A2.right = TreeNode(7)

s = Solution()
res = s.Mirror(A)
trvel_tree(res)