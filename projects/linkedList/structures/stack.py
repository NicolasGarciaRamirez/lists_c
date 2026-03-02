from models.node import Node

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, action):
        node = Node(action)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        if self.is_empty():
            return None
        removed = self.top.data
        self.top = self.top.next
        self._size -= 1
        return removed

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size

    def display(self):
        if self.is_empty():
            return "Historial vacío."

        actions = []
        current = self.top
        while current:
            actions.append(current.data)
            current = current.next
        return " -> \n".join(actions)

    def first_action(self):
        if self.is_empty():
            return None

        current = self.top
        while current.next:
            current = current.next
        return current.data


    