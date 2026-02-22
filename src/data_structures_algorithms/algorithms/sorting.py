# Sorting Algorithms
unsorted_list = [5, 3, 2, 4, 1]


def bubble_sort(lst):
    """
    Bubble sort is a simple sorting algorithm that repeatedly
    compares adjacent elements and swaps them if they are in the wrong order.
    It continues this process until the list is sorted.
    Complexity: O(n^2)
    """
    for first in range(len(lst) - 1):
        for second in range(len(lst) - 1 - first):
            if lst[second] > lst[second + 1]:
                lst[second], lst[second + 1] = lst[second + 1], lst[second]
    return lst


# print(bubble_sort(unsorted_list)) # Output: [1, 2, 3, 4, 5]


def insertion_sort(lst):
    """
    Insertion sort is a simple sorting algorithm that builds
    the final sorted list one element at a time by comparing
    each element to the ones that come before it
    and inserting it into the correct position.
    Complexity: O(n^2)
    """
    for i in range(1, len(lst)):
        current_value = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > current_value:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = current_value
    return lst


# print(insertion_sort(unsorted_list))  # Output: [1, 2, 3, 4, 5]


def selection_sort(lst):
    """
    Selection sort is a simple sorting algorithm that repeatedly
    selects the minimum element from the unsorted part of
    the list and appends it to the sorted part.
    Complexity: O(n^2)
    """
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


# print(selection_sort(unsorted_list))  # Output: [1, 2, 3, 4, 5]


def merge_sort():
    """
    Merge sort is a divide-and-conquer sorting algorithm
    that recursively splits the list in half, sorts the halves,
    and then merges them back together.
    Complexity: O(n log(n))
    """
    pass
