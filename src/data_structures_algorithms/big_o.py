"""
This module explains Big O notation and provides examples of different time complexities.
Big O notation is a mathematical notation that describes the limiting behavior of a function
when the argument tends towards a particular value or infinity. In computer science,
it is used to classify algorithms according to how their run time or space requirements grow as the input size grows.

- O(1) - Constant Time
- O(log n) - Logarithmic Time
- O(n) - Linear Time
- O(n log n) - Linearithmic Time
- O(n^2) - Quadratic Time
- O(2^n) - Exponential Time
- O(n!) - Factorial Time
"""


def constant_time_example(arr):
    """
    O(1) - Constant Time: The runtime is independent of the input size.
    Accessing an element in an array by its index is a constant time operation.
    """
    return arr[0]


def logarithmic_time_example(n):
    """
    O(log n) - Logarithmic Time: The runtime grows logarithmically with the input size.
    This is typical of algorithms that divide the problem in half with each step, like binary search.
    """
    i = 1
    while i < n:
        i *= 2
    return i


def linear_time_example(arr):
    """
    O(n) - Linear Time: The runtime is directly proportional to the input size.
    Iterating through all elements in an array is a linear time operation.
    """
    total = 0
    for item in arr:
        total += item
    return total


def linearithmic_time_example(arr):
    """
    O(n log n) - Linearithmic Time: The runtime is a product of linear and logarithmic time.
    This is common for efficient sorting algorithms like Merge Sort and Quick Sort.
    """
    return sorted(arr)


def quadratic_time_example(arr):
    """
    O(n^2) - Quadratic Time: The runtime is proportional to the square of the input size.
    This is common in algorithms that involve nested iterations over the input data.
    """
    for i in range(len(arr)):
        for j in range(len(arr)):
            # Some operation
            pass


def exponential_time_example(n):
    """
    O(2^n) - Exponential Time: The runtime doubles with each addition to the input data set.
    This is common in recursive algorithms that solve a problem of size n by recursively solving two smaller problems of size n-1.
    """
    if n <= 1:
        return n
    return exponential_time_example(n-1) + exponential_time_example(n-2) # Fibonacci sequence


def factorial_time_example(n):
    """
    O(n!) - Factorial Time: The runtime grows factorially with the input size.
    This is common in algorithms that need to compute all permutations of a list.
    """
    if n == 0:
        return
    for i in range(n):
        factorial_time_example(n-1)


if __name__ == '__main__':
    my_array = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"Constant Time (O(1)): {constant_time_example(my_array)}")
    print(f"Logarithmic Time (O(log n)): {logarithmic_time_example(8)}")
    print(f"Linear Time (O(n)): {linear_time_example(my_array)}")
    print(f"Linearithmic Time (O(n log n)): {linearithmic_time_example(my_array)}")
    print("Quadratic Time (O(n^2))")
    quadratic_time_example(my_array)
    print("Exponential Time (O(2^n))")
    exponential_time_example(8)
    print("Factorial Time (O(n!))")
    factorial_time_example(3)
