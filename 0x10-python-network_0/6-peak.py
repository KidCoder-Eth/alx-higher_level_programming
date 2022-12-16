#!/usr/bin/python3

"""
Find a peak in a list of unsorted ints
"""


def find_peak(list_of_integers):
    """Find a peak in a list of ints"""
    if not list_of_integers:
        return None
    return fp(list_of_integers, 0, len(list_of_integers) - 1,
              len(list_of_integers))


def fp(arr, low, high, n):
    """Helper function"""
    mid = low + (high - low)//2

    if (mid == 0 or arr[mid - 1] <= arr[mid]) and\
       (mid == n - 1 or arr[mid + 1] <= arr[mid]):
        return arr[mid]
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return fp(arr, low, mid - 1, n)
    else:
        return fp(arr, mid + 1, high, n)
