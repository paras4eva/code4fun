# -*- coding: utf-8 -*-
"""
ABSTRACT:
    This file provides data structures along with ADT

DATA STRUCTURES:
    - Linked list

CONTRIBUTOR:
    Paras Pandya [GitHub: paras4eva]

PYLINT:
    10 / 10
"""


class Node():
    """
    Class to provide linked list structure.
    """
    # pylint: disable=too-few-public-methods

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
        tail = self.header
        # Find object with given element data
        while tail.next:
            if tail.next.data == obj:
                break
            tail = tail.next
        if not tail.next:
            # If requested obj is not present
            print("ERROR: No object with element:", obj)
            return None
        # Remove logic
        data = tail.next.data
        tail.next = tail.next.next
        if self._type == "double":
            if tail.next.next is not None:
                # If element not last on linked list
                tail.next.next.prev = tail.next.prev
        # Clear references
            tail.next.prev = None
        # Return removed data to review
        return data

    def travel(self):
        """
        Metod to traverse through given linked list in forward
        direction.

        Returns
        -------
        None.

        """
        if self._type == "circle":
            print("NOT SUPPORTED YET!")
            return

        lst = list()
        tail = self.header.next

        # Collect all elements of linked list
        while tail and hasattr(tail, "data") is not None:
            lst.append(tail.data)
            tail = tail.next

        print("Linked List [%s]:" % self._type, lst)


if __name__ == "__main__":
    # Main method to demonstrate functionality of linked list
    s_ll = LinkedList()
    d_ll = LinkedList("double")
    ops = ["append", "append", "prepend", "travel", "remove",
           "travel"]
    PRESENT = None
    for i, op in zip(range(len(ops)), ops):
        if op.lower() == "append":
            PRESENT = i
            s_ll.append(i)
            d_ll.append(i)
        elif op.lower() == "prepend":
            PRESENT = i
            s_ll.prepend(i)
            d_ll.prepend(i)
        elif PRESENT is not None and op.lower() == "remove":
            s_ll.remove(PRESENT)
            d_ll.remove(PRESENT)
        elif op.lower() == "travel":
            s_ll.travel()
            d_ll.travel()
        else:
            print("ERROR: Not supported operation '%s'" % op.lower())
