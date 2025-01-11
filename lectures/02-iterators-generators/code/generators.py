def generator():
    """
    A simple generator that exposes the values 1, 2, and 3

    Yields:
        int: an integer object.
    """
    # first iteration
    value = 1
    yield value

    # second iteration
    value += 1
    yield value

    # third iteration
    value += 1
    yield value


def simulated_range(start, stop, step=1):
    current = start

    while current < stop:
        # expose the current value
        yield current

        # and when execution is picked back up, increase the value of current
        current += step
    
    # no need to return!


def main():
    gen = generator()
    print(f"The {gen} object is of type {type(gen)}.")

    print(next(gen))
    print(next(gen))
    print(next(gen))
    # print(next(gen)) # error

    for integer in simulated_range(3, 10):
        print(integer)


if __name__ == "__main__":
    main()
