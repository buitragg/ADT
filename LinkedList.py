class Node:
    """
    Represents a node in a linked list
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A linked list implementation of the List ADT
    """

    def __init__(self):
        self._head = None

    def add(self, val):
        """
        Adds a node containing val to the linked list
        """
        if self._head is None:  # If the list is empty
            self._head = Node(val)
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = Node(val)

    def display(self):
        """
        Prints out the values in the linked list
        """
        current = self._head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def remove(self, val):
        """
        Removes the node containing val from the linked list
        """
        if self._head is None:  # If the list is empty
            return

        if self._head.data == val:  # If the node to remove is the head
            self._head = self._head.next
        else:
            current = self._head
            while current is not None and current.data != val:
                previous = current
                current = current.next
            if current is not None:  # If we found the value in the list
                previous.next = current.next

    def is_empty(self):
        """
        Returns True if the linked list is empty,
        returns False otherwise
        """
        return self._head is None

    def to_regular_list(self):
        """
        Returns a regular Python list containing the same values,
        in the same order, as the linked list
        """
        result = []
        current = self._head
        while current is not None:
            result += [current.data]
            current = current.next
        return result

    def insert(self, val, pos):
        """
        function will add a value to the desired position on a liked list,
        if position is larger than the linked lists length then it will add it to the end of the list
        if the position is 0 it will be added to the start of the list
        :param value: value to be added
        :param position: position you would like to add the value
        :return: None
        """
        if self._head is None:  # If the list is empty
            self.add(val)
            return

        if pos == 0:
            temp = self._head
            self._head = Node(val)
            self._head.next = temp
        else:
            current = self._head
            for _ in range(pos - 1):
                if current.next is None:
                    current.next = Node(val)
                    return
                current = current.next
            temp = current.next
            current.next = Node(val)
            current.next.next = temp

    def reverse(self):
        """"
                Reverses the linked list
                """
        previous = None
        current = self._head

        while current is not None:
            following = current.next
            current.next = previous
            previous = current
            current = following
        self._head = previous

