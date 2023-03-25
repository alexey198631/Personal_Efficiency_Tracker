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
    class Solution:
        def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy_head = ListNode(0)
            current = dummy_head
            carry = 0
            while l1 or l2 or carry:
                total_sum = carry
                if l1:
                    total_sum += l1.val
                    l1 = l1.next
                if l2:
                    total_sum += l2.val
                    l2 = l2.next

                carry = total_sum // 10

                current.next = ListNode(total_sum % 10)

                current = current.next

            return dummy_head.next