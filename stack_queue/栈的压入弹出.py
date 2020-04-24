#!/usr/bin/env Python
# coding=utf-8
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        assist_stack = []
        while popV:
            #如果assist_stack的最后一个元素和popV的第一个元素相同，则将assist_stack和popV弹出
            if assist_stack and popV[0] == assist_stack[-1]:
                assist_stack.pop()
                popV.pop(0)
            #如果pushV压入assist_stack中
            elif pushV:
                assist_stack.append(pushV.pop(0))
            else:
                return False
        return True

# class Solution:
#     def IsPopOrder(self, pushV, popV):
#         # write code here
#         if popV[0] not in pushV:
#             return False
#         index = pushV.index(popV[0])
#         if index == 0:
#             return pushV == popV
#         else:
#             for i in pushV[(index+1):]:
#                 if i not in popV[1:(1+len(pushV[(index+1):]))]:
#                     return False
#             return pushV[(index-1)::-1]== popV[1+len(pushV[(index+1):]):]

s = Solution()
print(s.IsPopOrder([1,2,3,4,5],[3,5,4,2,1]))