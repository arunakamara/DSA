class CQueue:
    def __init__(self, max_size):
        self.items = max_size * [None]
        self.max_size = max_size
        self.front = -1
        self.rear = -1

    def __repr__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)