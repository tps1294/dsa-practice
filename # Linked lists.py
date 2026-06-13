# Linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):

        if self.head is None:
            print ("List is empty, no item to delete")
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        prev = None
        current = self.head
        
        while current is not None:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next

        print(f"{data} not found in list")
        


        




ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.print_list()

ll.prepend(0)
ll.print_list()

ll.delete(2)
ll.print_list()

ll.delete(0)
ll.print_list()

