"""
Author: Nishant Athawale
Date: 13th March 2022
Assignment: Long Project 7: Annoying Recursion Long
Class: CSC 120
Section Leader: Jason L'Italien
Section : #5
Description: In this assignment, I develop a function which recursively
            builds and return a list of first "n" numbers in Fibonacci
            sequence where "n" is the user input.
By default (unless you tell a function to return something else),
all functions return None. None is actually a special type of object.
This is important because if None is a value, "returns nothing,"
"doesn't return anything," and "no returns" are incorrect.
"""


def annoying_fibonacci_sequence(n):
    """
        This function recursively builds and return a list of first "n"
        numbers in Fibonacci sequence where "n" is the user input.
        Parameters:
        n: Number of desired Fibonacci sequence numbers.
        Returns:
        arr : A list of numbers from Fibonacci sequence.
        """
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    elif n == 3:
        return [0, 1, 1]
    elif n == 4:
        arr = annoying_fibonacci_sequence(n-1)
        arr.append(arr[-1]+arr[-2])
        return arr
    elif n == 5:
        arr = annoying_fibonacci_sequence(n - 1)
        arr.append(arr[-1] + arr[-2])
        return arr

    elif n == 6:
        arr = annoying_fibonacci_sequence(n - 1)
        arr.append(arr[-1] + arr[-2])
        return arr
    else:
        arr = annoying_fibonacci_sequence(n - 1)
        arr.append(arr[-1] + arr[-2])
        return arr
