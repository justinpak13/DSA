class Empty(Exception):
    pass


class LinkedQueue:
    """FIFO queue implkementation using a singly linked list for storage"""

    class _Node:
        """Lightweight, nonpublic claass for storing a singly linked node."""

        __slots__ = (
            "_element",
            "_next",
        )  # streamline memory usage as we expect to have many instances of a node class

        def __init__(self, element, next):  # Initialize node fields
            self._element = element  # reference to user's element
            self._next = next  # reference to next node

    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0

    def first(self):
        """Return but do not remove the element at the front of the queue"""

        if self.is_empty():
            raise Empty("Queue is Empty")
        return self._head._element

    def dequeue(self):
        """Remove and reutrn the first element of the queue
        Raise Empty exception if the queue is empty"""

        if self.is_empty():
            raise Empty("Queue is Empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():  # special case as queue is empty
            self._tail = None  # removed head had been the tail

        return answer

    def enqueue(self, e):
        """Add an element to the back of the queue"""
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

