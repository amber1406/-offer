# -*- coding:utf-8 -*-
class Solution:
    # 从n的2进制形式的最右边开始判断是不是1：n&1 == 1
    # 该解法如果输入是负数会陷入死循环，
    # 因为负数右移时，在最高位补得是1，移到最后会全变成1
    # 本题最终目的是求1的个数，那么会有无数个

    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff #计算n的补码
        while n != 0:
            n = n&(n-1)
            count += 1
        return count

if __name__ == '__main__':
    S = Solution()
    print(S.NumberOf1(-8))