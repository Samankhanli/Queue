class CircularQueue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = self.tail = -1

    def enqueue(self, item):
        if (self.tail + 1) % self.max_size == self.head:
            return "Queue is full"
        elif self.is_empty():
            self.head = self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.max_size
        self.queue[self.tail] = item

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.queue[self.head]
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.max_size
        return item

    def is_empty(self):
        return self.head == -1

    def size(self):
        if self.is_empty():
            return 0
        elif self.tail >= self.head:
            return self.tail - self.head + 1
        else:
            return self.max_size - self.head + self.tail + 1
	
