"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        l1.reverse()
        l2.reverse()
        l1 = [str(item) for item in l1]
        l2 = [str(item) for item in l2]
        num1 = ''.join(l1)
        num2 = ''.join(l2)
        sm = int(num1) + int(num2)
        sm = list(str(sm))
        sm = [int(item) for item in sm]
        sm.reverse()

        return sm