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
import math


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

    @staticmethod
    def __divide(array, pivot):
        """
        Static method used for quick sort. It devides list into three
        lists with respect to its pivot value.

        Parameters
        ----------
        array : LIST
            List to divide.
        pivot : INTEGER
            Pivot number to divide list with.

        Returns
        -------
        less : LIST
            List with elements having LESS value than pivot.
        equal : LIST
            List with elements having SAME value than pivot.
        great : LIST
            List with elements having GREATER value than pivot.

        """
        # Initialize three placeholders
        less, equal, great = list(), list(), list()

        # Iterate through all elements of list to divide and
        # populate all placeholders
        for i in array:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                great.append(i)
            else:
                equal.append(i)

        return less, equal, great

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

    def merge(self, array=None):
        """
        Method to demonstrate merge sort on a list. It is useful in
        sorting linked list as it sorts sequentially and requires low
        random access [e.g. in Array].

        TIME COMPLEXITY: O(n*Log(n))

        Parameters
        ----------
        array : LIST, optional
            To be used only for recurssive call(s). User need not
            pass any list. The default is None.

        Returns
        -------
        array : LIST
            Sorted list using merge sort algorithm.

        """
        # Used only at begining to load list
        if array is None:
            array = self._list.copy()

        # For lenght of array greater than 1. Otherwise just return
        if len(array) > 1:
            # Divide list in two half
            half = math.ceil(len(array)/2)
            list1 = array[:half]
            list2 = array[half:]

            # Recursive call(s) to divided halves
            list1 = self.merge(list1)
            list2 = self.merge(list2)
            array = list()

            # Conquer: re-arrange list with sorted elements. Run till
            # any one list goes empty
            while not (len(list1)==0 or len(list2)==0):
                if list1[0] <= list2[0]:
                    array.append(list1.pop(0))
                else:
                    array.append(list2.pop(0))

            # Add remaining list elements as it is
            if list1:
                array.extend(list1)
            else:
                array.extend(list2)

        return array

    def quick(self, array=None):
        """
        Method to demonstrate quick sort on a list. Here, pivot is
        last element of a list. There are various ways of selecting
        pivot. It works best when chosen pivot is middle value.

        TIME COMPLEXITY: O(n*Log(n)) [ Worst: O(n^2) for sorted list]

        Parameters
        ----------
        array : TYPE, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        array : TYPE
            DESCRIPTION.

        """
        # Used only at begining to load list
        if array is None:
            array = self._list

        # For lenght of array greater than 1. Otherwise just return
        if len(array) > 1:
            # Pivot selection: last element of list
            pivot = array[-1]
            # Divide given list into three parts
            lss, eql, grt = self.__divide(array, pivot)

            # Recursive calls to less and greater than parts
            lss = self.quick(lss.copy())
            grt = self.quick(grt.copy())
            array = list()

            # Conquer: merge sorted lists in following order
            array.extend(lss)
            array.extend(eql)
            array.extend(grt)

        return array


if __name__ == "__main__":
    l1 = [8, 4, 2, 1, 5, 3, 9, 6, 11, 7, 10]
    srt = Sort(l1)
    print("INSERTION:", srt.insertion())
    print("SELECTION:", srt.selection())
    print("MERGE:", srt.merge())
    print("QUICK:", srt.quick())
