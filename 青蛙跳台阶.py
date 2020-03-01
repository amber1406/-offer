# class Solution:
#     def jumpFloor(self, number):
#         # write code here
#         if number <= 0:
#             return -1
#         elif number == 1:
#             return 1
#         elif number == 2:
#             return 2
#         else:
#             return self.jumpFloor(number-1)+self.jumpFloor(number-2)
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.a=1
        self.b=2

    def jumpFloor(self, number):
        # write code here
        if number <= 0:
            return -1
        elif number == self.a or number == self.b:
            return number
        for i in range(3,number+1):
            self.a,self.b = self.b,self.a+self.b
        return self.b


if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor(5))