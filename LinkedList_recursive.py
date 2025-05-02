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

    def helper_add(self, a_node, value):
        """
        helper function for add. iterates through the list and adds the value to the end of the list
        """
        current = a_node
        if current.next is None:
            current.next = Node(value)
            return
        self.helper_add(a_node.next, value)

    def add(self, value):
        """
        just adds the value to the end of the list using the helper function
        :param value: value to be added
        :return: None
        """
        # if the list is empty add the value as the head
        if self._head is None:
            self._head = Node(value)
            return
        self.helper_add(self._head, value)

    def helper_remove(self, a_node, prev, value):
        """
        removes one instance of the value provided
        :param a_node: keeps track of current node
        :param value: value to be added
        :param prev: keeps track of previous node
        :return: None
        """
        # if we reached the end of the list
        if a_node is None:
            return
        if a_node.next is None and a_node.data != value:
            return
        else:
            # if we are in the last node
            if a_node.data == value and a_node.next is None:
                prev.next = a_node.next
                return
            # any other node
            if a_node.data == value and a_node.next is not None:
                prev.next = a_node.next
                self.helper_remove(a_node.next, prev, value)

        self.helper_remove(a_node.next, a_node, value)

    def remove(self, value):
        if self._head is None:
            return
        # if it's a list of all same value to be removed
        if self._head.data == value:
            self._head = self._head.next
            self.remove(value)
        self.helper_remove(self._head, None, value)

    def helper_display(self, a_node):
        """recursive display method"""
        if a_node is None:
            return
        print(a_node.data, end=" ")
        self.helper_display(a_node.next)

    def display(self):
        self.helper_display(self._head)


l = LinkedList()
l.add(3)
l.add(3)
l.add(3)
l.add(3)
l.add(2)
l.display()
l.remove(2)
l.display()
