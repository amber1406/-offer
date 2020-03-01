#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    def jumpFloorII(self, number):
        # write code here
        n = 1
        if number >= 2:
            for i in range(2,number+1):
                n *= 2
        return n

if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloorII(3))