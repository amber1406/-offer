# # -*- coding:utf-8 -*-
# class Solution:
#     def rectCover(self, number):
#         # write code here
#         if number == 0 or number == 1 or number == 2:
#             return number
#         a=1
#         b=2
#         for i in range(3, number + 1):
#             a, b=b, a + b
#
#         return b
#
# s = Solution()
# print(s.rectCover(6))

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.a = 1
        self.b = 2
    def rectCover(self, number):
        # write code here
        if number == 0 or number == 1 or number == 2:
            return number
        self.a,self.b = self.b, self.a+self.b
        self.rectCover(number-1)
        return self.b
s = Solution()
print(s.rectCover(6))