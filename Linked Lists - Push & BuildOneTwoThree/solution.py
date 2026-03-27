from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def push(head, data):
    # Your code goes here.
    nn = Node(data)
    nn.next = head
    return nn

def build_one_two_three():
    res = None
    for i in range(3, 0, -1):
        res = push(res, i)
    return res
        