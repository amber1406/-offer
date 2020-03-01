# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # if len(rotateArray) == 0:
        #     return 0
        # rotateArray.sort()
        # print(rotateArray[0])
        lens = len(rotateArray)
        if lens == 0:
            return 0
        if lens == 1:
            return rotateArray[0]
        left = 0
        right = lens-1

        #旋转数组由两个有序序列组成，如3,4,5,1,2
        #小于说明中间值属于前一个有序序列，此时使left = mid
        #大于否则属于后一个序列，使right = mid
        while (right-left) != 1:
            mid = (left + right) // 2
            if rotateArray[left]<rotateArray[mid]:
                left = mid
            if rotateArray[right] > rotateArray[mid]:
                right = mid
        return rotateArray[right]

if __name__ == '__main__':
    s = Solution()
    print(s.minNumberInRotateArray([6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]))
    # print(s.minNumberInRotateArray([3,4,5,1,2]))
