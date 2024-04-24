import random


class Queue:
    """
    A class used to represent a Queue

    ...

    Attributes
    ----------
    content : list
        a list containing the queue's elements
    maxQueueLength : int
        the maximum number of elements the queue can hold
    minQueueLength : int
        the minimum number of elements the queue can hold

    Methods
    -------
    get_queue_length():
        Returns the current number of elements in the queue
    add_element(element, index=-1):
        Adds a single element to the queue at the specified index
    add_elements(elements, index=-1):
        Adds multiple elements to the queue at the specified index
    get_element(index=0, remove_element=True):
        Retrieves an element from the queue at the specified index
    shuffle_queue():
        Randomly rearranges the elements in the queue
    """

    def __init__(self, max_queue_length: int = 536870912, min_queue_length: int = 0) -> None:
        """
        Constructs all the necessary attributes for the queue object.

        Parameters
        ----------
            max_queue_length : int, optional
                Maximum number of elements the queue can hold (default is 536870912)
            min_queue_length : int, optional
                Minimum number of elements the queue can hold (default is 0)
        """

        self.content: list = []
        self.maxQueueLength: int = max_queue_length
        self.minQueueLength: int = min_queue_length

    def get_queue_length(self):
        """Returns the current number of elements in the queue"""
        return len(self.content)

    def add_element(self, element, index: int = -1) -> None:
        """
        Adds a single element to the queue at the specified index.

        Parameters ---------- element : any The element to be added to the queue index : int, optional The index at
        which the element should be inserted (default is -1, which appends the element to the end of the queue)
        """

        if (self.get_queue_length() + 1) < self.maxQueueLength:
            if index != -1:
                self.content.insert(index, element)
            else:
                self.content.append(element)
        else:
            raise Exception("Queue exceeds max length of " + str(self.maxQueueLength) +
                            "\n change maxQueueLength if desired")

    def add_elements(self, elements: list, index: int = -1) -> None:
        """
        Adds multiple elements to the queue at the specified index.

        Parameters ---------- elements : list The elements to be added to the queue index : int, optional The index
        at which the elements should be inserted (default is -1, which appends the elements to the end of the queue)
        """

        if (self.get_queue_length() + len(elements)) < self.maxQueueLength:
            for element in elements:
                if index != -1:
                    self.content.insert(index, element)
                else:
                    self.add_element(element)
        else:
            raise Exception("Queue exceeds max length of " + str(self.maxQueueLength) +
                            "\n change maxQueueLength if desired")

    def get_element(self, index: int = 0, remove_element: bool = True):
        """
        Retrieves an element from the queue at the specified index.

        Parameters
        ----------
            index : int, optional
                The index of the element to be retrieved (default is 0)
            remove_element : bool, optional
                Whether the element should be removed from the queue after being retrieved (default is True)

        Returns
        -------
            The element at the specified index
        """

        if self.get_queue_length() > self.minQueueLength:
            if remove_element:
                return self.content.pop(index)
            else:
                return self.content[index]
        else:
            raise Exception("Queue is less than min length of " + str(self.minQueueLength) +
                            "\n change minQueueLength if desired")

    def shuffle_queue(self) -> None:
        """Randomly rearranges the elements in the queue"""
        current_content = list(self.content)
        current_length = self.get_queue_length()
        self.content = []
        for element in current_content:
            n = random.randint(0, current_length - 1)
            self.content.insert(n, element)
