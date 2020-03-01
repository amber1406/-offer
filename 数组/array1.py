#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        for i in array:
            for j in i:
                if j == target:
                    print("true")
                    return True

if __name__ == '__main__':
    s = Solution()
    s.Find(3,[[1,2,3],[4,5,6]])