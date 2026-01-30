# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        currA = headA
        currB = headB
        while currA != currB:                # Loop until both pointers meet
            if currA:
                currA = currA.next           # Move to the next node in list A
            else:
                currA = headB                # Switch to head of list B if reached the end

            if currB:
                currB = currB.next           # Move to the next node in list B
            else:
                currB = headA                # Switch to head of list A if reached the end


        return currA                         # Return the intersection node or None if no intersection

# Time Complexity: O(m + n) where m and n are the lengths of the two linked lists.
# Space Complexity: O(1) as we are using only constant extra space.