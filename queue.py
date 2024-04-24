import random


class Queue:
    def __init__(self, max_queue_length: int = 536870912, min_queue_length: int = 0) -> None:
        # initialise the list in which all queue objects are stored in
        self.content: list = []
        # sets the maximum amount of Objects in a single Queue
        self.maxQueueLength: int = max_queue_length
        # sets the minimum amount of Objects in a single Queue
        self.minQueueLength: int = min_queue_length

    # returns the amount of objects in the queue
    def get_queue_length(self):
        return len(self.content)
    
    # appends the list with a given object
    def add_element(self, element, index: int = -1) -> None:
        # checks if Queue is smaller than the maxQueueLength
        if (self.get_queue_length() + 1) < self.maxQueueLength:
            # checks if the Index where the Object should be inserted was changed from the default value
            if index != -1:
                self.content.insert(index, element)
            else:
                self.content.append(element)
        else:
            raise Exception("Queue exceeds max length of " + str(self.maxQueueLength) +
                            "\n change maxQueueLength if desired")
        
    # appends the list with n amount of given objects
    def add_elements(self, elements: list, index: int = -1) -> None:
        # checks if Queue is smaller than the maxQueueLength
        if (self.get_queue_length() + len(elements)) < self.maxQueueLength:
            # appends/inserts each element in elements list into the Queue
            for element in elements:
                # checks if the Index where the Object should be inserted was changed from the default value
                if index != -1:
                    self.content.insert(index, element)
                else:
                    self.add_element(element)
        else:
            raise Exception("Queue exceeds max length of " + str(self.maxQueueLength) +
                            "\n change maxQueueLength if desired")

    # returns the last object in the list and removes it if removeElement is set to true
    def get_element(self, index: int = 0, remove_element: bool = True):
        if self.get_queue_length() > self.minQueueLength:
            if remove_element:
                return self.content.pop(index)
            else:
                return self.content[index]
        else:
            raise Exception("Queue is less than min length of " + str(self.minQueueLength) +
                            "\n change minQueueLength if desired")
        
    # shuffles all objects in the queue
    def shuffle_queue(self) -> None:
        current_content = list(self.content)
        current_length = self.get_queue_length()
        self.content = []
        for element in current_content:
            n = random.randint(0, current_length - 1)
            self.content.insert(n, element)
