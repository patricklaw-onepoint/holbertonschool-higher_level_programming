#!/usr/bin/python3
"""A singly linked list"""


class Node:
    """A node on a singly linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node while keeping the list sorted

        Args:
            value (Node): The new Node to insert."""
        new = Node(value)
        if self.__head is None or self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new

    def __str__(self):
        return "\n".join(str(node.data) for node in self)

    def __iter__(self):
        node = self.__head
        while node is not None:
            yield node
            node = node.next_node
