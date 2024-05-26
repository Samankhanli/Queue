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
def maze_solver(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = Queue()
    queue.enqueue((start, [start])) # (current position, path)

    while not queue.is_empty():
        (current, path) = queue.dequeue()
        if current == end:
            return path

        for direction in directions:
            next_row, next_col = current[0] + direction[0], current[1] + direction[1]
            if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == 0:
                maze[next_row][next_col] = -1 # Mark visited
                queue.enqueue(((next_row, next_col), path + [(next_row, next_col)]))

    return None # No path found

	
