# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        current_head = pHead
        #复制链表节点
        while current_head:
            clone_node = RandomListNode(current_head.label)
            clone_node.next = current_head.next
            current_head.next = clone_node
            current_head = current_head.next.next
        #复制随机节点给新链表节点
        current_head = pHead
        while current_head:
            current_head.next.random = current_head.random if current_head.random else None
            current_head = current_head.next.next
        #拆分新旧两个链表
        current_head = pHead
        clone_head = pHead.next
        while current_head:
            temp = current_head.next
            current_head.next = temp.next
            temp.next = temp.next.next if temp.next else None
            current_head = current_head.next
        return clone_head


if __name__ == "__main__":
    l1=RandomListNode(1)
    l1.next=l11=RandomListNode(3)
    l11.next=l12=RandomListNode(5)
    l12.next=l13 = RandomListNode(4)
    l11.random=RandomListNode(6)
    l12.random=RandomListNode(8)
    s=Solution()
    aa=s.Clone(l1)
    while aa:
        print(aa.label)
        aa=aa.next
