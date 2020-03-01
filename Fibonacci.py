#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# -*- coding:utf-8 -*-
# class Solution:
#     def __init__(self):
#         self.a=0
#         self.b=1
#
#     def Fibonacci(self, n):
#         if n == 0:
#             return self.a
#         # write code here
#         self.a,self.b=self.b,self.a +self. b
#         self.Fibonacci(n-1)
#         return self.a

class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.Fibonacci(n-1)+self.Fibonacci(n-2)

if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci(5))


