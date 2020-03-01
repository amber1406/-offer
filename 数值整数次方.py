# -*- coding:utf-8 -*-
# class Solution:
#     def Power(self, base, exponent):
#         # write code here
#         # return pow(base,exponent)
#         res=1
#         flag=1
#         if exponent == 0:
#             return res
#         if exponent < 0:
#             flag=-1
#             exponent = -exponent
#         while True:
#             if exponent == 0:
#                 break
#             res*=base
#             exponent-=1
#         return res if flag == 1 else 1 / res

class Solution:
    def Power(self, base, exponent):
        # write code here
        flag = 1
        if exponent < 0:
            exponent = -exponent
            flag = 0
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        res = self.Power(base,exponent >> 1) #用右移来代替/2 效率更高
        res *= res
        if exponent & 1: #判断exponent是奇数还是偶数
            res *= base
        return res if flag else 1/res

s = Solution()
print(s.Power(2,-6))