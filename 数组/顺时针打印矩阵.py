#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        up=left=0
        right=len(matrix[0])-1
        down=len(matrix)-1
        result=[]
        while up <= down and left <= right:
            if left <= right:
                for i in range(left, right+1):
                    result.append(matrix[up][i])
                up+=1
            if up <= down:
                for j in range(up, down+1):
                    result.append(matrix[j][right])
                right-=1
            if left <= right and up <= down:
                for k in range(right, left-1, -1):
                    result.append(matrix[down][k])
                down-=1
            if left <= right and up <= down:
                for z in range(down, up-1, -1):
                    result.append(matrix[z][left])
                left+=1
        return result

s = Solution()
print(s.printMatrix([[1,2,3,4,5]]))
