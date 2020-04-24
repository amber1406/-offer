# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        lens = len(sequence)
        index = -1
        for i in range(lens-1):
            if sequence[i] > sequence[lens-1]:
                index = i
                break
        if index != -1:
            for j in range(index,lens-1):
                if sequence[j] < sequence[lens-1]:
                    return False
        return True