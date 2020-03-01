# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return
        if len(pre) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        left = tin[0:tin.index(pre[0])]
        root.left = self.reConstructBinaryTree(pre[1:len(left)+1],left)
        right = tin[(tin.index(pre[0])+1):]
        root.right = self.reConstructBinaryTree(pre[(tin.index(pre[0])+1):],right)
        return root

    def printTreeNode_last_order(self,node):
        # 后序遍历
        while node is None:
            return
        self.printTreeNode_last_order(node.left)
        self.printTreeNode_last_order(node.right)
        print(node.val,end=",")

    def breadth_travel(self,node):
        # 广度优先遍历
        while node is None:
            return
        queue = [node]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.val,end=",")
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)

if __name__ == '__main__':
    s = Solution()
    t = s.reConstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])
    # s.breadth_travel(t)
    s.printTreeNode_last_order(t)





