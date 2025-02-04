from ctypes import py_object


def make_array(size):
    """
    Returns a low-level C-style array of the specified size.
    
    Args:
        size (int): Desired size of the array.
    Returns:
        Array: A new low-level array of the specified size.
    """
    return (size * py_object)()


class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)  # Start with capacity for 1 element
        self.capacity = 1
        self.size = 0  # Track the current number of elements

    def append(self, value):
        if self.size == self.capacity:  # Need to resize
            self.resize(self.capacity * 2)
        self.data_arr[self.size] = value
        self.size += 1

    def resize(self, new_capacity):
        """
        Resize the array to a new capacity.
        """
        new_arr = make_array(new_capacity)
        for i in range(self.size):
            new_arr[i] = self.data_arr[i]
        self.data_arr = new_arr
        self.capacity = new_capacity

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        if not 0 <= idx < self.size:
            raise IndexError("Index out of range")
        return self.data_arr[idx]

    def __setitem__(self, idx, value):
        if not 0 <= idx < self.size:
            raise IndexError("Index out of range")
        self.data_arr[idx] = value