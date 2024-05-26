class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
	

def josephus(n, k):
    queue = Queue()
    for i in range(1, n + 1):
        queue.enqueue(i)

    while queue.size() > 1:
        for _ in range(k - 1):
            queue.enqueue(queue.dequeue())
        queue.dequeue() # Remove the k-th person

    return queue.dequeue()