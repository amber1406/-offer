# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        temp = result = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                result.next = ListNode(pHead1.val)
                result = result.next
                pHead1 = pHead1.next
            else:
                result.next = ListNode(pHead2.val)
                result = result.next
                pHead2 = pHead2.next
        if pHead1:
            result.next = pHead1
        if pHead2:
            result.next = pHead2
        return temp.next

l1 = ListNode(1)
l1.next = l11 = ListNode(3)
l11.next = l12 = ListNode(5)
l2 = ListNode(2)
l2.next = l21 = ListNode(4)
l21.next = l22 = ListNode(6)
l22.next = l23 = ListNode(8)
s = Solution()
aa = s.Merge(l1,l2)
while aa:
    print(aa.val)
    aa = aa.next
