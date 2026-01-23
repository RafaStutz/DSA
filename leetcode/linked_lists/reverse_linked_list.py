class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def reverse_list(self, head: Node) -> Node:
        current = head
        previous = None

        while current:
            temp = current.next             # Store next node
            current.next = previous         # Reverse the pointer/link
            previous = current              # Move previous to current node
            current = temp                  # Move to the next node
        return previous





