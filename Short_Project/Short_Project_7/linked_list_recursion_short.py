def is_rev_sorted(head):
    if head is None or head.next is None:
        return True
    else:
        curr = head
        while curr.next is not None:
            if curr.val < curr.next.val:
                return False
            else:
                curr = curr.next
        return True


def is_rev_sorted_recursive(head):
    if head is None or head.next is None:
        return True
    else:
        curr = head
        if curr.next is None:
            return True
        elif curr.val < curr.next.val:
            return False
        else:
            return is_rev_sorted_recursive(curr.next)

