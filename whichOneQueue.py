import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item, priority):
        heapq.heappush(self.items, (priority, item))

    def dequeue(self):
        if self.is_empty():
            return None
        return heapq.heappop(self.items)[1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
class WhichOneQueue:
    def __init__(self, string):
        self.queue = PriorityQueue()
        for char in string:
            self.enqueue(char)

    def enqueue(self, item):
        self.queue.enqueue(item, -ord(item)) # Use negative ASCII value to simulate max-heap

    def dequeue(self):
        return self.queue.dequeue()

    def __str__(self):
        items = []
        temp_queue = PriorityQueue()
        while not self.queue.is_empty():
            item = self.queue.dequeue()
            items.append(item)
            temp_queue.enqueue(item, -ord(item))

        self.queue = temp_queue
        return ''.join(items)

    def is_empty(self):
        return self.queue.is_empty()

    def size(self):
        return self.queue.size()
	
