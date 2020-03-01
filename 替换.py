#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import re
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        # split_str = s.split(" ")
        # # for i in range(len(split_str)):
        # i = 0
        # while True:
        #     if i == len(split_str)-1:
        #         print(split_str[i],end="")
        #         return
        #     print(split_str[i]+"%20",end="")
        #     i += 1
        after = re.sub(r' ','%20',s)
        return after

if __name__ == '__main__':
    s = Solution()
    a = s.replaceSpace("We Are Happy")
    print(a)