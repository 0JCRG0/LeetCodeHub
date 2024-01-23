from typing import Optional
import pretty_errors

"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            print(f"digit1: {digit1}")
            digit2 = l2.val if l2 is not None else 0
            print(f"digit2: {digit2}")
            print(f"carry: {carry}")

            sum = digit1 + digit2 + carry
            print(f"sum: {sum}")
            digit = sum % 10
            print(f"digit: {digit}")
            carry = sum // 10
            print(f"carry: {carry}\n")

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        
        return result


# Create linked lists from input lists
instance = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

# Call the addTwoNumbers method
result = instance.addTwoNumbers(l1, l2)


