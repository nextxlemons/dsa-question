# Last updated: 7/27/2026, 10:56:44 PM
# simple linked List
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
9        dummy = ListNode()
10        curr = dummy
11        carry = 0
12
13        while l1 or l2 or carry:
14            x = l1.val if l1 else 0
15            y = l2.val if l2 else 0
16
17            total = x + y + carry
18            carry = total // 10
19
20            curr.next = ListNode(total % 10)
21            curr = curr.next
22
23            if l1:
24                l1 = l1.next
25            if l2:
26                l2 = l2.next
27
28        return dummy.next