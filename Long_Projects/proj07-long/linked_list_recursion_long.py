"""
Author: Nishant Athawale
Date: 13th March 2022
Assignment: Long Project 7: Annoying Recursion Long
Class: CSC 120
Section Leader: Jason L'Italien
Section : #5
Description: In this assignment, I develop a few functions which use
            recursion to:
            1. Create a Linked List from arrays.
            2. Make delete alternate elements from a give list
            3. Create a linked list containing tuples made from Nodes of
               two different Linked Lists.
By default (unless you tell a function to return something else),
all functions return None. None is actually a special type of object.
This is important because if None is a value, "returns nothing,"
"doesn't return anything," and "no returns" are incorrect.
"""


from list_node import *


def array_to_list_recursive(data):
    """
        This function recursively builds a Linked List with each node
        containing elements from a given list of elements
        Parameters:
        data: List of elements which are to be converted into nodes of a
        linked lists.
        head: The head node of the new linked list.
    """
    if len(data) == 0:
        return None
    elif len(data) == 1:
        head = ListNode(data[0])
        return head
    else:
        head = ListNode(data[0])
        head.next = array_to_list_recursive(data[1:])
        return head


def accordion_recursive(head):
    """
        This function recursively deletes odd indexed elements from
        a linked list. (Indexing starts from 1)
        Parameters:
        head: The head node of the linked list
        Returns:
        head.next: The next List object.
    """
    if head is None:
        return None
    elif head.next is None:
        return None
    elif head.next.next is None:
        return head.next
    else:
        head.next.next = accordion_recursive(head.next.next)
        return head.next


def pair_recursive(head1, head2):
    """
        This function recursively builds a linked list of tuples
        which are made from Nodes of two separate Linked Lists.
        Parameters:
        head1: Head node of the first Linked List
        head2: Head node of the second Linked List
        Returns:
        head_out: Pointer of the newly formed ListNode object.
    """
    if head1 is None or head2 is None:
        return None
    else:
        tup = (head1.val, head2.val)
        head_out = ListNode(tup)
        head_out.next = pair_recursive(head1.next, head2.next)
        return head_out
