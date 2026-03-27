class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head or not head.next:
        raise ValueError("List must have at least two nodes")

    first_head = head
    second_head = head.next

    curr_first = first_head
    curr_second = second_head

    while curr_second and curr_second.next:
        curr_first.next = curr_second.next
        curr_first = curr_first.next

        curr_second.next = curr_first.next
        curr_second = curr_second.next

    curr_first.next = None
    if curr_second:
        curr_second.next = None

    return Context(first_head, second_head)
