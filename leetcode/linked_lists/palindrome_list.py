# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head

        # find middle of the linked list - slow will point to middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the second half of the linked list (from slow to end)
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # compare the first half and the reversed second half
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
    
# Time Complexity: O(n) - We traverse the linked list a constant number of times.
# Space Complexity: O(1) - We use a constant amount of extra space.