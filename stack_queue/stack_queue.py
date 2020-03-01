#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if self.stack1:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            pop_node = self.stack2.pop()
            for i in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop())
            return pop_node
        else:
            return None

if __name__ == '__main__':
    s = Solution()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    print(s.pop())