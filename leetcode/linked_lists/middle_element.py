class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TwoPassSolution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        
        half = size // 2

        new_curr = head
        for _ in range(half):
            new_curr = new_curr.next
        return new_curr

# Time Complexity: O(N)
# Space Complexity: O(1)

class FastSlowSolution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


# Time Complexity: O(N)
# Space Complexity: O(1)