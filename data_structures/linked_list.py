# -*- coding: utf-8 -*-
"""
ABSTRACT:
    This file provides data structures along with ADT

DATA STRUCTURES:
    - Linked list

CONTRIBUTOR:
    Paras Pandya [GitHub: paras4eva]

PYLINT:
    9.83 / 10 [too-few-public-methods]
"""


class Node():
    """
    Class to provide linked list structure.
    """

    def __init__(self, data, ll_type="single", sentinal=False):
        """
        Instantiate node with suitable parameters. Sentinals will not
        have data parameter [e.g. header]

        Parameters
        ----------
        data : ANY
            Data to store as element.
        ll_type : STRING, optional
            Type of linked list. The default is single.
        sentinal : BOOLEAN, optional
            To create node of element or sentinals. The default is False.

        Returns
        -------
        None.

        """
        self.next = None
        # Skip assigning data in case of sentinal
        if not sentinal:
            self.data = data
        if ll_type.lower() == "double":
            self.prev = None
        else:
            if ll_type.lower() != "single":
                raise Exception("LINKED LIST: Not supported type:",
                                ll_type)


class LinkedList():
    """
    Class demonstrating linked list ADT.
    """

    def __init__(self, ll_type="single"):
        """
        Method to instantiate linked list header [sentinal] node.

        Returns
        -------
        None.

        """
        self._type = ll_type
        self.header = Node(None, self._type, True)

    def prepend(self, obj):
        """
        Method to insert object in front of linked list.

        Parameters
        ----------
        obj : ANY
            Element to insert.

        Returns
        -------
        None.

        """
        element = Node(obj, self._type)
        if self.header.next is None:
            # If linked list is empty
            if self._type == "double":
                element.prev = self.header
            self.header.next = element
        else:
            # Insert logic otherwise
            if self._type == "double":
                self.header.next.prev = element
                element.prev = self.header
            element.next = self.header.next
            self.header.next = element

    def append(self, obj):
        """
        Method to append given element at the end of linked list.

        Parameters
        ----------
        obj : ANY
            Element to append.

        Returns
        -------
        None.

        """
        element = Node(obj, self._type)
        tail = self.header
        # Fetch last element
        while tail.next is not None:
            tail = tail.next
        # Append logic
        if self._type == "double":
            element.prev = tail
        element.next = tail.next
        tail.next = element

    def remove(self, obj):
        """
        Method to remove given element from linked list.

        Parameters
        ----------
        obj : ANY
            Element to be removed.

        Returns
        -------
        data : ANY
            Returns element removed.

        """
        tail = self.header.next
        # Find object with given element data
        while tail:
            if tail.data == obj:
                break
            tail = tail.next
        if not tail:
            # If requested obj is not present
            print("ERROR: No object with element:", obj)
            return None
        # Remove logic
        data = tail.data
        if self._type == "double":
            tail.prev.next = tail.next
            if tail.next is not None:
                # If element not last on linked list
                tail.next.prev = tail.prev
        # Clear references
            tail.prev = None
        tail.next = None
        # Return removed data to review
        return data


if __name__ == "__main__":
    ll = LinkedList("double")
    ll.append(1)
    ll.append(2)
    ll.prepend(3)
    print(ll.header.next.next.prev.data)
    ll.remove(3)
    print(ll.header.next.next.data)
