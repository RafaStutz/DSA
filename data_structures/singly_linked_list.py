class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    
    def add_to_front(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node


    def remove_from_front(self):
        if not self.head:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        return removed_value


    def add_to_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


    def remove_from_end(self):
        if not self.head:
            return None
        if not self.head.next:
            removed_value = self.head.value
            self.head = None
            return removed_value
        prev = self.head
        current = self.head.next
        while current.next:
            prev = current
            current = current.next
        removed_value = current.value
        prev.next = None
        return removed_value
        
            
        



        
