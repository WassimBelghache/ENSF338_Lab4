#This code was created using the help of chatgpt

class CircularQueueArray:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.is_full():
            print("enqueue None")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        print(f"enqueue {item}")

    def dequeue(self):
        if self.is_empty():
            print("dequeue None")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"dequeue {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("peek None")
            return None
        item = self.queue[self.front]
        print(f"peek {item}")
        return item

# Code of operations to test
cq = CircularQueueArray(5)

cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)

cq.dequeue()
cq.dequeue()
cq.dequeue()

cq.peek()

cq.enqueue(7)
cq.enqueue(8)
cq.enqueue(9)

cq.dequeue()
cq.dequeue()

cq.peek()

cq.enqueue(10)
cq.enqueue(11)
cq.enqueue(12)
cq.enqueue(13)
cq.enqueue(14)

cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()

cq.peek()

cq.enqueue(15)
cq.enqueue(16)
cq.enqueue(17)
cq.enqueue(18)
cq.enqueue(19)

cq.dequeue()
cq.dequeue()
cq.dequeue()

cq.peek()