# -*- coding: utf-8 -*-
"""
ABSTRACT:
    This file provides data structures along with ADT

DATA STRUCTURES:
    - Stack

CONTRIBUTOR:
    Paras Pandya [GitHub: paras4eva]

PYLINT:
    10 / 10
"""


class DataStructure():
    """
    Class to demonstrate data structures along with ADTs
    """

    def __init__(self, size, ds_type="Stack"):
        """
        Instantiate with requested type of data structure with given
        size.

        Parameters
        ----------
        size : INTEGER
            Defines maximum size of data structure.
        ds_type : STRING, optional
            Type of data structure to implement. The default is "Stack".

        Returns
        -------
        None.

        """
        # Protected: define parameters
        self._data_struct = ds_type.lower()
        self._size = size
        self._top = -1
        # Private: List to store data [list based]
        self.__list = [None] * self._size

    def push(self, obj):
        """
        STACK: method to add/push data on to given stack[list].

        Parameters
        ----------
        obj : ANY
            Object to be added.

        Returns
        -------
        None.

        """
        if self.size() == self._size:
            # Error if stack is full
            print("ERROR: Stack full")
        else:
            self._top += 1
            self.__list[self._top] = obj

    def pop(self):
        """
        STACK: method to remove/pop last element added from
        stack[list].

        Returns
        -------
        ANY
            Object removed from top of stack.

        """
        obj = None
        if self.is_empty():
            print("ERROR: Stack empty")
        else:
            # Store top element and replace with None
            obj = self.__list[self._top]
            self.__list[self._top] = None
            self._top -= 1
        return obj

    def is_empty(self):
        """
        Method to check if defined data structure is empty

        Returns
        -------
        bool
            True if data structure is empty, False otherwise.

        """
        if self._top == -1:
            return True
        return False

    def top(self):
        """
        STACK: method to show top of the stack without removing it

        Returns
        -------
        ANY
            Object present at top of the stack.

        """
        return self.__list[self._top]

    def size(self):
        """
        Method to return size of defined data structure.

        Returns
        -------
        INTEGER
            Size of populated data structure.

        """
        return self._top + 1


if __name__ == "__main__":
    ds = DataStructure(1, "stack")
    print("EMPTY?:", ds.is_empty())
    ds.push(1)
    print("EMPTY?:", ds.is_empty())
    ds.push(2)
    print("TOP:", ds.top())
    print("SIZE:", ds.size())
    print("POP:", ds.pop())
    print("EMPTY?:", ds.is_empty())
    ds.pop()
