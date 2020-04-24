#!/usr/bin/env Python
# coding=utf-8
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
        self.lens =0
    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.lens == 0:
            self.minstack.append(node)
        elif node < self.minstack[-1]:
            self.minstack.append(node)
        else:
            self.minstack.append(self.minstack[-1])
        self.lens += 1
    def pop(self):
        # write code here
        if self.lens == 0:
            return
        self.stack.pop()
        self.minstack.pop()
        self.lens -= 1
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.minstack[-1]