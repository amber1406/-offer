#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        lens = len(array)
        if lens == 1:
            return array[0]
        max_num = array[0]
        for i in range(1,lens):
            if array[i-1] > 0:
                array[i] = array[i-1] + array[i]
            max_num = max(array[i],max_num)
        return max_num

if __name__ == "__main__":
    s = Solution()
    print(s.FindGreatestSumOfSubArray([2,8,-1,-5,9]))