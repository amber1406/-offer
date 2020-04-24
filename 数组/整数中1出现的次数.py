#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# class Solution:
#     def NumberOf1Between1AndN_Solution(self, n):
#         # write code here
#         count = 0
#         for i in range(1,n+1):
#             s = str(i)
#             for j in s:
#                 if j == '1':
#                     count += 1
#         return count

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        base=1
        count=0
        round=n
        while round > 0:
            round, weight=divmod(round, 10)
            count+=round * base
            if weight == 1:
                count+=(n % base + 1)
            elif weight > 1:
                count+=base
            base*=10
        return count
