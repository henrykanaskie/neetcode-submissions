# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        while cur:
            if cur.val == float('inf'):
                return True
            cur.val = float('inf')
            cur = cur.next
        
        return False