class Queue:
    def __init__(self, limit=5) -> None:
        self.front = None
        self.rear = None
        self._q = []
        self._limit = limit
        self._size = 0

    def enQueue(self, data):
        if self._size == self._limit:
            raise Exception("Overflow")
        else:
            self._q.append(data)
            if self.front is None:
                self.front = self.rear = 0
            else:
                self.rear = self._size
            self._size += 1

    def deQueue(self):
        if self._size == 0:
            raise Exception("Underflow")
        else:
            self._q.pop(0)
            self._size -= 1
            if self._size == 0:
                self.front = self.rear = None
            else:
                self.rear = self._size - 1
