# -*- coding: utf-8 -*-
"""
ABSTRACT:
    This file provides data structures along with ADT

DATA STRUCTURES:
    - Binary Search Tree (BST)

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
        self.left = None
        self.right = None


class Tree():
    """
    Class to demonstrate tree ADT.
    """

    def __init__(self, data, tree_type="binary"):
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
        self._type = tree_type.lower()

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

    def insert(self, data, node=None):
        """
        Method to insert data to tree based on tree type.

        Parameters
        ----------
        data : ANY
            BST: NUMBER | STRING.
            Data to insert in given tree.
        node : Node
            Node to be used as root for recursive insert.

        Returns
        -------
        Node
            Node with child node(s)/tree.

        """
        if node is None:
            node = self._root

        if self._type == "bst":
            if not node.data:
                node.data = data
            elif node.data <= data:
                if node.right is None:
                    node.right = Node(data)
                else:
                    node.right = self.insert(data, node.right)
            else:
                if node.left is None:
                    node.left = Node(data)
                else:
                    node.left = self.insert(data, node.left)
        return node

    def traverse(self, order="in", node=None):
        """
        Method to traverse through every node of tree in given order.

        Parameters
        ----------
        order : STRING, optional
            Supported orders: pre, in and post. The default is "in".
        node: Node
            Node to be used for recursive traversal.

        Returns
        -------
        None.

        """
        if node is None:
            node = self._root

        if order.lower() == "pre":
            print("%s" % node.data, end=" ")
            if node.left is not None:
                self.traverse(order, node.left)
            if node.right is not None:
                self.traverse(order, node.right)
        elif order.lower() == "in":
            if node.left is not None:
                self.traverse(order, node.left)
            print("%s" % node.data, end=" ")
            if node.right is not None:
                self.traverse(order, node.right)
        elif order.lower() == "post":
            if node.left is not None:
                self.traverse(order, node.left)
            if node.right is not None:
                self.traverse(order, node.right)
            print("%s" % node.data, end=" ")
        else:
            print("NOT SUPPORTED ORDER: ", order.lower())


if __name__ == "__main__":
    b_tree = Tree(9, "bst")
    b_tree.insert(15)
    b_tree.insert(11)
    b_tree.insert(5)
    b_tree.insert(7)
    b_tree.insert(3)
    print("PRE-ORDER:")
    b_tree.traverse(order="pre")
    print("\nIN-ORDER:")
    b_tree.traverse(order="in")
    print("\nPOST-ORDER:")
    b_tree.traverse(order="post")
