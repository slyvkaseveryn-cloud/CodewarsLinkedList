from preloaded import Node

def linked_list_from_string(l: str) -> Node | None:
    parts = l.split(' -> ')
    parts.pop()
    head = None
    for i in parts[::-1]:
        head = Node(int(i), head)
    return head
