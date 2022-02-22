from list_node import *


def list_to_array(head):
    array = []
    curr = head
    while curr is not None:
        array.append(curr.val)
        curr = curr.next
    return array


def array_to_list(data):
    head = None
    length = len(data)
    curr = None
    if length != 0:
        for i in range(length):
            if i == 0:
                head = ListNode(data[i])
                curr = head
            else:
                curr.next = ListNode(data[i])
                curr = curr.next
        curr.next = None
    return head
                

def list_length(head):
    count = 0
    if head is None:
        count = 0
    else:
        curr = head
        while curr is not None:
            count += 1
            curr = curr.next
    return count


def is_sorted(head):
    list_len = list_length(head)
    if list_len == 0 or list_len == 1:
        return True
    else:
        curr = head
        while curr.next is not None:
            if curr.next.val < curr.val:
                return False
            curr = curr.next
        return True


def accordion(old_head):
    list_len = list_length(old_head)
    new_head = None
    if list_len >= 2:
        new_head = old_head.next
        curr = new_head
        while curr.next is not None and curr.next.next is not None:
            curr.next = curr.next.next
            curr = curr.next
        if list_len % 2 == 1:
            curr.next = None
    return new_head
