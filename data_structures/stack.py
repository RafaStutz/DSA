class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop():
        if not self.head:
            return "the stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def isEmpty(self):
        return self.size == 0

    def stackSize(self):
        return self.size
        
# Time Complexity: O(1) for push, pop, isEmpty, and stackSize operations.
# Space Complexity: O(n) where n is the number of elements in the stack, as we need to store each element in the stack.
