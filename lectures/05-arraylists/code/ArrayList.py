from ctypes import py_object


def make_array(size):
    """
    Returns a C-style low-level array of a specified size.

    Args:
        size (int): The desired size of the array

    Returns:
        Array: A low-level array
    """
    return (size * py_object)()


class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.capacity = 1
        self.size = 1

    def append(self, value):
        pass

    def resize(self, new_size):
        pass

    def extend(self, iter_collection):
        pass

    def __len__(self):
        pass

    def __getitem__(self, idx):
        pass

    def __setitem__(self, idx, value):
        pass

    def __iter__(self):
        pass
