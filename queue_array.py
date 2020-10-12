# Queue ADT - circular array implementation

class Queue:
    """Implements an efficient first-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity, init_items=None):
        """Creates a queue with a capacity and initializes with init_items"""
        self.capacity= capacity
        self.items = [None]*capacity
        self.num_items = 0
        self.front = 0
        self.rear = 0
        if init_items is not None:      
            if len(init_items) > capacity:
                raise IndexError
            else:
                self.num_items = len(init_items)
                self.items[:self.num_items] = init_items
                self.rear = self.num_items % self.capacity

    def __eq__(self, other):
        return ((type(other) == Queue)
            and self.capacity == other.capacity
            and self.get_items() == other.get_items()
            )

    def __repr__(self):
        return ("Queue({!r}, {!r})".format(self.capacity, self.get_items()))

    def get_items(self):
        if self.num_items == 0:
            return []
        if self.front < self.rear:
            return self.items[self.front:self.rear]
        else:
            return self.items[self.front:] + self.items[:self.rear]

# ----------------------------- #

    def is_empty(self):
        """Returns true if the queue is empty and false otherwise"""
        return self.num_items == 0

    def is_full(self):
        """Returns true if the queue is full and false otherwise"""
        return self.num_items == self.capacity

    def enqueue(self, item):
        """enqueues item"""
        if self.num_items < self.capacity:
            self.items[self.rear] = item
            self.rear = (self.rear + 1) % self.capacity
            self.num_items += 1
        else:
            raise IndexError

    def dequeue(self):
        """dequeues item"""
        if self.num_items > 0:
            val = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front + 1) % self.capacity
            self.num_items -= 1
            return val
        else:
            raise IndexError

    def size(self):
       """Returns the number of items in the queue"""
       return self.num_items
