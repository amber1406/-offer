#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        sort_list=[]
        # write code here
        self.mid_visit(pRootOfTree,sort_list)
        lens = len(sort_list)
        if lens == 0:
            return None
        if lens == 1:
            return sort_list[0]
        #改变列表中的元素节点的指针指向
        for i in range(lens):
            if i == 0:
                sort_list[i].right = sort_list[i+1]
            elif i == lens-1:
                sort_list[i].left = sort_list[i-1]
            else:
                sort_list[i].right = sort_list[i+1]
                sort_list[i].left = sort_list[i-1]
        return sort_list[0]

    # 中序遍历，通过列表存储二叉树的遍历结果
    def mid_visit(self, pRoot,sort_list):
        if not pRoot:
            return
        self.mid_visit(pRoot.left,sort_list)
        sort_list.append(pRoot)
        self.mid_visit(pRoot.right,sort_list)

A = TreeNode(1)
A1 = A.left = TreeNode(2)
A2 = A.right = TreeNode(3)
A1.left = TreeNode(4)
A1.right = TreeNode(5)
A2.left = TreeNode(6)
A2.right = TreeNode(7)

s = Solution()
re = s.Convert(A)
while re:
    print(re.val)
    re = re.right