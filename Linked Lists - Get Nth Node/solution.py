from preloaded import Node

def get_nth(node, index):
    if node is None or index < 0:
        raise ValueError("Invalid node or index")

    current = node
    count = 0

    while current:
        if count == index:
            return current

        count += 1
        current = current.next

    raise ValueError("Index out of bounds")
  