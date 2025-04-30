class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node
        return

    def dequeue(self):
        if self.is_empty():
            print('queue is empty')
            return
        delete_node = self.head
        self.head = self.head.next
        return delete_node

    def peek(self):
        return self.head.data
        return

    def is_empty(self):
        return self.head is None
        return

queue = Queue()
queue.enqueue(4)
print(queue.peek())
queue.enqueue(2)
print(queue.peek())
queue.enqueue(3)
print(queue.peek())