#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def FindKthToTail(self, head, k):
#         # write code here
#         news_Node = head
#         if head is None or k == 0:
#             return None
#         lens=0
#         while head:
#             lens+=1
#             head=head.next
#         if k > lens:
#             return None
#         nth=lens - k
#         for i in range(nth):
#             news_Node = news_Node.next
#         return news_Node
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None or k == 0:
            return None
        fast = low = head
        for i in range(k):
            if not fast:
                return None
            fast = fast.next
        while fast:
            fast = fast.next
            low = low.next
        return low.val

l1 = ListNode(1)
# l2 = l1.next = ListNode(2)
# l3 = l2.next = ListNode(3)
s = Solution()
print(s.FindKthToTail(l1,2))



