#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution():
    def simpy(self,input):
        path_list = []
        for i in list(input):
            while str(i).isalpha():
                path_list.append(i)
                continue
        return "/"+path_list.pop(-1)

if __name__ == '__main__':
    s = Solution()
    a = s.simpy("/a/./b/../../c/")
    print(a)