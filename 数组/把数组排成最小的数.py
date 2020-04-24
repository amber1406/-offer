#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        lens=len(numbers)
        if lens == 0:
            return ""

        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                front=int(str(numbers[i]) + str(numbers[j]))
                last=int(str(numbers[j]) + str(numbers[i]))
                if front > last:
                    numbers[i], numbers[j]=numbers[j], numbers[i]

        return int("".join(list(map(str, numbers))))


if __name__ == '__main__':
    s = Solution()
    print(s.PrintMinNumber([1]))