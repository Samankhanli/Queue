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
	
