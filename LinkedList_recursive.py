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
        if self._head is None:
            self._head = Node(value)
            return
        self.helper_add(self._head, value)


    def helper_remove(self, a_node, value):
        """
        removes one instance of the value provided
        :param a_node:
        :param value:
        :return:
        """
        if a_node is None:
            return
        elif a_node.next.data == value:
            a_node.next = a_node.next.next
        else:
            self.helper_remove(a_node.next, value)



    def remove(self, value):
        if self._head.data == value:
            self._head = self._head.next
            return
        self.helper_remove(self._head, value)


    def helper_display(self, a_node):
        """recursive display method"""
        if a_node is None:
            return
        print(a_node.data, end=" ")
        self.helper_display(a_node.next)

    def display(self):
        self.helper_display(self._head)
        

l = LinkedList()
l.add(1)
l.add(2)
l.add(2)
l.display()
l.remove(2)
l.display()
l.add(4)
l.display()

