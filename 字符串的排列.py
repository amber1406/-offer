#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    def Permutation(self, ss):
        # write code here
        result = []
        lens = len(ss)
        if lens <= 1:
            return ss
        for i in range(lens):
            for leave in self.Permutation(ss[:i]+ss[i+1:]):
                temp = ss[i]+leave
                if temp not in result:
                    result.append(temp)
        return result

s = Solution()
print(s.Permutation("abc"))