# Queue Class Implementation in Python

This repository contains an implementation of a Queue data structure in Python. The Queue follows the FIFO (First In, First Out) principle and is implemented with additional features and constraints.

## Requirements

- Python 2.6+

## Installation

Clone the repository and navigate to the project directory. The project does not require any additional libraries outside the Python Standard Library.

## Features

- The Queue class is initialized with two parameters: `max_queue_length` and `min_queue_length`. These parameters define the maximum and minimum number of elements that the queue can hold.
- The `get_queue_length` method returns the current number of elements in the queue.
- The `add_element` method is used to add a single element to the queue.
- The `add_elements` method is similar to `add_element`, but it allows adding multiple elements at once.
- The `get_element` method is used to retrieve an element from the queue.
- The `shuffle_queue` method is used to randomly rearrange the elements in the queue.

## Error Handling

The Queue class raises two custom exceptions:

- `QueueFullException`: This exception is raised when an attempt is made to add an element to a queue that has reached its maximum length.
- `QueueEmptyException`: This exception is raised when an attempt is made to retrieve an element from an empty queue.

## Usage

```python
from queue import Queue

# Initialize a Queue with max length 10 and min length 2
q = Queue(10, 2)

# Add elements to the Queue
q.add_element(5)
q.add_elements([6, 7, 8])

# Get Queue length
print(q.get_queue_length())  # Output: 4

# Get and remove element from the Queue
print(q.get_element())  # Output: 5

# Shuffle the Queue
q.shuffle_queue()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
```

This `README.md` provides a brief overview of the Queue class, its features, usage, requirements, and contribution guidelines. You can customize it according to your project's needs.