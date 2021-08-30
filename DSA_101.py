#Linear Search
def linear_search(list, target):

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return -1

#Binary Search
def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return -1

#Recursive Binary Search
def recursive_binary_search(list, target, start = 0, end = None):
    if end is None:
        end = len(list) - 1
    if start > end:
        return -1

    mid = (start + end) // 2

    if target == list[mid]:
        return mid
    else:
        if target < list[mid]:
            return recursive_binary_search(list, target, start, mid - 1)
        else:
            return recursive_binary_search(list, target, mid + 1, end)

#Node
class Node:

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return "<Node data: %s>" % self.data

#Singly Linked List
class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.__count = 0

    def is_empty(self):
        """
        Determines if the linked list is empty
        Takes O(1) time
        """

        return self.head is None

    def __len__(self):
        """
        Returns the length of the linked list
        Takesn O(1) time
        """

        return self.__count

    def add(self, data):
        """
        Adds new Node containing data to head of the list
        Also called prepend
        Takes O(1) time
        """

        new_head = Node(data, next_node=self.head)
        self.head = new_head
        self.__count += 1

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Returns the node or `None` if not found
        Takes O(n) time
        """

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion takes O(1) time but finding node at insertion point takes
        O(n) time.
        Takes overall O(n) time.
        """

        if index >= self.__count:
            raise IndexError('index out of range')

        if index == 0:
            self.add(data)
            return
        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

        self.__count += 1

    def node_at_index(self, index):
        """
        Returns the Node at specified index
        Takes O(n) time
        """

        if index >= self.__count:
            raise IndexError('index out of range')

        if index == 0:
            return self.head

        current = self.head
        position = 0

        while position < index:
            current = current.next_node
            position += 1

        return current

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Returns the node or `None` if key doesn't exist
        Takes O(n) time
        """

        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
                self.__count -= 1
                return current
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
                self.__count -= 1
                return current
            else:
                previous = current
                current = current.next_node

        return None

    def remove_at_index(self, index):
        """
        Removes Node at specified index
        Takes O(n) time
        """

        if index >= self.__count:
            raise IndexError('index out of range')

        current = self.head

        if index == 0:
            self.head = current.next_node
            self.__count -= 1
            return current

        position = index

        while position > 1:
            current = current.next_node
            position -= 1

        prev_node = current
        current = current.next_node
        next_node = current.next_node

        prev_node.next_node = next_node
        self.__count -= 1

        return current


    def __iter__(self):
        current = self.head

        while current:
            yield current
            current = current.next_node


    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return  '-> '.join(nodes)

#Merge Sort
def merge_sort(values):
  if len(values) <= 1:
    return values

  middle_index = len(values) // 2
  left_values = merge_sort(values[:middle_index])
  right_values = merge_sort(values[middle_index:])
  sorted_values = []
  i = 0
  j = 0

  while i < len(left_values) and j < len(right_values):
    if left_values[i] < right_values[j]:
      sorted_values.append(left_values[i])
      i += 1
    else:
      sorted_values.append(right_values[j])
      j += 1
  sorted_values += left_values[i:]
  sorted_values += right_values[j:]

  return sorted_values