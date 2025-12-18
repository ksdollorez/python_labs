
from collections import deque


class Stack:
    "Класс стека (LIFO) на основе списка"

    def __init__(self):
        self._data = []  # внутренняя структура

    def push(self, item):
        "Добавить элемент в стек"
        self._data.append(item)

    def pop(self):
        "Снять элемент с вершины стека"
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        "Посмотреть верхний элемент без удаления"
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        "True если стек пуст"
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"Stack({self._data})"


class Queue:
    "Класс очереди (FIFO) на основе deque"

    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        "Добавить в конец очереди"
        self._data.append(item)

    def dequeue(self):
        "Удалить первый элемент очереди"
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self):
        "Посмотреть первый элемент без удаления"
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"Queue({list(self._data)})"
