# -*- coding: utf-8 -*-
"""
ABSTRACT:
    This file demonstrate data structures with ADT

DATA STRUCTURES:
    - Stack
    - Queue

CONTRIBUTOR:
    Paras Pandya [GitHub: paras4eva]

PYLINT:
    10 / 10
"""


class DataStructure():
    """
    Class to demonstrate data structures along with ADTs
    """
    # Available data structure ADTs
    STACK = "stack"
    QUEUE = "queue"
    # ADT dictionary to validate
    valid_adt = {
        STACK: ["push", "pop", "top"],
        QUEUE: ["enqueue", "dequeue", "front"]
    }

    def validate(method):
        """
        Decorator method to validate if called method is supported
        for defined data structure.

        Parameters
        ----------
        method : OBJECT [METHOD/FUNCTION]
            Method object decorated to validate.

        Returns
        -------
        allow : ANY
            Returns response from decorated method.

        """
        # pylint: disable=no-member,no-self-argument,not-callable
        def allow(self, *args, **kwargs):
            if method.__name__ in \
                    self.valid_adt.get(self.data_struct):
                return method(self, *args, **kwargs)
            print("ERROR: Method '%s' not allowed for data " \
                  "structure: '%s'" % (method.__name__,
                                       self.data_struct))
            return None
        return allow

    def __init__(self, size, ds_type="Stack"):
        """
        Instantiate with requested type of data structure with given
        size.

        Parameters
        ----------
        size : INTEGER
            Defines maximum size of data structure.
        ds_type : STRING, optional
            Type of data structure to implement. The default is
            "Stack".

        Returns
        -------
        None.

        """
        # General parameters
        self.data_struct = ds_type.lower()
        self._size = size
        # Protected: define parameters
        if self.data_struct == self.STACK:
            self._top = -1
        elif self.data_struct == self.QUEUE:
            self._front = 0
            self._rear = 0
            # Add an extra buffer to address full/empty queue issue
            self._size += 1
        else:
            raise Exception("ERROR: Not supported DS >",
                            self.data_struct)
        # Private: List to store data [list based]
        self.__list = [None] * self._size

    @validate
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

    @validate
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

    @validate
    def top(self):
        """
        STACK: method to show top of the stack without removing it

        Returns
        -------
        ANY
            Object present at top of the stack.

        """
        return self.__list[self._top]

    @validate
    def enqueue(self, obj):
        """
        QUEUE: method to add/enqueue data to rear on given
        queue[list].

        Parameters
        ----------
        obj : ANY
            Data object to enqueue.

        Returns
        -------
        None.

        """
        if self.size() == self._size - 1:
            # Error if queue is full
            print("ERROR: Queue full")
        else:
            # Add object to rear of the queue
            self.__list[self._rear] = obj
            self._rear = (self._rear + 1) % self._size

    @validate
    def dequeue(self):
        """
        QUEUE: method to remove/dequeue data object from from of
        given queue[list].

        Returns
        -------
        obj : ANY
            Data object dequeue/removed.

        """
        obj = None
        if self.is_empty():
            # Error if empty queue
            print("ERROR: Queue empty")
        else:
            # Remove and return data object
            obj = self.__list[self._front]
            self.__list[self._front] = None
            self._front = (self._front + 1) % self._size
        return obj

    @validate
    def front(self):
        """
        QUEUE: method to show element in front of queue without
        removing it.

        Returns
        -------
        ANY
            Front element on queue.

        """
        return self.__list[self._front]

    def is_empty(self):
        """
        Method to check if defined data structure is empty

        Returns
        -------
        bool
            True if data structure is empty, False otherwise.

        """
        # Empty check based on defined data structure
        if (self.data_struct == self.STACK and self._top == -1) or \
                (self.data_struct == self.QUEUE and \
                 self._front == self._rear):
            return True
        return False

    def size(self):
        """
        Method to return size of defined data structure.

        Returns
        -------
        INTEGER
            Size of populated data structure.

        """
        ds_size = -1
        if self.data_struct == self.STACK:
            # Stack size calculation
            ds_size = self._top + 1
        elif self.data_struct == self.QUEUE:
            # Size calculations for queue
            ds_size = (self._size - self._front + self._rear) % self._size
        return ds_size


if __name__ == "__main__":
    # Main method to demonstrate functionality of stack and queue
    st = DataStructure(3, "stack")
    qu = DataStructure(3, "queue")
    ops = ["empty", "add", "add", "look", "add", "size", "add", "",
           "remove", "remove", "remove", "remove", "empty", "size"]
    for i, op in zip(range(len(ops)), ops):
        if op.lower() == "empty":
            print("STACK > Empty?", st.is_empty())
            print("QUEUE > Empty?", qu.is_empty())
        elif op.lower() == "look":
            print("STACK > Top:", st.top())
            print("QUEUE > Front:", qu.front())
        elif op.lower() == "size":
            print("STACK > Size:", st.size())
            print("QUEUE > Size:", qu.size())
        elif op.lower() == "add":
            st.push(i)
            qu.enqueue(i)
        elif op.lower() == "remove":
            print("STACK > Pop:", st.pop())
            print("QUEUE > Dequeue:", qu.dequeue())
        else:
            st.front()
            qu.top()
