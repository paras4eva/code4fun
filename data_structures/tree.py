# -*- coding: utf-8 -*-
"""
ABSTRACT:
    This file provides data structures along with ADT

DATA STRUCTURES:
    - Binary tree

CONTRIBUTOR:
    Paras Pandya [GitHub: paras4eva]

PYLINT:
    10 / 10
"""


class Node():
    """
    Class to provide binary tree node structure
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, data):
        """
        Instantiate binary node with given data

        Parameters
        ----------
        data : ANY
            Element to be stored.

        Returns
        -------
        None.

        """
        self.data = data
        self._left = None
        self._right = None


class Tree():
    """
    Class to demonstrate tree ADT.
    """

    def __init__(self, data):
        """
        Method to instantiate binary tree root node.

        Parameters
        ----------
        data : ANY
            Element to be stored.

        Returns
        -------
        None.

        """
        self._root = Node(data)

    def root(self):
        """
        Method to return root node.

        Returns
        -------
        Node
            Class to resperent binary tree structure.

        """
        return self._root

    def is_root(self, data):
        """
        Method to check if data node is root.

        Parameters
        ----------
        data : ANY
            Data rlement to check if given data is root or not.

        Returns
        -------
        bool
            True if root has respected data, False otherwise.

        """
        if self._root.data == data:
            return True
        return False


if __name__ == "__main__":
    b_tree = Tree(1)
