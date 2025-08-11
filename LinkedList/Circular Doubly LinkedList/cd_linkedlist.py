class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"{self.prev} <-> {self.value} <-> {self.next}"