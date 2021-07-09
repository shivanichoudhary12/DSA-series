#### everything about linked list

## first you have to start with a node/element -> that is a single unit in linked list

class Node(object):
    def __init__(self,data):
        self.val = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self,item):
        if not self.head:
            self.head = Node(item)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(item)
            
