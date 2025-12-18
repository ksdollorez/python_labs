# Лабораторная работа № 10
### structures
``` Python

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

```
### linked_list
``` Python
class Node:
    "Узел односвязного списка"

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value})"


class SinglyLinkedList:
    "Односвязный список"

    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, value):
        "Вставить в конец"
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def prepend(self, value):
        "Вставить в начало"
        new_node = Node(value, self.head)
        self.head = new_node
        if self._size == 0:
            self.tail = new_node
        self._size += 1

    def insert(self, idx: int, value):
        "Вставка по индексу"
        if idx < 0 or idx > self._size:
            raise IndexError("index out of range")

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:
            self.append(value)
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        new_node = Node(value, current.next)
        current.next = new_node
        self._size += 1

    def remove_at(self, idx: int):
        "Удаление по индексу"
        if idx < 0 or idx >= self._size:
            raise IndexError("index out of range")

        if idx == 0:
            self.head = self.head.next
            if self._size == 1:
                self.tail = None
            self._size -= 1
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        current.next = current.next.next
        if idx == self._size - 1:
            self.tail = current

        self._size -= 1

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"SinglyLinkedList({list(self)})"

```
![](images/lab10/aayyee.jpg)