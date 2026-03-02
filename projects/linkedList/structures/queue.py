from models.node_students import NodeStudents

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, student_id, reason):
        node = NodeStudents(student_id, reason)

        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

        self._size += 1

    def dequeue(self):
        if self.front is None:
            return None

        removed = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self._size -= 1
        return removed

    def is_empty(self):
        return self.front is None

    def size(self):
        return self._size

    def display(self):
        if self.is_empty():
            return "No hay solicitudes pendientes."

        result = []
        current = self.front
        while current:
            result.append(f"[ID: {current.student_id} | Motivo: {current.reason}]")
            current = current.next
        return " -> \n".join(result)
