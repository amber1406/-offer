# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None
        list_node = []
        while pHead:
            list_node.append(pHead.val)
            pHead = pHead.next
        list_node = list_node[::-1]
        result = head = ListNode(0)
        for i in list_node:
            head.next = ListNode(i)
            head = head.next
        return result.next

l1 = ListNode(1)
l2 = l1.next = ListNode(2)
l3 = l2.next = ListNode(3)
s = Solution()
print(s.ReverseList(l1))