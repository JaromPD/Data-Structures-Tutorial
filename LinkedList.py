class LinkedList:

    class Node:
        def __init__(self, data): # COLON
            self.data = data
            self.next = None
            self.prev = None
    
    def __init__(self): # COLON
        self.head = None
        self.tail = None

    def insert_head(self, value): # COLON
        new_node = LinkedList.Node(value)
        if self.head is None: # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_tail(self, value): # DECLERATION
        new_node = LinkedList.Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_head(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head is not None:
            self.head.next.prev = None
            self.head = self.head.next

    def remove_tail(self):
        if self.tail == self.head:
            self.head = None
            self.tail = None
        elif self.tail is not None:
            self.tail = self.tail.prev
            self.tail.next = None

    def insert_after(self, value, new_value): # COLON
        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr == self.tail:
                    self.insert_tail(new_value)
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr
                    new_node.next = curr.next
                    curr.next.prev = new_node
                    curr.next = new_node
                return
            curr = curr.next

    def remove(self, value): # COMMA
        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr == self.head:
                    self.remove_head()
                elif curr == self.tail:
                    self.remove_tail()
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
            curr = curr.next

    def replace(self, old_value, new_value):
        curr_value = self.head
        while curr is not None:
            if curr.data == old_value:
                curr.data = new_value
            curr = curr.next

    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr.data
            curr = curr.next

    def __reversed__(self):
        curr = self.tail
        while curr is not None:
            yield curr.data
            curr = curr.prev

    def __str__(self):
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output