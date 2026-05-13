# "Stacks and Queues classes"

class Stack:
    def __init__(self):
        self.data = []


    def push (self, item):
        self.data.append(item)
        print (f"pushed: {item}")


    def pop(self):
        if not self.data:
            print ("Stack is empty")
            return None
        return self.data.pop()
    
    
    def peek(self):
        if not self.data:
            print ("Stack is empty")
            return None
        return self.data[-1]
    
    
class Queue:
    def __init__(self):
        self.data = []


    def enqueue(self, item):
        self.data.append(item)
        print(f"Enqueued: {item}")


    def dequeue(self):
        if not self.data:
            print ("queue is empty")
            return None
        return self.data.pop(0)
    
    
    def peek(self):
        if not self.data:
            print ("queue is empty")
            return None
        return self.data[0]
    

# Stack test
s = Stack()
s.push("google.com")
s.push("youtube.com")
s.push("reddit.com")
print(s.pop())
print(s.peek())

# Queue test
q = Queue()
q.enqueue("ticket1")
q.enqueue("ticket2")
q.enqueue("ticket3")
print(q.dequeue())
print(q.peek())







