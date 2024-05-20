#!/bin/usr/python3

"""
defines the node of a single linked list
"""


class Node:
    """
    class defines the node of a single linked list

    Args:
    """
    def __int__(self, data, next_node=None):
        self.data = data
        self.node = next_node

    @property
    def data(self):
        """
        return value for node
        """
        return self.__data

    @data.setter
    def data(self, value):

    """
    sets the value for node
    """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        gets the value of the next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        gets the next valaue
        """
    self.see= value


