"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToCopy = {None:None}
        itr = head
        while itr:
            copy = Node(itr.val)
            oldToCopy[itr] = copy
            itr = itr.next
        
        itr = head
        while itr:
            copy = oldToCopy[itr]
            copy.next = oldToCopy[itr.next]
            copy.random = oldToCopy[itr.random]
            itr = itr.next
        return oldToCopy[head]