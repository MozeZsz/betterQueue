import random
from typing import Any, List

# Custom exception class for when the queue is full
class QueueFullException(Exception):
    pass

# Custom exception class for when the queue is empty
class QueueEmptyException(Exception):
    pass

# Queue class
class Queue:
    # Initialize the queue with a maximum and minimum length
    def __init__(self, max_queue_length: int = 536870912, min_queue_length: int = 0) -> None:
        self.content: List[Any] = []  # The content of the queue
        self.maxQueueLength: int = max_queue_length  # The maximum length of the queue
        self.minQueueLength: int = min_queue_length  # The minimum length of the queue

    # Get the current length of the queue
    def get_queue_length(self) -> int:
        return len(self.content)

    # Add an element to the queue at a specific index, or at the end if no index is provided
    def add_element(self, element: Any, index: int = -1) -> None:
        if (self.get_queue_length() + 1) > self.maxQueueLength:
            raise QueueFullException(
                f"Queue exceeds max length of {self.maxQueueLength}. Change maxQueueLength if desired.")
        if index != -1:
            self.content.insert(index, element)
        else:
            self.content.append(element)

    # Add multiple elements to the queue at a specific index, or at the end if no index is provided
    def add_elements(self, elements: List[Any], index: int = -1) -> None:
        if (self.get_queue_length() + len(elements)) > self.maxQueueLength:
            raise QueueFullException(
                f"Queue exceeds max length of {self.maxQueueLength}. Change maxQueueLength if desired.")
        for element in elements:
            self.add_element(element, index)

    # Get an element from the queue at a specific index, and optionally remove it from the queue
    def get_element(self, index: int = 0, remove_element: bool = True) -> Any:
        if self.get_queue_length() < self.minQueueLength:
            raise QueueEmptyException(
                f"Queue is less than min length of {self.minQueueLength}. Change minQueueLength if desired.")
        if remove_element:
            return self.content.pop(index)
        else:
            return self.content[index]

    # Shuffle the elements in the queue
    def shuffle_queue(self) -> None:
        random.shuffle(self.content)