"""LAB3: Queues
CPE202
Author: Richard Hua
"""

from linked_list import Node


class QueueArray:
    """QueueArray allows enqueuing to front or dequeuing from rear through array implementation.
    Attributes:
        capacity (int): the capacity of the list
        front (int): a pointer to front (read) of queue
        rear (int): a pointer to rear (write) of queue
        items (list): a python list construct which stores items
        num_items (int): the number of items in the list
    """
    def __init__(self, capacity, front=0, rear=0):
        #the maximum number of items that can be stored in queue
        self.capacity = capacity
        self.front = front #pointer to the front of queue
        self.rear = rear #pointer to the rear of queue
        self.items = [None] * (self.capacity + 1) #array whose size is the capacity
        self.num_items = 0

    def __eq__(self, other):
        return (self.capacity == other.capacity)\
        and (self.front == other.front)\
        and (self.rear == other.rear)\
        and (self.items == other.items)\
        and (self.num_items == other.num_items)

    def __repr__(self):
        return 'QueueArray(cap=%s, front=%s, rear=%s, items=%s, num_items=%s)'\
        % (self.capacity, self.front, self.rear, self.items, self.num_items)

    def is_empty(self):
        """ checks to see if QueueArray is empty
        """
        if self.num_items:
            return False
        return True

    def is_full(self):
        """ checks to see if QueueArray is full
        """
        if self.num_items == self.capacity:
            return True
        return False

    def enqueue(self, item):
        """Inserts item to rear of array. Throws IndexError if full.
        Args:
            item (int): the value to be inserted
        """
        if self.is_full(): # instead of rp ==(wp+1) & (cap+1)
            raise IndexError
        self.items[self.rear] = item
        # case of empty index at end of arr before wrap around
        if self.front == (self.rear + 1) % self.capacity: # arr is full
            # lets you move to last idx instead of to the beginning
            self.rear = (self.rear + 1) % (self.capacity + 1)
        else:
            # after inserting if full, wrap wp/rear around
            # possible to wrap around w/o being full
            self.rear = (self.rear + 1) % (self.capacity)
        self.num_items += 1

    def dequeue(self):
        """Removes value from front of queue and moves front pointer up one.
        """
        if self.is_empty():
            raise IndexError
        val = self.items[self.front]
        self.front = (self.front + 1) % self.capacity
        self.num_items -= 1
        return val

    #returns the number of items in the queue
    def size(self):
        """Returns number of items in array.
        """
        return self.num_items

#You must have the same functionalities for the Linked List Implementation
class QueueLinked:
    """QueueLinked allows enqueuing to front or dequeuing
        from rear through a linked list implementation.
    Attributes:
        capacity (int): the capacity of the list
        front (Node): a pointer to front (read) of queue
        rear (Node): a pointer to rear (write) of queue
        num_items (int): the number of items in the list
    """
    def __init__(self, capacity):
        #the maximum number of items that can be stored in queue
        self.capacity = capacity
        # self.node = Node(None)
        self.front = None #pointer to the front of queue
        self.rear = None #pointer to the rear of queue
        self.num_items = 0 #number of items in array

    def __eq__(self, other):
        return (self.capacity == other.capacity)\
        and (self.front == other.front)\
        and (self.rear == other.rear)\
        and (self.num_items == other.num_items)

    def __repr__(self):
        return 'QueueLinked(cap=%s, front=%s, rear=%s, num_items=%s)'\
        % (self.capacity, self.front, self.rear, self.num_items)

    def is_empty(self):
        """ checks to see if QueueLinked is empty
        """
        if self.num_items:
            return False
        return True

    def is_full(self):
        """ checks to see if QueueLinked is full
        """
        if self.num_items == self.capacity:
            return True
        return False

    def enqueue(self, item):
        """Inserts item to front of queue. Throws IndexError if full.
        Args:
            item (int): the value to be inserted
        """
        if self.is_full():
            raise IndexError
        if self.front is None:
            self.front = Node(item)
            self.rear = self.front
            self.num_items += 1
            return
        self.rear = self.helper_traverse()
        new = Node(item)
        self.rear.next = new
        self.rear = new
        self.num_items += 1

    def helper_traverse(self):
        """Helper function to traverse down list to rear for enqueue.
        """
        if self.rear.next is None:
            return self.rear
        return helper_traverse(self.rear.next)

    def dequeue(self):
        """Removes value from front of queue and moves front pointer to next node.
        """
        if self.is_empty():
            raise IndexError
        val = self.front.val
        self.front = self.front.next
        self.num_items -= 1
        return val

    #returns the number of items in the queue
    def size(self):
        """Returns number of items in list.
        """
        return self.num_items
