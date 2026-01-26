class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def reverse_list(self, head: Node) -> Node:
        current = head
        previous = None

        while current:
            nxt = current.next             # Store next node in a temporary variable
            current.next = previous         # Reverse the pointer/link
            previous = current              # Update previous node: move it to current node
            current = nxt                   # Update current node: move it to the next node
        return previous


# Time Complexity: O(n) - We traverse the entire linked list once.
# Space Complexity: O(1) - We use a constant amount of extra space.




