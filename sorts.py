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
    9.38 / 10 (too-few-public-methods)
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
        Method to demonstrate insertion sort on input.

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


if __name__ == "__main__":
    l1 = [8, 4, 2, 1, 5, 3, 9, 11, 7, 10]
    srt = Sort(l1)
    print("SORTED: ", srt.insertion())
