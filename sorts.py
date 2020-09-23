# -*- coding: utf-8 -*-
"""
ABSTRACT:
    This file has various sorting algorithms applied to an array.

ALGORITHMS:
    - Insertion sort
    - Selection sort

CONTRIBUTOR:
    Paras Pandya [GitHub: paras4eva]

PYLINT:
    10 / 10
"""


class Sort():
    """
    Class to define various sorting algorithms to understand it works
    differently to achieve same result.
    """

    def __init__(self, array):
        """
        Instantiate method to define an object with given array.

        Parameters
        ----------
        array : List (of numerics)
            Input on which different sorting to apply.

        Returns
        -------
        None.

        """
        self._list = array

    def insertion(self):
        """
        Method to demonstrate insertion sort on a list. It can be
        used for small list or nealy sorted list.

        TIME COMPLEXITY: O(n^2)

        Returns
        -------
        Sorted list using insertion sort algorithm.

        """
        for i in range(1, len(self._list)):
            # Load predecessor
            j = i - 1
            # Load key value to compare
            k = self._list[i]

            # Shift every predecessor elements greater than key value
            # by one position to right
            while j >= 0 and self._list[j] > k:
                self._list[j+1] = self._list[j]
                j -= 1

            # Insert key element to min position
            self._list[j+1] = k

        return self._list

    def selection(self):
        """
        Method to demonstrate selection sort on a list. It can be
        used when memory write is costlier operation. Because, it
        makes no more than O(n) swaps.

        TIME COMPLEXITY: O(n^2)

        Returns
        -------
        Sorted list using selection sort algorithm.

        """
        for i in range(len(self._list)-1):
            # Set index to keep minimun value
            ind = i

            # Iterate through all elements to its right side finding
            # minimum, and storing index value.
            for j in range(i+1, len(self._list)):
                if self._list[j] < self._list[ind]:
                    ind = j

            # Swap index values
            temp = self._list[ind]
            self._list[ind] = self._list[i]
            self._list[i] = temp

        return self._list


if __name__ == "__main__":
    l1 = [8, 4, 2, 1, 5, 3, 9, 11, 7, 10]
    srt = Sort(l1)
    print("INSERTION:", srt.insertion())
    print("SELECTION:", srt.selection())
