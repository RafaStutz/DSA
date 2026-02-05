class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None


    def enqueue(self, value):                  # Add an element to the end of the queue
        new_node = ListNode(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    
    def dequeue(self):                         # Remove an element from the front of the queue
        if self.head is None:
            raise IndexError("Dequeue from an empty queue")
        value = self.head.value
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return value





# Time Complexity: O(1) for both enqueue and dequeue operations.
# Space Complexity: O(n) where n is the number of elements in the queue.
