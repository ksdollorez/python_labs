# В run_lab10.py
from structures import Stack, Queue
from linked_list import SinglyLinkedList


def test_stack():
    print("ТЕСТ STACK")
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Текущее состояние:", s)

    print("peek():", s.peek())
    print("pop():", s.pop())
    print("После pop:", s)

    print("is_empty:", s.is_empty())
    print("len(stack) =", len(s))


def test_queue():
    print("ТЕСТ: QUEUE")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Текущее состояние:", q)

    print("peek():", q.peek())
    print("dequeue():", q.dequeue())
    print("После dequeue:", q)

    print("is_empty:", q.is_empty())
    print("len(queue) =", len(q))


def test_linked_list():
    print("ТЕСТ: SinglyLinkedList")
    lst = SinglyLinkedList()
    lst.append(10)
    lst.append(20)
    lst.append(30)
    print("Текущее состояние:", lst)

    print("prepend(5)")
    lst.prepend(5)
    print("После prepend:", lst)

    print("insert(2, 99)")
    lst.insert(2, 99)
    print("После insert:", lst)

    print("remove_at(1)")
    lst.remove_at(1)
    print("После remove_at:", lst)

    print("len(list) =", len(lst))
    print("Элементы списка:", list(lst))


def main():
    test_stack()
    test_queue()
    test_linked_list()
    print("Все тесты выполнены")


if __name__ == "__main__":
    main()