#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    def reOrderArray(self, array):
        # write code here
        n = len(array)
        i = 0
        while i < n:
            if array[i] % 2 == 1:
                i += 1
            else:
                array.append(array.pop(array.index(array[i])))
                n -= 1
        return array


s = Solution()
print(s.reOrderArray([1,2,3,4,5,6,7]))