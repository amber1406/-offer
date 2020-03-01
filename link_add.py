# #!/usr/bin/env python
# # _*_ coding:utf-8 _*_
#
# #!/usr/bin/env python
# # _*_ coding:utf-8 _*_
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class SingleLink(object):
#     def __init__(self,node = None):
#         self.__head = node
#
#     def add(self,x):
#         node = ListNode(x)
#         node.next = self.__head
#         self.__head = node
#
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         a,b,p,carry = l1,l2,ListNode(None),0
#         while a or b:
#             a_val = a.val if a else 0
#             b_val = b.val if b else 0
#             val_sum = a_val + b_val +carry
#             if val_sum >= 10:
#                 carry = 1
#                 val_sum = val_sum % 10
#             p,p.val = a,val_sum
#             a = a.next if a else None
#             b = b.next if b else None
#             p = p.next
#         if carry:
#             p.next = ListNode(carry)
#         return p
#
# if __name__ == '__main__':
#     s = Solution()
#     link1 = SingleLink()
#     link1.add(1)
#     link1.add(2)
#     link1.add(3)
#     link2=SingleLink()
#     link2.add(4)
#     link2.add(5)
#     link2.add(6)
#     print(s.addTwoNumbers(link1,link2))


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 这里一开始不做l1、l2非空判断，题意表明非空链表
        # 记录是否需要增加新节点，或在链表下一个节点是否需要加1，同时记录链表同级节点的和
        carry = 0
        # 这里的执行顺序是res = ListNode(0), pre = res
        res = pre = ListNode(0)
        # 判断l1、l2、carry是否有值，carry有值的话需要增加新节点，或在链表下一个节点需要加1
        while l1 or l2 or carry:
            # 判断l1是否有值
            if l1:
                carry += l1.val
                l1 = l1.next
            # 判断l2是否有值
            if l2:
                carry += l2.val
                l2 = l2.next
            # carry有同级节点的和
            # divmod返回商与余数的元组，拆包为carry和val
            # carry有值的话需要增加新节点，或在链表下一个节点需要加1,在循环中会用到
            carry, val = divmod(carry, 10)
            # 新建链表节点
            # 这里是n.next = ListNode(val), n = n.next()
            pre.next  = ListNode(val)
            pre = pre.next
            # pre.next = pre = ListNode(val)
            # res等价于pre，res.val=0，所以返回res.next
        return res.next


if __name__ == '__main__':
    # 创建对象Solution
    sol = Solution()
    # 定义l1链表
    l1 = ListNode(2)
    l1.next = l11 = ListNode(4)
    l11.next = l12 = ListNode(5)
    # 定义l2链表
    l2 = ListNode(5)
    l2.next = l21 = ListNode(2)
    l21.next = l22 = ListNode(4)
    # 获取返回值的链表
    res = sol.addTwoNumbers(l1, l2)
    # 循环遍历出来
    while res:
        print(res.val,end="")
        res = res.next

#
#
#
